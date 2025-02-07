**Objectives of Implementing a Database System in Company**
Data Centralization and Accessibility
Data Security and Integrity
Efficient Query Performance
 Scalability and Growth
# CarRentalSystem

## pre-requisites

- node  
- npm 
- python3
- pip3

## Installation and serve backend app

- git clone https://github.com/ArraudhahSabri/CarRentalSystem.git
- cd CarRentalSystem
- python3 -m venv .venv 
- source .venv/bin/activate
- pip install django djangorestframework
- pip install django-cors-headers
- cd backend
- python manage.py runserver

## install and serve frontend app
- cd frontend
- npm install
- npx tailwindcss -i ./src/input.css -o ./src/assets/main.css --watch

### for dev mode , hot reload
- npm run dev 

### for build assets bundling
- npm run build
  
## install and serve backend app
Create virtual environment : python3 -m venv .venv
Activate environtment : .venv\Scripts\activate
Install backend dependecies : pip install django djangorestframework
                              pip install django-cors-headers
Set up backend database : python manage.py migrate
Run backend server : cd backend python manage.py runserver

## view app
- http://localhost:5174/ (frontend)
- http://127.0.0.1:8000/ (backend)
