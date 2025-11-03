import argparse
import pandas as pd
import os
import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def load_data(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")

    ext = os.path.splitext(file_path)[1].lower()
    try:
        if ext == ".csv":
            df = pd.read_csv(file_path, encoding='utf-8', low_memory=False)
        elif ext == ".json":
            df = pd.read_json(file_path)
        else:
            logging.error(f"Unsupported file format: {ext}")
            raise ValueError(f"Unsupported file format: {ext}")
        logging.info(f"Loaded {len(df)} records from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        raise

def save_raw_copy(df: pd.DataFrame, output_path: str):
    try:
        df.to_csv(output_path, index=False)
        logging.info(f"Raw data saved to {output_path}")
    except Exception as e:
        logging.error(f"Failed to save raw copy: {e}")
        raise

def main():
    setup_logger()
    parser = argparse.ArgumentParser(description="Extract raw product review data")
    parser.add_argument("--input", required=True, help="Path to input file (.csv or .json)")
    parser.add_argument("--output", required=False, help="Optional path to save raw copy")
    args = parser.parse_args()

    df = load_data(args.input)

    if args.output:
        save_raw_copy(df, args.output)

if __name__ == "__main__":
    main()
