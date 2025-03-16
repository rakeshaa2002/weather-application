# Weather Application

## Overview
This is a weather application built using **Python, Django, HTML, Tailwind CSS, JSON, and the OpenWeather API**. The application allows users to search for current weather conditions of any city worldwide.

## Features
- Fetches real-time weather data using the **OpenWeather API**.
- User-friendly interface with **Tailwind CSS** styling.
- Displays temperature, humidity, wind speed, and weather description.
- Supports searching for multiple cities.
- Error handling for invalid city names.

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, Tailwind CSS
- **Data Handling**: JSON
- **API**: OpenWeather API

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- Python (>=3.8)
- Django (>=4.0)
- A valid OpenWeather API key

### Steps to Run the Project
1. Clone this repository:
   ```sh
   git clone <repository_url>
   cd weather-application
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up your OpenWeather API key:
   - Create a `.env` file in the root directory and add:
     ```env
     OPENWEATHER_API_KEY=your_api_key_here
     ```
5. Run database migrations:
   ```sh
   python manage.py migrate
   ```
6. Start the Django server:
   ```sh
   python manage.py runserver
   ```
7. Open your browser and visit `http://127.0.0.1:8000/` to use the application.

## Usage
- Enter a city name in the search bar.
- View real-time weather data, including temperature, wind speed, and weather conditions.
- If an invalid city is entered, an error message will be displayed.

## API Integration
The application uses the **OpenWeather API** to fetch weather data. The API response is processed in JSON format and displayed on the UI.

## Project Structure
```
weather-application/
│── weather/
│   ├── templates/ (HTML Templates)
│   ├── static/ (Tailwind CSS & JS)
│   ├── views.py (Django Views)
│   ├── urls.py (URL Routing)
│   ├── models.py (Database Models)
│── manage.py
│── requirements.txt
│── .env
```

## Contributing
Feel free to contribute to the project by submitting issues or pull requests..

## Contact
For queries, reach out at: **your-email@example.com**

