"""
Combined Data Fetching and Processing Script
Author: Kevin Hennelly
"""

import pathlib
import sys
import csv
import statistics
import json
import requests
import openpyxl
from utils_logger import logger

# Directories
FETCHED_DATA_DIR = "data"
PROCESSED_DIR = "hennelly_processed"

# ========== FETCH FUNCTIONS ==========

def fetch_csv_file():
    url = "https://raw.githubusercontent.com/Neil-Paine-1/College-Football-QB-PAR/main/historical-QB-PAR-seasons.csv"
    filename = "historical_QB_PAR_seasons.csv"
    file_path = pathlib.Path(FETCHED_DATA_DIR, filename)
    logger.info(f"Fetching CSV from {url}")
    response = requests.get(url)
    response.raise_for_status()
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w') as f:
        f.write(response.text)
    logger.info(f"Saved CSV to {file_path}")

def fetch_excel_file():
    url = "https://raw.githubusercontent.com/Cap110100/College-Football-Analysis/main/All_stats.xlsx"
    filename = "all_NCAA_data.xlsx"
    file_path = pathlib.Path(FETCHED_DATA_DIR, filename)
    logger.info(f"Fetching Excel from {url}")
    response = requests.get(url)
    response.raise_for_status()
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('wb') as f:
        f.write(response.content)
    logger.info(f"Saved Excel to {file_path}")

def fetch_json_file():
    url = "https://raw.githubusercontent.com/statsbomb/open-data/refs/heads/master/data/competitions.json"
    filename = "matches.json"
    file_path = pathlib.Path(FETCHED_DATA_DIR, filename)
    logger.info(f"Fetching JSON from {url}")
    response = requests.get(url)
    response.raise_for_status()
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w') as f:
        json.dump(response.json(), f, indent=4)
    logger.info(f"Saved JSON to {file_path}")

def fetch_txt_file():
    url = "https://www.gutenberg.org/cache/epub/2701/pg2701.txt"
    filename = "ahab.txt"
    file_path = pathlib.Path(FETCHED_DATA_DIR, filename)
    logger.info(f"Fetching text from {url}")
    response = requests.get(url)
    response.raise_for_status()
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w') as f:
        f.write(response.text)
    logger.info(f"Saved text to {file_path}")

# ========== PROCESS FUNCTIONS ==========

def analyze_qb_par():
    input_file = pathlib.Path(FETCHED_DATA_DIR, "historical_QB_PAR_seasons.csv")
    output_file = pathlib.Path(PROCESSED_DIR, "qb_par_stats.txt")
    try:
        with input_file.open('r', newline='', encoding='utf-8-sig') as f:
            r = csv.DictReader(f)
            def is_number(val):
                try:
                    float(val)
                    return True
                except Exception:
                    return False
            scores = [float(row['PAR/Gm']) for row in r if row.get('PAR/Gm') and is_number(row['PAR/Gm'])]
        stats = {
            "min": min(scores),
            "max": max(scores),
            "mean": statistics.mean(scores),
            "median": statistics.median(scores),
            "stdev": statistics.stdev(scores) if len(scores) > 1 else 0.0,
        }
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with output_file.open('w') as file:
            file.write("QB PAR Statistics:\n")
            file.write(f"Minimum: {stats['min']:.2f}\n")
            file.write(f"Maximum: {stats['max']:.2f}\n")
            file.write(f"Mean: {stats['mean']:.2f}\n")
            file.write(f"Median: {stats['median']:.2f}\n")
            file.write(f"Standard Deviation: {stats['stdev']:.2f}\n")
        logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")
    except Exception as e:
        logger.error(f"Error processing CSV: {e}")

def process_excel_file():
    input_file = pathlib.Path(FETCHED_DATA_DIR, "all_NCAA_data.xlsx")
    output_file = pathlib.Path(PROCESSED_DIR, "cody_schrader.txt")
    column_to_check = "D"
    word_to_count = "Cody Schrader"
    try:
        workbook = openpyxl.load_workbook(input_file)
        sheet = workbook.active
        count = 0
        for cell in sheet[column_to_check]:
            if cell.value and isinstance(cell.value, str):
                count += cell.value.lower().count(word_to_count.lower())
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with output_file.open('w') as file:
            file.write(f"Occurrences of '{word_to_count}' in column {column_to_check}: {count}\n")
        logger.info(f"Processed Excel file: {input_file}, Word count saved to: {output_file}")
    except Exception as e:
        logger.error(f"Error processing Excel: {e}")

def process_json_file():
    input_file = pathlib.Path(FETCHED_DATA_DIR, "matches.json")
    output_file = pathlib.Path(PROCESSED_DIR, "json_seasons_per_competition.txt")
    try:
        with input_file.open("r", encoding="utf-8") as f:
            competitions = json.load(f)
        counts = {}
        for comp in competitions:
            name = comp.get("competition_name", "Unknown")
            counts[name] = counts.get(name, 0) + 1
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with output_file.open("w", encoding="utf-8") as f:
            f.write("Seasons per competition:\n")
            for league, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
                f.write(f"{league}: {n}\n")
        logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")
    except Exception as e:
        logger.error(f"Error processing JSON: {e}")

def process_text_file():
    input_file = pathlib.Path(FETCHED_DATA_DIR, "ahab.txt")
    output_file = pathlib.Path(PROCESSED_DIR, "text_ahab_word_count.txt")
    word_to_count = "Ahab"
    try:
        with input_file.open('r') as file:
            content = file.read()
            word_count = content.lower().count(word_to_count.lower())
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with output_file.open('w') as file:
            file.write(f"Occurrences of '{word_to_count}': {word_count}\n")
        logger.info(f"Processed text file: {input_file}, Word count saved to: {output_file}")
    except Exception as e:
        logger.error(f"Error processing text: {e}")

# ========== MAIN ========== 

def main():
    print("\n--- DataFun-03-Analytics: Project 3 Combined Script ---\n")
    print("1. Fetch all data files")
    print("2. Process all data files")
    print("3. Fetch AND process all data files")
    print("4. Exit\n")
    choice = input("Select an option (1-4): ").strip()
    if choice == "1":
        fetch_csv_file()
        fetch_excel_file()
        fetch_json_file()
        fetch_txt_file()
        print("\nAll data files fetched.\n")
    elif choice == "2":
        analyze_qb_par()
        process_excel_file()
        process_json_file()
        process_text_file()
        print("\nAll data files processed.\n")
    elif choice == "3":
        fetch_csv_file()
        fetch_excel_file()
        fetch_json_file()
        fetch_txt_file()
        analyze_qb_par()
        process_excel_file()
        process_json_file()
        process_text_file()
        print("\nAll data files fetched and processed.\n")
    else:
        print("Exiting.")

if __name__ == "__main__":
    main()

