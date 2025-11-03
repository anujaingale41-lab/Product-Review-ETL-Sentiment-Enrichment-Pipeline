import pandas as pd
import logging
import argparse
import os

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Deduplicate based on product_id + description
    before = len(df)
    df = df.drop_duplicates(subset=["product_id", "description"])
    after = len(df)
    logging.info(f"Deduplicated {before - after} rows")

    # Reorder columns (adjust as needed)
    desired_order = [
        "product_id", "review_rating", "rating_label", "description",
        "review_length", "has_exclamation", "clean_text"
    ]
    df = df[[col for col in desired_order if col in df.columns]]

    # Format types
    if "review_rating" in df.columns:
        df["review_rating"] = df["review_rating"].round(1)
    if "has_exclamation" in df.columns:
        df["has_exclamation"] = df["has_exclamation"].astype(int)

    logging.info("Transformation complete: reordered columns, deduplicated, formatted types")
    return df

def main():
    setup_logger()
    parser = argparse.ArgumentParser(description="Transform enriched product review data")
    parser.add_argument("--input", required=True, help="Path to enriched input CSV")
    parser.add_argument("--output", required=False, help="Optional path to save final output")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        logging.error(f"Input file not found: {args.input}")
        return

    df = pd.read_csv(args.input, encoding='utf-8', low_memory=False)
    transformed_df = transform_data(df)

    if args.output:
        transformed_df.to_csv(args.output, index=False)
        logging.info(f"Final data saved to {args.output}")
    else:
        print(transformed_df.head())

if __name__ == "__main__":
    main()
