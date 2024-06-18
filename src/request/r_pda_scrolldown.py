import re
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

class PaoDeAcucarScraper:
    def __init__(self):
        self.http = self._configure_session()
        self.origin = 'https://www.paodeacucar.com'
        self.products = []
        self.api_key = 'paodeacucar'
        self.content = None

    def start(self, keyword: str, page: int = None, results_per_page: int = None):
        self.page = page or 1
        self.results_per_page = results_per_page or 12
        self.search_products(keyword)
        total_pages = self.get_total_pages()
        for i in range(2, total_pages):
            self.page= i
            self.products = [*self.products, *self.get_product_data()]
            self.search_products(keyword)
        return self.products

    def _configure_session(self):
        retry_strategy = Retry(
            total=3,
            status_forcelist=[403, 404, 429, 500, 502, 503, 504]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        return session

    def get_headers(self):
        return {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Origin': self.origin,
            'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def search_products(self, keyword):

        api_url = (
            f'https://api.linximpulse.com/engage/search/v3/search?apikey={self.api_key}'
            f'&origin={self.origin}&page={self.page}&resultsPerPage={self.results_per_page}&terms={keyword}'
            f'&allowRedirect=true&salesChannel=461&salesChannel=catalogmkp&sortBy=relevance'
        )
        headers = self.get_headers()

        try:
            response = self.http.get(api_url, headers=headers)
            response.raise_for_status()
            if response.status_code == 200:
                self.content = response.json()
            else:
                raise(response.status_code)
        except requests.exceptions.RequestException as e:
            raise(f"Erro ao fazer requisição: {e}") 
    
    def get_product_data(self):
        if self.content:
            products = self.content["products"]
            return products
        else:
            print(f"Erro na resposta: {self.content}")
            return []
    
    def get_total_pages(self):
        last_page = 1
        pagination = self.content["pagination"]
        last_page_url = pagination["last"]
        
        pattern = r'page=(\d+)'
        match = re.search(pattern, last_page_url)
        if match:
            page_value = match.group(1)
            print(f"O valor da página é: {page_value}")
            last_page = page_value
        
        return int(last_page)

# Uso da classe
keyword = 'azeite'
scraper = PaoDeAcucarScraper()
data = scraper.start(keyword)

if data:
    print(data)
