# 🌦️ Weather ETL Pipeline

An automated ETL pipeline that fetches real-time weather data 
for 5 Indian cities, transforms it with Pandas, and loads 
into PostgreSQL — orchestrated with Apache Airflow.

## 🏗️ Architecture
OpenWeatherMap API → Extract → Transform → Load → PostgreSQL

## 🛠️ Tech Stack
- Python, Pandas
- Apache Airflow (orchestration & scheduling)
- PostgreSQL (data storage)
- OpenWeatherMap API (data source)

##  Project Structure
weather-etl-pipeline/
├── dags/
│   └── weather_dag.py     # Airflow DAG - runs hourly
├── etl/
│   ├── extract.py         # Fetches weather from API
│   ├── transform.py       # Cleans data with Pandas
│   └── load.py            # Saves to PostgreSQL
├── sql/
│   └── create_tables.sql  # Database schema
├── requirements.txt
└── README.md

##  Setup
1. Clone repo
2. Create .env file with API_KEY and DB_URL
3. pip install -r requirements.txt
4. Start PostgreSQL and create weatherdb database
5. Run: airflow standalone

##  Sample Data
Cities tracked: Mumbai, Delhi, Bengaluru, Chennai, Kolkata
Data collected: temperature, humidity, wind speed, pressure
Schedule: Every hour automatically
