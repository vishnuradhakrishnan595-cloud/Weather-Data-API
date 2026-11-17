# Weather Data API

A real-time weather application developed using **Python, FastAPI, and the OpenWeatherMap API**. The application retrieves current weather information for cities worldwide and presents it through a modern, responsive dashboard built with Tailwind CSS.

## Features

- Search for real-time weather information by city.
- Display current temperature in Celsius.
- View feels-like temperature.
- Display humidity and wind speed.
- View weather conditions and detailed descriptions.
- Responsive and modern user interface.
- Smooth animations and interactive elements.
- Fast and asynchronous API requests using HTTPX.
- Secure API key management using environment variables.
- Error handling for invalid cities and API failures.

## Technology Stack

### Backend
- Python
- FastAPI
- HTTPX
- Pydantic
- Uvicorn

### Frontend
- HTML5
- Tailwind CSS
- JavaScript

### API and Configuration
- OpenWeatherMap API
- Python-dotenv

## Project Structure

```text
Weather-Data-API/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── weather_service.py
│   │
│   └── utils/
│       └── __init__.py
│
├── frontend/
│   └── index.html
│
├── .env
├── .gitignore
└── requirements.txt
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vishnuradhakrishnan595-cloud/Weather-Data-API.git
```

### 2. Navigate to the Project Directory

```bash
cd Weather-Data-API
```

### 3. Create a Virtual Environment

```bash
python -m venv env
```

### 4. Activate the Virtual Environment

For Windows:

```cmd
env\Scripts\activate
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Configure Environment Variables

Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).

Create a `.env` file in the project root directory and add:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenWeatherMap API key.

**Security Note:** Never commit your `.env` file or expose your API credentials in a public repository. The `.env` file is excluded through `.gitignore`.

### 7. Start the Backend Server

Run the following command from the project root:

```bash
python -m uvicorn app.main:app --reload
```

The backend API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

The application provides interactive API documentation through FastAPI.

### Available Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Returns the API welcome message |
| `/health` | GET | Checks API health status |
| `/weather/{city}` | GET | Retrieves current weather information for a city |

### Example API Request

```http
GET http://127.0.0.1:8000/weather/Kochi
```

### Example API Response

```json
{
  "city": "Kochi",
  "country": "IN",
  "temperature": 30.5,
  "feels_like": 34.2,
  "humidity": 75,
  "wind_speed": 3.5,
  "weather": "Clouds",
  "description": "scattered clouds"
}
```

### Interactive API Documentation

Once the backend server is running, access:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Running the Frontend

Open a separate terminal and navigate to the frontend directory:

```cmd
cd frontend
```

Start the frontend development server:

```cmd
python -m http.server 5500
```

Open the application in your browser:

http://127.0.0.1:5500

**Note:** Keep both the FastAPI backend and frontend servers running while using the application.

## Environment Variables

The application uses environment variables to securely manage API credentials.

| Variable | Description |
|---|---|
| `OPENWEATHER_API_KEY` | OpenWeatherMap API authentication key |

Ensure that `.env` is included in `.gitignore` before pushing the project to GitHub.

## Project Preview

Add application screenshots to the repository to demonstrate the user interface.

Example:

```markdown
![Weather Dashboard](screenshots/dashboard.png)
```

## Future Enhancements

- Implement a five-day weather forecast.
- Add weather data caching.
- Maintain recent city search history.
- Introduce dynamic weather icons and backgrounds.
- Support Celsius and Fahrenheit conversion.
- Add automated API testing using Pytest.
- Deploy the application to a cloud platform.

## Author

**Vishnu Radhakrishnan Nair**

Python Full Stack Developer

- GitHub: [vishnuradhakrishnan595-cloud](https://github.com/vishnuradhakrishnan595-cloud)

---

If you find this project useful, consider giving the repository a star.

**Developed using Python, FastAPI, and modern web technologies.**
