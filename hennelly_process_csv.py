"""
Process a CSV file on 2020 Happiness ratings by country to analyze the `Ladder score` column and save statistics.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics
import sys

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


def analyze_qb_par(file_path: pathlib.Path, column_hint: str = "PAR/Gm") -> dict:
    """Analyze a numeric PAR-like column (e.g., 'PAR/Gm', 'PAR/13') and return stats."""
    try:
        scores = []

        def norm(s: str) -> str:
            return ''.join(ch for ch in s.strip().lower() if ch.isalnum())

        with file_path.open('r', newline='', encoding='utf-8-sig') as f:
            r = csv.DictReader(f)
            headers = r.fieldnames or []
            # map normalized header -> original header
            colmap = {norm(h): h for h in headers}
            # try to find the column
            candidates = [norm(column_hint), "par", "qbpar", "pointsabovereplacement"]
            col = next((colmap[c] for c in candidates if c in colmap), None)

            if not col:
                logger.error(f"PAR column not found. Available columns: {headers}")
                return {}

            for row in r:
                raw = (row.get(col) or "").strip()
                if raw in ("", "NA", "N/A", "-"):
                    continue
                try:
                    scores.append(float(raw))
                except ValueError:
                    logger.warning(f"Skipping non-numeric value: {raw!r}")
                    continue

        if not scores:
            logger.error("No numeric values found in the PAR column.")
            return {}

        return {
            "min": min(scores),
            "max": max(scores),
            "mean": statistics.mean(scores),
            "median": statistics.median(scores),
            "stdev": statistics.stdev(scores) if len(scores) > 1 else 0.0,
        }

    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze QB PAR, and save the results."""
    input_file = pathlib.Path(FETCHED_DATA_DIR, "historical_QB_PAR_seasons.csv")
    output_file = pathlib.Path(PROCESSED_DIR, "qb_par_stats.txt")

    # run analysis once
    stats = analyze_qb_par(input_file)

    # ensure output dir exists
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # if analysis failed, write note and exit early
    if not stats:
        with output_file.open('w') as file:
            file.write("QB PAR Statistics:\n")
            file.write("No stats produced. Check column name in the CSV; see logs.\n")
        logger.error("Stats dict empty; likely wrong column name. See error above.")
        return

    # write real stats
    with output_file.open('w') as file:
        file.write("QB PAR Statistics:\n")
        file.write(f"Minimum: {stats['min']:.2f}\n")
        file.write(f"Maximum: {stats['max']:.2f}\n")
        file.write(f"Mean: {stats['mean']:.2f}\n")
        file.write(f"Median: {stats['median']:.2f}\n")
        file.write(f"Standard Deviation: {stats['stdev']:.2f}\n")

    # Log the processing of the CSV file
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")
