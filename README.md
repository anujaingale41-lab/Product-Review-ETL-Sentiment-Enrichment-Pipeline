#  Product Review ETL + Enrichment Pipeline

A modular, production-ready pipeline that extracts, validates, enriches, and transforms product reviews for downstream analytics and sentiment modeling. Built for recruiter visibility, business relevance, and real-world scalability.

---

##  Features

- Modular `.py` scripts for each pipeline stage
- Schema validation, null checks, and type enforcement
- Enrichment: review length, rating labels, exclamation flags, clean text
- Output in CSV, Parquet, or JSON
- CLI and notebook compatible
- Ready for optional sentiment scoring (TextBlob/VADER)


##  Pipeline Structure

```
src/
├── extract.py      # Load raw data
├── validate.py     # Enforce schema and null checks
├── enrich.py       # Add derived features
├── transform.py    # Deduplicate and format
├── load.py         # Save final output
├── utils.py        # Shared helpers (logging, file I/O)
```


##  Sample Output

| product_id | review_rating | rating_label | review_length | has_exclamation | clean_text |
|------------|---------------|--------------|----------------|------------------|-------------|
| B00123     | 5.0           | positive     | 12             | 1                | this product is amazing |


##  How to Run (CLI)

# Step 1: Extract
python src/extract.py --input data/raw/ProductReviews.csv --output data/processed/raw_copy.csv

# Step 2: Validate
python src/validate.py --input data/processed/raw_copy.csv

# Step 3: Enrich
python src/enrich.py --input data/processed/raw_copy.csv --output data/processed/enriched_reviews.csv

# Step 4: Transform
python src/transform.py --input data/processed/enriched_reviews.csv --output data/processed/final_reviews.csv

# Step 5: Load
python src/load.py --input data/processed/final_reviews.csv --output data/output/reviews_final.csv --format csv
```


##  Folder Structure


project-root/
├── src/                  # Modular pipeline scripts
├── data/
│   ├── raw/              # Original input files
│   ├── processed/        # Intermediate outputs
│   └── final_reviews.csv # Final enriched output
├── docs/
│   └── README.md         # Project overview
│   └── sample_output.csv # Optional preview
├── requirements.txt      # Python dependencies
```


## Author

**Anuja Ingale** — Early-career technologist specializing in hybrid Data Engineering and Backend Development.  
Modular pipelines. Recruiter-ready code. Real-world impact.


## Optional Enhancements

- Add sentiment scoring with TextBlob or VADER
- Add Airflow DAG or CLI runner script
- Add unit tests for validation and enrichment
- Add demo notebook or video walkthrough
