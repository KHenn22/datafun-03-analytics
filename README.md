
# DataFun-03-Analytics

## Project Overview

This project is part of the Northwest Missouri State University Data Analytics Fundamentals course (Week 3). It demonstrates data fetching, processing, and analysis using Python. The project focuses on retrieving various data formats (CSV, Excel, JSON, Text), processing them, and generating summary statistics.

## Directory Structure

- `hennelly_get_csv.py` — Fetches CSV data of college football statistics from the web and saves it locally.
- `hennelly_get_excel.py` — Fetches Excel data of college football statistics from the web and saves it locally.
- `hennelly_get_json.py` — Fetches JSON data on soccer (football) matches from the web and saves it locally.
- `hennelly_get_text.py` — Fetches text data from the web and saves it locally.
- `hennelly_process_csv.py` — Processes the fetched CSV data and outputs QB PAR per game overall statistics.
- `hennelly_process_excel.py` - Processes the fetched Excel data and counts the number of occurrences of Cory Schrader.
- `hennelly_process_json.py` - Processes the fetched JSON data and counts the number of seasons per competition.
- `utils_logger.py` — Logging utility used across scripts.
- `hennelly_data/` — Directory for raw fetched data files.
- `hennelly_processed/` — Directory for processed output files.
- `logs/` — Contains log files for script execution.

## Setup

1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure you have Python 3.10 or later installed.

## Usage

To fetch all data files (CSV, Excel, JSON, Text):

```bash
python hennelly_get_csv.py && python hennelly_get_excel.py && python hennelly_get_json.py && python hennelly_get_text.py
```

To process the CSV data and generate statistics:

```bash
python hennelly_process_csv.py
```

## Data Sources

- **CSV:** [College Football PAR Data] https://raw.githubusercontent.com/Neil-Paine-1/College-Football-QB-PAR/main/historical-QB-PAR-seasons.csv
  - Saved as `data/historical_QB_PAR_seasons.csv`

## Logs

- Logs are written to `logs/project_log.log`.

## Notes

- Update file paths in scripts if you change directory names.
- All scripts use a shared logging utility for consistent output.

---
**Author:** Kevin Hennelly
**Course:** Data Analytics Fundamentals
