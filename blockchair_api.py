import requests
from typing import Optional, Dict, Any

def get_blockchair_data(date: str) -> Optional[Dict[str, Any]]:
    """
    Fetch Bitcoin transaction data from Blockchair API for a specific date.
    
    Args:
        date (str): The date to fetch transactions for in YYYY-MM-DD format
        
    Returns:
        Optional[Dict[str, Any]]: JSON response containing transaction data if successful,
                                 None if the request fails
    """
    url = f"https://api.blockchair.com/bitcoin/transactions?q=time({date})"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None 