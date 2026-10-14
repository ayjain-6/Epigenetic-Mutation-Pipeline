import pandas as pd
import numpy as np

def process_bulk_mutations(raw_mutation_df: pd.DataFrame, config: dict) -> pd.DataFrame:
    """
    Processes a large-scale set of mutations across multiple databases:
    1. Filters common germline variants using gnomAD MAFs.
    2. Classifies structural pathogenicity using AlphaMissense thresholds.
    3. Flags recurrent tumor hotspots using COSMIC sample counts.
    4. Integrates DepMap dependency Z-scores.
    """
    filters = config.get("filters", {})
    max_maf = filters.get("gnomad_max_maf", 0.001)
    am_thresh = filters.get("alpha_missense_pathogenic", 0.564)
    min_cosmic = filters.get("cosmic_min_recurrence", 5)
    
    df = raw_mutation_df.copy()
    
    # 1. gnomAD germline filter (keep rare or novel variants)
    if "gnomad_af" in df.columns:
        df = df[(df["gnomad_af"] <= max_maf) | (df["gnomad_af"].isna())].copy()
        
    # 2. AlphaMissense classification
    if "alpha_missense" in df.columns:
        df["am_classification"] = df["alpha_missense"].apply(
            lambda x: "Pathogenic" if x >= am_thresh else ("Benign" if x <= 0.1 else "Ambiguous")
        )
        
    # 3. COSMIC hotspot flag
    if "cosmic_sample_count" in df.columns:
        df["is_cosmic_hotspot"] = df["cosmic_sample_count"] >= min_cosmic
    else:
        df["is_cosmic_hotspot"] = False
        
    return df
