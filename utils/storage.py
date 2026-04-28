import pandas as pd
import os

FILE = "data/trades.csv"

def load_trades():
    if not os.path.exists(FILE):
        return pd.DataFrame(columns=[
            "ticker","type","strike","expiry",
            "premium","shares"
        ])
    return pd.read_csv(FILE)


def save_trade(trade):
    df = load_trades()
    df = pd.concat([df, pd.DataFrame([trade])])
    df.to_csv(FILE, index=False)
