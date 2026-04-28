from datetime import datetime

def calculate_pnl(trade, current_price):
    strike = float(trade["strike"])
    premium = float(trade["premium"])
    shares = int(trade["shares"])

    if trade["type"] == "CSP":
        intrinsic = max(0, strike - current_price)
    else:  # Covered Call
        intrinsic = max(0, current_price - strike)

    return round((premium - intrinsic) * shares, 2)


def option_status(trade, current_price):
    strike = float(trade["strike"])

    if trade["type"] == "CSP":
        return "ITM 🔴" if current_price < strike else "OTM 🟢"
    else:
        return "ITM 🔴" if current_price > strike else "OTM 🟢"


def days_to_expiry(expiry):
    today = datetime.today().date()
    return (expiry - today).days
