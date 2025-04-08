import requests
import pandas as pd

# Define the API endpoint for Open-Meteo
url = "https://api.open-meteo.com/v1/forecast"

# Define the parameters for the request (e.g., London)
params = {
    "latitude": 51.5074,      # Latitude for London
    "longitude": -0.1278,     # Longitude for London
    "hourly": "temperature_2m,precipitation,wind_speed_10m",  # Data to fetch
    "timezone": "Europe/London"
}

# Make the API request
response = requests.get(url, params=params)
print("Status code:", response.status_code)

if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    # Extract relevant data (hourly forecast)
    hourly_data = data["hourly"]
    
    # Convert to a DataFrame
    df = pd.DataFrame(hourly_data)
    
    # Rename columns to be more user-friendly
    df.rename(columns={
        "temperature_2m": "Temperature (°C)",
        "precipitation": "Precipitation (rain)",
        "wind_speed_10m": "Wind Speed (km/h)"
    }, inplace=True)
    
    # Convert wind speed from m/s to km/h (1 m/s = 3.6 km/h)
    if "Wind Speed (km/h)" in df.columns:
        df["Wind Speed (km/h)"] = df["Wind Speed (km/h)"] * 3.6
    
    # Convert the 'time' column to datetime for better readability and filtering
    if 'time' in df.columns:
        df['time'] = pd.to_datetime(df['time'])
    
    df['load_time'] = pd.Timestamp.now()

    
    # Display the transformed DataFrame
    print("Transformed DataFrame sample:")
    print(df.head(24))
else:
    print(f"Error: Failed to retrieve data. Status code: {response.status_code}")

from sqlalchemy import create_engine
import os

# PostgreSQL connection details
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"  # If running locally
DB_PORT = "5432"       # Default PostgreSQL port
DB_NAME = "weather_db"

# Create a connection string
connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create a SQLAlchemy engine
engine = create_engine(connection_string)

# Define the table name
table_name = "weather_data"

try:
    # Load DataFrame to PostgreSQL
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"✅ Data successfully loaded to the '{table_name}' table in PostgreSQL!")
except Exception as e:
    print(f"❌ An error occurred: {e}")
