from trading_bot import BasicBot
import sys

# Load your Testnet credentials
API_KEY = "BSpJ3fowkgTeIoPXPHA9DAYSWWoHtwqu0pW5n3XewPMQGTgAiATh1Ic3sZcZ9gPg"
API_SECRET = "etYIq2jUlHU1JFZ7pqRGWV7NaiJB4tJfDOs27SgsPSBi5QEf8oGZ72uDEG2JiH43"

def get_user_input():
    print("\nWelcome to the Binance Futures Trading Bot!\n")

    symbol = input("Enter trading symbol (e.g., BTCUSDT): ").upper()
    side = input("Order side [BUY / SELL]: ").upper()

    # Enhanced order type selection
    print("Select order type:")
    print("1. MARKET")
    print("2. LIMIT")
    print("3. STOP-LIMIT")
    print("4. TAKE-PROFIT-MARKET")
    order_type_map = {
        '1': 'MARKET',
        '2': 'LIMIT',
        '3': 'STOP-LIMIT',
        '4': 'TAKE-PROFIT-MARKET'
    }
    order_type_choice = input("Enter order type number: ").strip()
    order_type = order_type_map.get(order_type_choice, None)
    if not order_type:
        print("Invalid order type selection.")
        sys.exit(1)

    # Input validation for quantity
    while True:
        try:
            quantity = float(input("Enter quantity: "))
            if quantity <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid quantity. Please enter a positive number.")

    if order_type == "LIMIT":
        while True:
            try:
                price = float(input("Enter limit price: "))
                if price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid price. Please enter a positive number.")
        return symbol, side, order_type, quantity, price
    elif order_type == "STOP-LIMIT":
        while True:
            try:
                stop_price = float(input("Enter stop price: "))
                limit_price = float(input("Enter limit price: "))
                if stop_price <= 0 or limit_price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid price. Please enter positive numbers.")
        return symbol, side, order_type, quantity, stop_price, limit_price
    elif order_type == "TAKE-PROFIT-MARKET":
        while True:
            try:
                stop_price = float(input("Enter take-profit trigger price: "))
                if stop_price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid price. Please enter a positive number.")
        return symbol, side, order_type, quantity, stop_price
    else:
        return symbol, side, order_type, quantity

def main():
    bot = BasicBot(API_KEY, API_SECRET, testnet=True)
    order_info = get_user_input()

    symbol, side = order_info[0], order_info[1]
    order_type = order_info[2]

    if order_type == "MARKET":
        result = bot.place_market_order(symbol, side, order_info[3])
    elif order_type == "LIMIT":
        result = bot.place_limit_order(symbol, side, order_info[3], order_info[4])
    elif order_type == "STOP-LIMIT":
        result = bot.place_stop_limit_order(symbol, side, order_info[3], order_info[4], order_info[5])
    elif order_type == "TAKE-PROFIT-MARKET":
        result = bot.place_take_profit_market_order(symbol, side, order_info[3], order_info[4])
    else:
        print("Invalid order type.")
        return

    print("\nOrder Result:")
    print(result)

if __name__ == "__main__":
    main()
