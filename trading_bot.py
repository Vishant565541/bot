import logging
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException

# Configure logging
logging.basicConfig(filename='trading_bot.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
            self.client.FUTURES_WEBSOCKET_URL = 'wss://stream.binancefuture.com/ws'
        logging.info('Initialized BasicBot with testnet=%s', testnet)

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info('Market order placed: %s', order)
            return order
        except BinanceAPIException as e:
            logging.error('Market order error: %s', e)
            return {'error': str(e)}

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            logging.info('Limit order placed: %s', order)
            return order
        except BinanceAPIException as e:
            logging.error('Limit order error: %s', e)
            return {'error': str(e)}

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                type=ORDER_TYPE_STOP,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=limit_price,
                stopPrice=stop_price
            )
            logging.info('Stop-Limit order placed: %s', order)
            return order
        except BinanceAPIException as e:
            logging.error('Stop-Limit order error: %s', e)
            return {'error': str(e)}

    def place_take_profit_market_order(self, symbol, side, quantity, stop_price):
        """
        Place a Take-Profit Market order (closes position at market price when stop_price is reached).
        """
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                type=ORDER_TYPE_TAKE_PROFIT_MARKET,
                quantity=quantity,
                stopPrice=stop_price,
                timeInForce=TIME_IN_FORCE_GTE_GTC
            )
            logging.info('Take-Profit Market order placed: %s', order)
            return order
        except BinanceAPIException as e:
            logging.error('Take-Profit Market order error: %s', e)
            return {'error': str(e)}
