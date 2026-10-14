import numpy as np
import pandas as pd

def annotate_alphamissense(variant_df: pd.DataFrame, threshold: float = 0.564) -> pd.DataFrame:
    """
    Annotates missense variants with AlphaMissense pathogenicity predictions.
    Scores > 0.564 are typically classified as likely pathogenic.
    """
    if "am_pathogenicity" in variant_df.columns:
        variant_df["am_class"] = variant_df["am_pathogenicity"].apply(
            lambda x: "Pathogenic" if x >= threshold else ("Benign" if x <= 0.1 else "Ambiguous")
        )
    return variant_df

def compute_dependency_zscore(depmap_matrix: pd.DataFrame, target_gene: str) -> pd.Series:
    """
    Calculates CRISPR gene effect Z-scores to identify selective dependencies 
    in chromatin-mutant cell lines vs wild-type.
    """
    if target_gene in depmap_matrix.columns:
        col = depmap_matrix[target_gene]
        z_scores = (col - col.mean()) / col.std()
        return z_scores
    return pd.Series(dtype=float)
