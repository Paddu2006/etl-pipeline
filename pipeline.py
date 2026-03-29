# Automated ETL Pipeline
# By Padma Shree
# Project 5 of 25

import pandas as pd
import sqlite3
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)

log = logging.getLogger()

def extract(filepath):
    log.info("EXTRACT — Reading data from " + filepath)
    df = pd.read_csv(filepath)
    log.info("EXTRACT — Loaded " + str(len(df)) + " rows")
    return df

def transform(df):
    log.info("TRANSFORM — Starting data cleaning")
    before = len(df)
    df = df.drop_duplicates()
    log.info("TRANSFORM — Removed " + str(before - len(df)) + " duplicates")
    before = len(df)
    df = df.dropna()
    log.info("TRANSFORM — Removed " + str(before - len(df)) + " missing rows")
    df["processed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log.info("TRANSFORM — Done! " + str(len(df)) + " clean rows ready")
    return df

def load(df, db_name, table_name):
    log.info("LOAD — Saving to database " + db_name)
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    log.info("LOAD — Saved " + str(len(df)) + " rows to " + table_name)

def run_pipeline():
    log.info("=" * 50)
    log.info("PIPELINE STARTED")
    log.info("=" * 50)
    filepath = r"C:\Users\Padma shree jena\Desktop\PadduDS_Journey\05_resources\datasets\city_day.csv"
    df = extract(filepath)
    df = transform(df)
    load(df, "pipeline.db", "aqi_clean")
    log.info("=" * 50)
    log.info("PIPELINE COMPLETED SUCCESSFULLY")
    log.info("=" * 50)

run_pipeline()