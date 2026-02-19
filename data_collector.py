import requests
from typing import Dict, Optional

class DataCollector:
    """
    Collects performance data from multiple affiliate networks.
    
    Attributes:
        headers: Default HTTP request headers
        proxies: List of available proxies for IP rotation (optional)
    """
    
    def __init__(self, proxies: Optional[List[str]] = None):
        self.headers = {'Content-Type': 'application/json'}
        self.proxies = proxies
        
    def collect(self, networks: List[str]) -> Dict:
        """
        Collects data from specified affiliate networks.
        
        Args:
            networks: List of network URLs to collect data from
            
        Returns:
            Dictionary mapping network names to their response data
        """
        data = {}
        try:
            for network in networks:
                proxy = self._get_proxy() if self.proxies else None
                response = requests.get(network, headers=self.headers, proxies=proxy)
                if response.status_code == 200:
                    data[network] = response.json()
                else:
                    self._log_request_error(network, response.status_code)
        except requests.RequestException as e:
            self._log_error(str(e))
            raise
        return data
    
    def _get_proxy(self) -> Optional[Dict]:
        """
        Returns a random proxy from the list for IP rotation.
        """
        if not self.proxies:
            return None
        # Implementation to rotate proxies would go here
        return {"http": self.proxies[0]}
    
    def _log_request_error(self, network: str, status_code: int):
        logging.error(f"Request to {network} failed with status code {status_code}")