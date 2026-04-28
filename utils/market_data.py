import yfinance as yf

def get_live_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        return float(data["Close"].iloc[-1])
    except:
        return None
