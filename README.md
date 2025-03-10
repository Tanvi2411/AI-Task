# Overview  

A Flask-based REST API that dynamically scrapes course data from [Brainlox](https://brainlox.com/courses/category/technical), processes it using TF-IDF vectorization, and provides a search functionality using cosine similarity.  

## Features  

- Scrapes course names dynamically from Brainlox  
- Uses TF-IDF embeddings for text similarity  
- Provides REST APIs to list and search courses  
- Includes a health check endpoint to verify API status  



### Install Dependencies  
```sh
pip install flask requests beautifulsoup4 scikit-learn
```  

### Run the Flask App  
```sh
python app.py
```  
By default, the API runs at:  
`http://127.0.0.1:5000/`  

## API Endpoints  

### List All Courses  
- Method: `GET`  
- Endpoint: `/list_courses`  
- Description: Fetches all available course names from Brainlox  


### Search for a Course  
- Method: `POST`  
- Endpoint: `/search`  
- Headers:  
  - `Content-Type: application/json`  
- Request Body (JSON):  
  ```json
  {"query": "Python"}
  ```


### Health Check  
- Method: `GET`  
- Endpoint: `/health`  
- Description: Checks if the API is running  
- Example Response:  
  ```json
  {"status": "API is running!"}
  ```  

## Testing API with Postman  

### Open Postman and Create a New Request  
- Open Postman  
- Click on "New Request"  
- Select the method (GET/POST)  

### Test Endpoints  

#### List All Courses (`GET /list_courses`)  
- Method: `GET`  
- URL: `http://127.0.0.1:5000/list_courses`  
 

#### Search for a Course (`POST /search`)  
- Method: `POST`  
- URL: `http://127.0.0.1:5000/search`  
- Headers:  
  - `Content-Type: application/json`  
- Body (JSON):  
  ```json
  {"query": "Python"}
  ```


#### Health Check (`GET /health`)  
- Method: `GET`  
- URL: `http://127.0.0.1:5000/health`  
- Example Response:  
  ```json
  {"status": "API is running!"}
  ```  




## Using Postman Collections  

### Export Postman Collection  
- Open Postman  
- Click on "Collections" → "New Collection"  
- Add requests (`/list_courses`, `/search`, `/health`)  
- Click "Export" and save as `Brainlox-API.postman_collection.json`  

### Import into Postman  
- Go to "File → Import"  
- Select the exported Postman collection file  
- Test the APIs easily  

## Future Improvements  

- Use LangChain + FAISS for better embeddings  
- Store course data in a database for faster retrieval  
- Deploy on AWS/GCP for public access  

