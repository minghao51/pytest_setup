# Purpose

The `data/` folder is dedicated to managing all data related to this project. It is intended to keep data files organized and separate from code, facilitating data versioning and clarity.

For some projects, the data would instead be saved on cloud storage, 

# Typical Contents:
This is just one of the suggestion, medallion data architecture would also work. 
*   **`raw/`**:  Stores the original, unprocessed data sources. These files should ideally be read-only and reflect the data exactly as it was received.
    *   Examples: CSV files, JSON files, database dumps, image datasets, etc.
    *   **Do not modify files in `raw/` directly after initial ingestion.**
*   **`interim/`**:  Holds intermediate datasets that have been processed but are not yet in their final "processed" form. This can include data after initial cleaning, feature engineering steps, or transformations that are part of a multi-stage data pipeline.
    *   Examples: Feather files, Parquet files, cleaned CSVs, etc.
*   **`processed/`**:  Contains the final, processed datasets that are ready for model training or analysis. Data in this folder should be in a consistent and well-defined format.
    *   Examples: Feature matrices, training/testing splits, optimized data formats for specific models, etc.
*   **`external/`**: Stores data obtained from external sources that are not part of the project's primary data ingestion process.
    *   Examples: Pre-trained models, lookup tables, geographical data, etc.


# Usage Guidelines:

*   Treat `raw/` data as immutable after initial ingestion.
*   Data processing scripts (likely found outside the `data/` folder, perhaps in `src/` or `notebooks/`) should read from `raw/` and write to `interim/` or `processed/`.
*   Clearly document the data transformation pipelines and the purpose of each data folder.