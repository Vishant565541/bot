# Binance Futures Trading Bot

This project is a command-line trading bot for Binance Futures, designed for both educational and practical use. It allows users to place various types of orders (Market, Limit, Stop-Limit, and Take-Profit-Market) on Binance Futures using the official Binance API. The bot is configured to use the Binance Testnet by default, making it safe for testing without risking real funds.

## Features
- **Interactive CLI**: Guides users through order creation with input validation.
- **Order Types Supported**:
  - Market Order
  - Limit Order
  - Stop-Limit Order
  - Take-Profit-Market Order
- **Logging**: All actions and errors are logged to `trading_bot.log` for easy debugging and tracking.
- **Testnet Support**: Uses Binance Testnet endpoints for safe practice trading.

## How It Works
1. **User Input**: The CLI (`cli.py`) prompts the user for trading details such as symbol, side (BUY/SELL), order type, quantity, and relevant prices.
2. **Order Execution**: Based on the user's input, the bot (implemented in `trading_bot.py`) sends the appropriate order request to the Binance Futures API.
3. **Result Display**: The result of the order (success or error) is displayed to the user and logged.

## File Overview
- `cli.py`: Handles user interaction, collects order details, and calls the trading bot methods.
- `trading_bot.py`: Contains the `BasicBot` class, which wraps Binance API calls for different order types and manages logging.

## Requirements
- Python 3.7+
- `python-binance` library

Install dependencies with:
```bash
pip install python-binance
```

## Usage
1. **Set Your API Keys**: Replace the `API_KEY` and `API_SECRET` in `cli.py` with your Binance Testnet credentials.
2. **Run the Bot**:
```bash
python cli.py
```
3. **Follow the Prompts**: Enter the required trading details as prompted.

## Security Note
- **Never use real API keys on Testnet or share your credentials.**
- This bot is for educational and testing purposes only. Use at your own risk.

## Logging
- All actions and errors are logged to `trading_bot.log` in the project directory.

## Disclaimer
This project is for educational purposes. Trading cryptocurrencies involves risk. The author is not responsible for any financial losses. 
