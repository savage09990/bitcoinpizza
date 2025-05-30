# Bitcoin Pizza Counter 🍕

A Streamlit app that analyzes Bitcoin transactions to estimate how many pizzas might have been bought on a given day. The analysis is based on transaction patterns, amounts, and keywords that might indicate pizza purchases.

## Features

- Analyze Bitcoin transactions for any date since the genesis block
- Estimate pizza-related transactions based on various heuristics
- View detailed transaction information
- Special highlight for the famous Bitcoin Pizza Day (May 22, 2010)

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app locally:
   ```bash
   streamlit run app.py
   ```

## Deployment

This app is designed to be deployed on Streamlit Cloud. To deploy:

1. Push your code to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with your GitHub account
4. Click "New app"
5. Select your repository, branch, and main file (app.py)
6. Click "Deploy"

## Data Source

This app uses the [Blockchair API](https://blockchair.com/api/docs) to fetch Bitcoin transaction data.

## License

MIT License 