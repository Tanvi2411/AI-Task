from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Function to scrape course data from Brainlox dynamically
def scrape_courses():
    url = "https://brainlox.com/courses/category/technical"
    response = requests.get(url)
    
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    courses = []
    # Update the selector based on the actual HTML structure of Brainlox
    for course in soup.find_all("h3"):  # Example: Finding course titles inside <h3> tags
        courses.append(course.get_text(strip=True))
    
    return courses

# API: List All Courses (Fetches live data every time)
@app.route("/list_courses", methods=["GET"])
def list_courses():
    courses = scrape_courses()
    return jsonify(courses if courses else {"error": "No courses found"})

# API: Search Courses
@app.route("/search", methods=["POST"])
def search():
    query = request.json.get("query", "").strip()
    if not query:
        return jsonify({"error": "Query is required"}), 400

    courses = scrape_courses()
    if not courses:
        return jsonify({"error": "No courses found on Brainlox"}), 404

    # Compute TF-IDF embeddings dynamically
    vectorizer = TfidfVectorizer()
    course_vectors = vectorizer.fit_transform(courses)
    
    # Transform the query into the same space
    query_vector = vectorizer.transform([query])

    # Compute cosine similarity
    similarities = cosine_similarity(query_vector, course_vectors).flatten()
    top_indices = similarities.argsort()[-3:][::-1]  # Get top 3 matches

    results = [{"title": courses[i], "score": float(similarities[i])} for i in top_indices]
    
    return jsonify(results if results else {"error": "No matching courses found"})

# API: Health Check
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "API is running!"})

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
