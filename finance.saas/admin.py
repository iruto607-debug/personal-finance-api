import streamlit as st
from database import db, User, Transaction

st.set_page_config(page_title="Investor Dashboard")

st.title("🏢 Startup Admin Panel")

users = db.query(User).all()
transactions = db.query(Transaction).all()

total_users = len(users)
total_transactions = len(transactions)

st.metric("Total Users", total_users)
st.metric("Total Transactions", total_transactions)

premium_users = [u for u in users if hasattr(u, "is_premium")]

st.info("📊 System Overview Ready for Investors")