import pandas as pd
import logging
import argparse
import os

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def save_data(df: pd.DataFrame, output_path: str, format: str = "csv"):
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
        logging.info(f"Data saved to {output_path} as {format.upper()}")
    except Exception as e:
        logging.error(f"Failed to save data: {e}")

def main():
    setup_logger()
    parser = argparse.ArgumentParser(description="Save final product review data")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument("--output", required=True, help="Path to save output file")
    parser.add_argument("--format", default="csv", choices=["csv", "parquet", "json"], help="Output format")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        logging.error(f"Input file not found: {args.input}")
        return

    df = pd.read_csv(args.input, encoding='utf-8', low_memory=False)
    save_data(df, args.output, args.format)

if __name__ == "__main__":
    main()
