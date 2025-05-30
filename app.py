import streamlit as st
from datetime import datetime, timedelta
from blockchair_api import get_blockchair_data
from pizza_counter import get_pizza_transactions, is_pizza_related

# Set page config
st.set_page_config(
    page_title="Bitcoin Pizza Counter 🍕",
    page_icon="🍕",
    layout="wide"
)

# Title and description
st.title("Bitcoin Pizza Counter 🍕")
st.markdown("""
This app analyzes Bitcoin transactions to estimate how many pizzas might have been bought on a given day.
The analysis is based on transaction patterns, amounts, and keywords that might indicate pizza purchases.
""")

# Sidebar for date selection
st.sidebar.header("Date Selection")
default_date = "2010-05-22"  # The famous pizza day
max_date = datetime.now().date()

# Date input with validation
selected_date = st.sidebar.date_input(
    "Select a date to analyze",
    value=datetime.strptime(default_date, "%Y-%m-%d").date(),
    max_value=max_date,
    min_value=datetime(2009, 1, 3).date()  # Bitcoin genesis block
)

# Convert date to string format
date_str = selected_date.strftime("%Y-%m-%d")

# Main content
st.header(f"Analysis for {date_str}")

# Add a loading spinner while fetching data
with st.spinner("Fetching Bitcoin transaction data..."):
    data = get_blockchair_data(date_str)

if data and "data" in data:
    transactions = data["data"]
    pizza_txs = get_pizza_transactions(transactions, date_str)
    
    # Display metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "🍕 Estimated Pizzas",
            len(pizza_txs),
            help="Number of transactions that might be pizza-related"
        )
    
    with col2:
        total_txs = len(transactions)
        st.metric(
            "📊 Total Transactions",
            total_txs,
            help="Total number of Bitcoin transactions on this day"
        )
    
    with col3:
        if total_txs > 0:
            percentage = (len(pizza_txs) / total_txs) * 100
            st.metric(
                "📈 Pizza Ratio",
                f"{percentage:.2f}%",
                help="Percentage of transactions that might be pizza-related"
            )
    
    # Display transaction details in an expander
    with st.expander("View Pizza-Related Transactions", expanded=False):
        if pizza_txs:
            for tx in pizza_txs:
                tx_hash = tx.get("hash", "Unknown")
                tx_time = datetime.fromtimestamp(tx.get("time", 0)).strftime("%H:%M:%S")
                tx_fee = tx.get("fee", 0) / 100000000  # Convert to BTC
                
                st.markdown(f"""
                **Transaction Hash:** `{tx_hash}`  
                **Time:** {tx_time}  
                **Fee:** {tx_fee:.8f} BTC
                """)
                st.markdown("---")
        else:
            st.info("No pizza-related transactions found for this date.")
    
    # Add some historical context
    if date_str == default_date:
        st.info("""
        🎯 This is the famous "Bitcoin Pizza Day" when Laszlo Hanyecz paid 10,000 BTC for two pizzas!
        The actual transaction might not be detected by our heuristics as it was a special case.
        """)
    
else:
    st.error("""
    Failed to fetch data from Blockchair API. This could be due to:
    - API rate limiting
    - Network issues
    - Invalid date range
    - API service disruption
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Made with ❤️ and 🍕 | Data from <a href='https://blockchair.com' target='_blank'>Blockchair API</a></p>
</div>
""", unsafe_allow_html=True) 