import pandas as pd

def filter_common_germline(variant_df: pd.DataFrame, max_maf: float = 0.001) -> pd.DataFrame:
    """
    Filters out common germline polymorphisms using gnomAD population allele frequencies 
    to isolate rare somatic mutations or high-penetrance rare germline variants.
    """
    if "gnomad_af" in variant_df.columns:
        # Retain variants below threshold or where AF is missing (novel somatic mutations)
        filtered = variant_df[(variant_df["gnomad_af"] <= max_maf) | (variant_df["gnomad_af"].isna())].copy()
        return filtered
    return variant_df
