"""
hennelly_project3.py
Runs all four data analytics demos (CSV, Excel, JSON, Text) as required for Project 3.
"""

# ---- Imports ----
from hennelly_get_csv import get_csv_data
from hennelly_get_excel import get_excel_data
from hennelly_get_json import get_json_data
from hennelly_get_text import get_text_data

from hennelly_process_csv import process_csv_data
from hennelly_process_excel import process_excel_data
from hennelly_process_json import process_json_data
from hennelly_process_text import process_text_data


# Main function
def main():
    print("=== Project 3: Data Analytics ===")

    # CSV demo
    print("\n--- CSV Demo ---")
    csv_path = "data/historical_QB_PAR_seasons.csv"
    csv_data = get_csv_data(csv_path)
    process_csv_data(csv_data)

    # Excel demo
    print("\n--- Excel Demo ---")
    excel_path = "data/all_NCAA_data.xlsx"
    excel_data = get_excel_data(excel_path)
    process_excel_data(excel_data)

    # JSON demo
    print("\n--- JSON Demo ---")
    json_path = "data/matches.json"
    json_data = get_json_data(json_path)
    process_json_data(json_data)

    # Text demo
    print("\n--- Text Demo ---")
    text_path = "data/ahab.txt"
    text_data = get_text_data(text_path)
    process_text_data(text_data)


# Run if called directly
if __name__ == "__main__":
    main()
