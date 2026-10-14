import pandas as pd

class OncologyDatabaseClient:
    """Mock/API client for querying COSMIC recurrence and ClinVar clinical assertions."""
    
    def annotate_cosmic_hotspots(self, df: pd.DataFrame, min_recurrence: int = 5) -> pd.DataFrame:
        """Flags variants as recurrent tumor hotspots based on COSMIC tumor occurrence counts."""
        if "cosmic_sample_count" in df.columns:
            df["is_cosmic_hotspot"] = df["cosmic_sample_count"] >= min_recurrence
        else:
            df["is_cosmic_hotspot"] = False
        return df

    def integrate_clinvar_assertions(self, df: pd.DataFrame) -> pd.DataFrame:
        """Integrates ClinVar clinical significance classifications."""
        if "clinvar_significance" not in df.columns:
            df["clinvar_significance"] = "Unclassified"
        return df
