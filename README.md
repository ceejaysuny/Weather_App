
```markdown
# Weather App

A simple weather application built using Django and WeatherAPI.com. This app allows users to search for the current weather of any city.

## Features

- Search for current weather information by city name.
- Display temperature, weather condition, and an appropriate weather icon.
- Beautifully styled interface.

## Technologies Used

- Django
- WeatherAPI.com
- HTML/CSS
- Python

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Python 3.x
- pip (Python package installer)
- Django

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/ceejaysuny/Weather_App.git
   cd weather-app
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory of your project and add your WeatherAPI.com API key:

   
   WEATHER_API_KEY=your_api_key_here
   ```

5. **Run migrations:**

   ```sh
   python manage.py migrate
   ```

6. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

7. **Access the application:**

   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1. Enter the name of the city you want to check the weather for in the input field.
2. Click the "Get Weather" button.
3. The app will display the current weather information for the specified city.


## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome improvements and new features!

## License

This project is licensed under the MIT License.

## Acknowledgements

- Thanks to [WeatherAPI.com](https://www.weatherapi.com/) for providing the weather data API.
- Created with Django and lots of ☕ and ❤️.
- Sign-up to get your free weather API from WeatherAPI.com

## Contact

For any questions or feedback, feel free to reach out at chijioke.ekejimbe@gmail.com.


