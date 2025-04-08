# ETL Pipeline Weather Project - Detailed Description

## Overview
This project is designed to extract weather forecast data from the Open-Meteo API, perform data transformations using Pandas, and load the processed data into a PostgreSQL database using SQLAlchemy.

## Data Extraction
- **API Endpoint:** `https://api.open-meteo.com/v1/forecast`
- **Parameters:** Includes geographical coordinates for London (latitude: 51.5074, longitude: -0.1278) and specific weather metrics like temperature, precipitation, and wind speed.

## Data Transformation
- Converts JSON response data into a Pandas DataFrame.
- Renames columns for clarity.
- Performs unit conversion for wind speed (from m/s to km/h).
- Formats time columns and adds a `load_time` for tracking when the data was loaded.

## Data Loading
- Loads the transformed DataFrame into a PostgreSQL database.
- Uses SQLAlchemy along with the `psycopg2` driver for database connectivity.
- Inserts data into a table named `weather_data`.

## Requirements and Setup
- **Python Packages:** `requests`, `pandas`, `sqlalchemy`, `psycopg2`
- **Database:** Ensure PostgreSQL is installed, running, and accessible with correct credentials.

## Future Enhancements
- Improve error handling and logging.
- Parameterize API calls for different locations.
- Expand data transformation and reporting features.
