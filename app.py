import streamlit as st
from utils.storage import load_trades
from components.trade_form import trade_form
from components.dashboard import show_dashboard

st.set_page_config(page_title="Options Tracker", layout="wide")

st.title("📈 Options Selling Tracker")

tab1, tab2 = st.tabs(["Dashboard", "Add Trade"])

with tab1:
    df = load_trades()
    show_dashboard(df)

with tab2:
    trade_form()
