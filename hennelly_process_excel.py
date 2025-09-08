"""
Process an Excel file to count occurrences of a specific word in a column.

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import sys

# Import from external packages
import openpyxl

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

FETCHED_DATA_DIR: str = "data"
PROCESSED_DIR: str = "hennelly_processed"

#####################################
# Define Functions
#####################################

def count_cody_schrader(file_path: pathlib.Path, column_letter: str, word: str) -> int:
    """Count the occurrence of Cody Schrader."""
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        count = 0
        for cell in sheet[column_letter]:
            if cell.value and isinstance(cell.value, str):
                count += cell.value.lower().count(word.lower())
        return count
    except Exception as e:
        logger(f"Error reading Excel file: {e}")
        return 0

def process_excel_file():
    """Read an Excel file, count occurrences of Cody Schrader, and save the result."""
    
    input_file = pathlib.Path(FETCHED_DATA_DIR, "all_NCAA_data.xlsx")

    output_file = pathlib.Path(PROCESSED_DIR, "cody_schrader.txt")

    column_to_check = "D"  

    word_to_count = "Cody Schrader"

    # Call the function to count occurrences of the word in the specified column
    word_count = count_cody_schrader(input_file, column_to_check, word_to_count)
    
    # Write the results to the output file    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        file.write(f"Occurrences of '{word_to_count}' in column {column_to_check}: {word_count}\n")
    
    # Log the processing of the Excel file    
    logger.info(f"Processed Excel file: {input_file}, Word count saved to: {output_file}")

###########################################################################
# Process and display some info about the Excel DataFrame
###########################################################################

def process_excel_data(df):
    """Process and display some info about the Excel DataFrame."""
    print("Excel Data preview:")
    print(df.head())
    print(f"Shape: {df.shape}")
    
#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    process_excel_file()
    logger.info("Excel processing complete.")
