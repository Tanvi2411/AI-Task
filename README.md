This project is a Flask-based REST API that dynamically scrapes course data from Brainlox, processes it using TF-IDF vectorization, and provides search functionality using cosine similarity.

 Features
Scrapes course names dynamically from Brainlox
Uses TF-IDF embeddings for text similarity
Provides REST APIs to list and search courses
✅ Health check endpoint to verify API status

  Install Dependencies
sh
Copy
Edit
pip install flask requests beautifulsoup4 scikit-learn
3.  Run the Flask App
sh
Copy
Edit
python app.py
By default, the API runs at:
📍 http://127.0.0.1:5000/

🚀 API Endpoints
Method	Endpoint	Description
GET	/list_courses	Fetches all available course names from Brainlox
POST	/search	Searches for courses based on a given query
GET	/health	Checks if the API is running
📌 Testing API with Postman
1️⃣ Open Postman and Create a New Request
Open Postman
Click on "New Request"
Select the method (GET/POST)
2️⃣ Test Endpoints
✅ List All Courses (GET /list_courses)
Method: GET
URL: http://127.0.0.1:5000/list_courses
Response Example:
json
Copy
Edit
["Python for Beginners", "Machine Learning", "Data Science"]
✅ Search for a Course (POST /search)
Method: POST
URL: http://127.0.0.1:5000/search
Headers:
Content-Type: application/json
Body (JSON):
json
Copy
Edit
{"query": "Python"}
Response Example:
json
Copy
Edit
["Python for Beginners", "Advanced Python"]
✅ Health Check (GET /health)
Method: GET
URL: http://127.0.0.1:5000/health
Response Example:
json
Copy
Edit
{"status": "API is running!"}
