# Automated ETL Pipeline

A data engineering pipeline that automatically extracts, transforms and loads real AQI data using Python — with full logging at every step.

---

## Overview

ETL — Extract, Transform, Load — is the backbone of every data-driven company in the world. Netflix, Amazon, Google — all of them run pipelines like this to move and clean data automatically.

This project builds one from scratch using real Indian AQI data, demonstrating how raw messy data gets cleaned and stored reliably without manual intervention.

Built as part of an ongoing data science learning journey.

---

## Pipeline Results

| Stage | Details |
|-------|---------|
| Extracted | 29,531 rows from city_day.csv |
| Duplicates removed | 0 |
| Missing rows removed | 23,295 |
| Clean rows loaded | 6,236 |
| Output | pipeline.db — aqi_clean table |

---

## How the Pipeline Works

```
Extract → Transform → Load
```

**Extract**
Reads raw AQI data from a CSV file containing 29,531 daily city readings.

**Transform**
Removes duplicate records, drops rows with missing values, and adds a processing timestamp to every row.

**Load**
Saves the cleaned data into a SQLite database table called `aqi_clean`.

**Logging**
Every step is logged with a timestamp — both to the terminal and to a `pipeline.log` file for debugging.

---

## Sample Log Output

```
2026-03-30 00:36:14 - INFO - PIPELINE STARTED
2026-03-30 00:36:14 - INFO - EXTRACT — Loaded 29531 rows
2026-03-30 00:36:14 - INFO - TRANSFORM — Removed 23295 missing rows
2026-03-30 00:36:14 - INFO - TRANSFORM — Done! 6236 clean rows ready
2026-03-30 00:36:14 - INFO - LOAD — Saved 6236 rows to aqi_clean
2026-03-30 00:36:14 - INFO - PIPELINE COMPLETED SUCCESSFULLY
```

---

## How to Run

```bash
# Clone the repository
git clone https://github.com/Paddu2006/etl-pipeline.git
cd etl-pipeline

# Install dependencies
pip install pandas

# Update the filepath in pipeline.py to point to your CSV file
# Run the pipeline
python pipeline.py
```

---

## Project Structure

```
etl_pipeline/
│
├── pipeline.py     # Main ETL script
├── pipeline.db     # Output SQLite database
├── pipeline.log    # Execution log
└── README.md
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.13 | Core language |
| Pandas | Data extraction and transformation |
| SQLite3 | Data loading and storage |
| Logging | Pipeline monitoring |

---

## What I Learned Building This

- How ETL pipelines work in real data engineering environments
- How to use Python's logging module to monitor pipeline execution
- How to modularise code into extract, transform and load functions
- Why pipelines matter — manual data cleaning does not scale

---

## Part of a Larger Journey

This is Project 5 of an ongoing series of data science projects.

Project 1 — AQI India Analyser: https://github.com/Paddu2006/aqi-india-analyser
Project 2 — Crop Yield Explorer: https://github.com/Paddu2006/crop-yield-explorer
Project 3 — Personal Finance Tracker: https://github.com/Paddu2006/personal-finance-tracker
Project 4 — Hospital Patient Records: https://github.com/Paddu2006/hospital-patient-records

---

## License

MIT License — free to use, share, and build upon.
