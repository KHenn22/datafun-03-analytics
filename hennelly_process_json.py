"""
Process a JSON file to count number of seasons per soccer competition.

JSON file is in the format where people is a list of dictionaries with keys "craft" and "name".

{
    "people": [
        {
            "craft": "ISS",
            "name": "Oleg Kononenko"
        },
        {
            "craft": "ISS",
            "name": "Nikolai Chub"
        }
    ],
    "number": 2,
    "message": "success"
}

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
import pathlib
import sys
from pathlib import Path

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


def count_competitions(file_path: pathlib.Path) -> dict[str, int]:
    """
    Count how many soccer seasons exist per competition_name
    from StatsBomb competitions.json (saved locally as matches.json).
    """
    with file_path.open("r", encoding="utf-8") as f:
        competitions = json.load(f)

    counts: dict[str, int] = {}
    for comp in competitions:
        name = comp.get("competition_name", "Unknown")
        counts[name] = counts.get(name, 0) + 1

    # sort: most seasons first, then alphabetically
    return dict(sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))


def process_json_file() -> None:
    """Read competitions.json (saved as matches.json), tally, and save results."""
    input_file = pathlib.Path("data") / "matches.json"   # your file
    output_file = Path(PROCESSED_DIR) / "json_seasons_per_competition.txt"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    counts = count_competitions(input_file)

    with output_file.open("w", encoding="utf-8") as f:
        f.write("Seasons per competition:\n")
        for league, n in counts.items():
            f.write(f"{league}: {n}\n")

    print(f"[INPUT_FILE]  {input_file}")
    print(f"[OUTPUT_FILE] {output_file}")
    
    # Log the processing of the JSON file
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

###############################################################
# Process and display some info about the JSON object
###############################################################

def process_json_data(obj):
    print("JSON Data preview:")
    if isinstance(obj, dict):
        print("Top-level keys:", list(obj.keys())[:5])
    elif isinstance(obj, list):
        print("First element:", obj[0])
    print(f"Type: {type(obj)}")
    
#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")
