class PubMed():

    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_pmids(self, query):
        # Use esearch to get PMIDs
        esearch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={query}&retmode=json&api_key={self.api_key}"
        response = requests.get(esearch_url)
        return response.json()['esearchresult']['idlist']

    def fetch_abstracts(self, pmids):
        # Use efetch to get abstracts
        pmid_string = ','.join(pmids)
        efetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid_string}&retmode=text&rettype=abstract&api_key={self.api_key}"
        response = requests.get(efetch_url)
        return response.text