

# DataFun-03-Analytics

## Project Overview

This project is part of the Northwest Missouri State University Data Analytics Fundamentals course (Week 3). It demonstrates data fetching, processing, and analysis using Python. The project focuses on retrieving various data formats (CSV, Excel, JSON, Text), processing them, and generating summary statistics for sports and literature datasets.

## Directory Structure

- `hennelly_get_csv.py` — Fetches college football statistics (CSV) from the web and saves them locally.
- `hennelly_get_excel.py` — Fetches college football statistics (Excel) from the web and saves them locally.
- `hennelly_get_json.py` — Fetches soccer (football) match data (JSON) from the web and saves it locally.
- `hennelly_get_text.py` — Fetches the text of Moby Dick from the web and saves it locally.
- `hennelly_process_csv.py` — Processes the fetched CSV data and outputs QB PAR per game overall statistics.
- `hennelly_process_excel.py` — Processes the fetched Excel data and counts the number of occurrences of Cory Schrader.
- `hennelly_process_json.py` — Processes the fetched JSON data and counts the number of seasons per competition.
- `hennelly_process_text.py` — Processes the fetched text data and counts the number of occurrences of "Ahab".
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


### Recommended: Use the All-in-One Script

You can now use `hennelly_project3.py` to fetch and process all data files from a single menu-driven program:

```bash
python hennelly_project3.py
```

Follow the on-screen prompts to fetch, process, or do both for all data types.

---

### (Advanced) Run Individual Scripts

To fetch all data files (CSV, Excel, JSON, Text):

```bash
python hennelly_get_csv.py && python hennelly_get_excel.py && python hennelly_get_json.py && python hennelly_get_text.py
```

To process all data and generate statistics:

```bash
python hennelly_process_csv.py && python hennelly_process_excel.py && python hennelly_process_json.py && python hennelly_process_text.py
```

## Data Sources


- **CSV:** [College Football PAR Data](https://raw.githubusercontent.com/Neil-Paine-1/College-Football-QB-PAR/main/historical-QB-PAR-seasons.csv)
- **Excel:** [NCAA Data](https://raw.githubusercontent.com/Cap110100/College-Football-Analysis/main/All_stats.xlsx)
- **JSON:** [Soccer Data](https://raw.githubusercontent.com/statsbomb/open-data/refs/heads/master/data/competitions.json)
- **Text:** [Moby Dick](https://www.gutenberg.org/cache/epub/2701/pg2701.txt)

## Output

- Processed statistics and results are saved in the `hennelly_processed/` directory.
- Logs are written to `logs/project_log.log`.

## Notes

- Update file paths in scripts if you change directory names.
- All scripts use a shared logging utility for consistent output.

---
**Author:** Kevin Hennelly
**Course:** Data Analytics Fundamentals
