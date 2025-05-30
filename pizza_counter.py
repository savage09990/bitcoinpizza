from typing import Dict, Any, List
from datetime import datetime

def is_pizza_related(tx: Dict[str, Any]) -> bool:
    """
    Determine if a transaction might be pizza-related based on various heuristics.
    
    Args:
        tx (Dict[str, Any]): A Bitcoin transaction object from Blockchair API
        
    Returns:
        bool: True if the transaction might be pizza-related, False otherwise
        
    Note:
        This is a heuristic-based filter that looks for:
        - 'pizza' keyword in decoded script
        - Small transaction fees (typical for small purchases)
        - Small output amounts (typical for pizza purchases)
    """
    # Check for pizza keyword in decoded script
    if 'pizza' in tx.get('decoded_script', '').lower():
        return True
        
    # Check for small transaction fees (typical for small purchases)
    if 0.001 <= tx.get('fee', 0) <= 0.01:
        return True
        
    # Check for small output amounts (typical for pizza purchases)
    outputs = tx.get('outputs', [])
    for output in outputs:
        value = output.get('value', 0) / 100000000  # Convert satoshis to BTC
        if 0.001 <= value <= 0.1:  # Typical range for a pizza purchase
            return True
            
    return False

def filter_transactions_by_date(transactions: List[Dict[str, Any]], date: str) -> List[Dict[str, Any]]:
    """
    Filter transactions for a specific date.
    
    Args:
        transactions (List[Dict[str, Any]]): List of transactions from Blockchair API
        date (str): Date in YYYY-MM-DD format
        
    Returns:
        List[Dict[str, Any]]: Filtered list of transactions for the specified date
    """
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        return [
            tx for tx in transactions
            if datetime.fromtimestamp(tx.get('time', 0)).date() == target_date
        ]
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")

def get_pizza_transactions(transactions: List[Dict[str, Any]], date: str) -> List[Dict[str, Any]]:
    """
    Get all pizza-related transactions for a specific date.
    
    Args:
        transactions (List[Dict[str, Any]]): List of transactions from Blockchair API
        date (str): Date in YYYY-MM-DD format
        
    Returns:
        List[Dict[str, Any]]: List of pizza-related transactions for the specified date
    """
    date_filtered = filter_transactions_by_date(transactions, date)
    return [tx for tx in date_filtered if is_pizza_related(tx)] 