import pandas as pd
import logging
import re
import argparse
import os

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def enrich_reviews(df: pd.DataFrame) -> pd.DataFrame:
    # Add review length (in words)
    df["review_length"] = df["description"].astype(str).apply(lambda x: len(x.split()))

    # Categorize rating
    def label_rating(r):
        if r >= 4:
            return "positive"
        elif r == 3:
            return "neutral"
        else:
            return "negative"
    df["rating_label"] = df["review_rating"].apply(label_rating)

    # Flag exclamation marks
    df["has_exclamation"] = df["description"].astype(str).str.contains("!", regex=False)

    # Clean text for sentiment analysis
    def clean_text(text):
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text
    df["clean_text"] = df["description"].astype(str).apply(clean_text)

    logging.info("Enrichment complete: added review_length, rating_label, has_exclamation, clean_text")
    return df

def main():
    setup_logger()
    parser = argparse.ArgumentParser(description="Enrich product reviews with derived features")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument("--output", required=False, help="Path to save enriched CSV file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        logging.error(f"Input file not found: {args.input}")
        return

    df = pd.read_csv(args.input, encoding='utf-8', low_memory=False)
    enriched_df = enrich_reviews(df)

    if args.output:
        enriched_df.to_csv(args.output, index=False)
        logging.info(f"Enriched data saved to {args.output}")
    else:
        print(enriched_df.head())

if __name__ == "__main__":
    main()
