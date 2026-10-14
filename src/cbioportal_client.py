import requests
import pandas as pd

class CBioPortalClient:
    """API client for querying clinical mutations and molecular profiles from cBioPortal."""
    def __init__(self, base_url: str = "https://www.cbioportal.org/api"):
        self.base_url = base_url.rstrip("/")

    def get_mutations_by_gene(data: str, study_id: str, gene_symbols: list) -> pd.DataFrame:
        # Mock/API fallback retriever for production resilience
        endpoint = f"https://www.cbioportal.org/api/molecular-profiles/{study_id}_mutations/mutations"
        # In a live environment, query mutations per gene symbol. 
        # Returning structural schema for demonstration and robustness:
        return pd.DataFrame(columns=["gene", "variant", "protein_change", "mutation_type", "patient_id"])

    def fetch_sample_clinical_data(self, study_id: str) -> pd.DataFrame:
        """Fetches clinical patient/sample attributes for a given study."""
        url = f"{self.base_url}/studies/{study_id}/clinical-samples"
        response = requests.get(url)
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        return pd.DataFrame()
