import pandas as pd
from datetime import datetime

def transform_weather(raw_data):
    records = []
    for item in raw_data:
        records.append({
            "city":        item["name"],
            "country":     item["sys"]["country"],
            "temperature": item["main"]["temp"],
            "feels_like":  item["main"]["feels_like"],
            "humidity":    item["main"]["humidity"],
            "pressure":    item["main"]["pressure"],
            "weather":     item["weather"][0]["description"],
            "wind_speed":  item["wind"]["speed"],
            "fetched_at":  datetime.utcnow()
        })
    df = pd.DataFrame(records)
    # Remove duplicates just in case
    df.drop_duplicates(subset=["city", "fetched_at"], inplace=True)
    return df