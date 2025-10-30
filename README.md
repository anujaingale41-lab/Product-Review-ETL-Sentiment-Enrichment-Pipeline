# Product-Review-ETL-Sentiment-Enrichment-Pipeline
A modular ETL pipeline that ingests product reviews, validates structure and rating logic, cleans and transforms text, and enriches each review with sentiment scores and labels using NLP. Designed for scalable analytics, ML readiness, and optional REST API integration for review sentiment lookup.


Designed to demonstrate hybrid **Data Engineering + Backend Validation** skills with production-ready structure, CLI support, and optional REST API integration.


## Pipeline Modules

### 1. **Extract**
- Reads product reviews from CSV, JSON, or simulated API
- Enforces schema and logs ingestion stats

### 2. **Validate**
- Checks for:
  - Nulls in critical fields (`review_id`, `product_id`, `review_text`, `rating`)
  - Rating ∈ [1, 5]
  - Valid product ID format

### 3. **Transform**
- Cleans review text (lowercase, punctuation removal, stopword filtering)
- Tokenizes and extracts keywords
- Converts timestamp to `day`, `month`, `hour` (if available)

### 4. **Enrich**
- Adds:
  - Sentiment score using TextBlob or Vader
  - Sentiment label (`Positive`, `Neutral`, `Negative`)
  - Keyword frequency or tag cloud (optional)

### 5. **Load**
- Saves enriched reviews to Parquet or Delta Lake
- Partitioned by sentiment label or product category
- Includes deduplication and schema evolution


## Features
- ✅ Modular CLI-enabled Python scripts
- 🧪 Unit tests for validation logic
- 🔁 Optional Airflow DAG for orchestration
- 🌐 Optional REST API for querying sentiment by product ID
- 📊 Sample output previews for recruiter visibility


## How to Run
```bash
# Step-by-step CLI execution
python src/extract.py --input data/sample_reviews.csv
python src/validate.py --input data/raw_reviews.json
python src/transform.py --input data/validated.json
python src/enrich.py --input data/transformed.json
python src/load.py --input data/enriched.json
```


Sample Output Preview
| review_id | product_id | rating | sentiment_score | sentiment_label |
|-----------|------------|--------|------------------|------------------|
| R001      | P123       | 5      | 0.85             | Positive         |
| R002      | P456       | 2      | -0.40            | Negative         |
