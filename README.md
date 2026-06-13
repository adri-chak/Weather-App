# 🌦️ Weather App

A full-stack weather application built using FastAPI, HTML, CSS, and JavaScript.

This project fetches real-time weather data from the Open-Meteo API and displays it in a modern weather dashboard.

---

## 🚀 Features

- Search weather by city name
- Real-time weather data
- Temperature display
- Wind speed display
- Weather condition detection
- Dynamic weather icons
- FastAPI REST API backend
- JavaScript Fetch API integration
- Modern glassmorphism UI
- Responsive weather dashboard

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python
- Uvicorn

### Frontend
- HTML
- CSS
- JavaScript

### External APIs
- Open-Meteo Geocoding API
- Open-Meteo Weather Forecast API

---

## 📂 Project Structure

Weather-App/

├── backend/

│ ├── main.py

│ └── weather.py

│

├── frontend/

│ ├── index.html

│ └── style.css

│

├── requirements.txt

├── .gitignore

└── README.md

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/adri-chak/Weather-App.git
cd Weather-App
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Backend

```bash
uvicorn backend.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Frontend

Open:

```text
frontend/index.html
```

or use VS Code Live Server.

---

## 📸 Current Screenshots

- Weather search interface
- Real-time weather results
- Glassmorphism weather card
- Dynamic weather condition icons

---

## 📚 Concepts Learned

- REST APIs
- FastAPI Routing
- Query Parameters
- JSON Responses
- Async Functions
- Fetch API
- CORS
- DOM Manipulation
- CSS Styling
- Git & GitHub Workflow

---

## 🚧 Upcoming Improvements

- Separate JavaScript file
- Loading animation
- Error handling
- Weather-based themes
- Mobile responsiveness
- Vercel deployment
- Public FastAPI deployment

---

## 👩‍💻 Author

Adrija Chakraborty

B.Tech Engineering Student
