import streamlit as st
import pandas as pd
from utils.market_data import get_live_price
from utils.calculations import calculate_pnl, option_status, days_to_expiry

def show_dashboard(df):
    st.subheader("📊 Portfolio Dashboard")

    results = []
    total_pnl = 0

    for _, trade in df.iterrows():
        price = get_live_price(trade["ticker"])
        if price is None:
            continue

        pnl = calculate_pnl(trade, price)
        status = option_status(trade, price)
        dte = days_to_expiry(pd.to_datetime(trade["expiry"]).date())

        total_pnl += pnl

        results.append({
            "Ticker": trade["ticker"],
            "Type": trade["type"],
            "Price": price,
            "Strike": trade["strike"],
            "Expiry": trade["expiry"],
            "DTE": dte,
            "Status": status,
            "P&L ($)": pnl
        })

    st.metric("💰 Total P&L", f"${round(total_pnl,2)}")

    if results:
        st.dataframe(pd.DataFrame(results), use_container_width=True)
