import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("DB_URL")

def load_weather(df):
    engine = create_engine(DB_URL)
    df.to_sql(
        "weather_data",
        engine,
        if_exists="append",   # keeps adding new rows each run
        index=False
    )
    print(f"Loaded {len(df)} rows into weather_data")