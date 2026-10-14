import os
import yaml
import pandas as pd
from snapshot_loader import SnapshotDataLoader

def run_integration_pipeline():
    os.makedirs("results", exist_ok=True)
    os.makedirs("figures", exist_ok=True)
    
    # 1. Load config parameters
    config_path = os.path.join("config", "cohort_params.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
        
    target_genes = config.get("genes", ["H3F3A", "ATRX", "DAXX"])
    max_maf = config.get("filters", {}).get("gnomad_max_maf", 0.001)
    
    # 2. Ingest from local snapshot data warehouse
    loader = SnapshotDataLoader(data_dir="data/raw")
    raw_df = loader.load_gene_mutations(target_genes)
    
    # 3. Apply enterprise multi-database filters (e.g., gnomAD MAF threshold)
    filtered_df = raw_df[(raw_df["gnomAD_AF"] <= max_maf) | (raw_df["gnomAD_AF"].isna())].copy()
    
    # 4. Save reproducible summary artifact
    csv_path = os.path.join("results", "cross_db_summary.csv")
    filtered_df.to_csv(csv_path, index=False)
    print(f"✅ Successfully processed snapshot and generated {len(filtered_df)} variants at results/cross_db_summary.csv!")

if __name__ == "__main__":
    run_integration_pipeline()
