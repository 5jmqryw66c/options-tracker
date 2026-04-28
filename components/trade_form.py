import streamlit as st
from datetime import date
from utils.storage import save_trade

def trade_form():
    st.subheader("➕ Add Trade")

    with st.form("trade_form"):
        ticker = st.text_input("Ticker").upper()
        option_type = st.selectbox("Type", ["CSP", "Covered Call"])
        strike = st.number_input("Strike", min_value=0.0)
        expiry = st.date_input("Expiry", min_value=date.today())
        premium = st.number_input("Premium (per share)", min_value=0.0)
        shares = st.number_input("Shares", value=100)

        submitted = st.form_submit_button("Save Trade")

        if submitted:
            save_trade({
                "ticker": ticker,
                "type": option_type,
                "strike": strike,
                "expiry": expiry,
                "premium": premium,
                "shares": shares
            })
            st.success("Trade saved!")
