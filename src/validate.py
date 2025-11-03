import argparse
import pandas as pd
import logging
import sys

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def validate_schema(df: pd.DataFrame, required_columns: dict) -> bool:
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        logging.error(f"Missing required columns: {missing_cols}")
        return False

    type_mismatches = []
    for col, expected_type in required_columns.items():
        if not pd.api.types.is_dtype_equal(df[col].dtype, expected_type):
            type_mismatches.append((col, str(df[col].dtype), str(expected_type)))

    if type_mismatches:
        for col, actual, expected in type_mismatches:
            logging.warning(f"Column '{col}' has type {actual}, expected {expected}")
        return False

    logging.info("Schema validation passed.")
    return True

def check_nulls(df: pd.DataFrame, critical_columns: list) -> bool:
    null_report = df[critical_columns].isnull().sum()
    nulls_found = null_report[null_report > 0]

    if not nulls_found.empty:
        logging.warning(f"Null values found:\n{nulls_found}")
        return False

    logging.info("No nulls found in critical columns.")
    return True

def main():
    setup_logger()
    parser = argparse.ArgumentParser(description="Validate product review dataset")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    args = parser.parse_args()

    try:
        df = pd.read_csv(args.input, encoding='utf-8', low_memory=False)
    except Exception as e:
        logging.error(f"Failed to read input file: {e}")
        sys.exit(1)

    # Define expected schema (adjust types as needed)
    required_columns = {
        "review_text": "object",
        "rating": "float64",  # or "int64" depending on your dataset
        "product_id": "object"
    }

    critical_columns = ["review_text", "rating"]

    schema_ok = validate_schema(df, required_columns)
    nulls_ok = check_nulls(df, critical_columns)

    if schema_ok and nulls_ok:
        logging.info("Validation successful ✅")
    else:
        logging.warning("Validation failed ❌")

if __name__ == "__main__":
    main()
