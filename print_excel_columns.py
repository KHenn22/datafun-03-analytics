import pandas as pd

# Path to your Excel file
excel_path = 'data/all_NCAA_data.xlsx'

def print_column_letters_and_names(excel_path):
    df = pd.read_excel(excel_path, engine='openpyxl')
    print("Column Letter | Column Name")
    print("--------------------------")
    for idx, col in enumerate(df.columns):
        # Convert index to Excel column letter
        col_letter = chr(65 + idx) if idx < 26 else chr(65 + (idx // 26) - 1) + chr(65 + (idx % 26))
        print(f"{col_letter:>12} | {col}")

if __name__ == "__main__":
    print_column_letters_and_names(excel_path)
