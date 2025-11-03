import pandas as pd
import logging
import os

def setup_logger(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def load_file(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")

    ext = os.path.splitext(file_path)[1].lower()
    try:
        if ext == ".csv":
            df = pd.read_csv(file_path, encoding='utf-8', low_memory=False)
        elif ext == ".json":
            df = pd.read_json(file_path)
        elif ext == ".parquet":
            df = pd.read_parquet(file_path)
        else:
            logging.error(f"Unsupported file format: {ext}")
            raise ValueError(f"Unsupported file format: {ext}")
        logging.info(f"Loaded {len(df)} records from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        raise

def save_file(df: pd.DataFrame, output_path: str, format: str = "csv"):
    format = format.lower()
    try:
        if format == "csv":
            df.to_csv(output_path, index=False)
        elif format == "parquet":
            df.to_parquet(output_path, index=False)
        elif format == "json":
            df.to_json(output_path, orient="records", lines=True)
        else:
            logging.error(f"Unsupported format: {format}")
            return
        logging.info(f"Saved data to {output_path} as {format.upper()}")
    except Exception as e:
        logging.error(f"Failed to save data: {e}")
        raise
