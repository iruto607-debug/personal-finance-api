import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

from database import db, Transaction
from auth import register_user, login_user
from analytics import financial_summary, expense_breakdown
from insights import financial_health_score, spending_alert

st.set_page_config(page_title="Startup Finance App", layout="wide")

if "user" not in st.session_state:
    st.session_state.user = None

# ---------------- LOGIN ----------------
if st.session_state.user is None:

    st.title("💼 Startup Finance App")

    mode = st.radio("Choose", ["Login", "Register"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if mode == "Register":
        if st.button("Create Account"):
            if register_user(username, password):
                st.success("Account created")
            else:
                st.error("User already exists")

    if mode == "Login":
        if st.button("Login"):
            if login_user(username, password):
                st.session_state.user = username
                st.rerun()
            else:
                st.error("Invalid login")

# ---------------- APP ----------------
else:

    user = st.session_state.user

    st.sidebar.success(f"Logged in as {user}")

    menu = st.sidebar.radio(
        "Menu",
        ["Dashboard", "Add Transaction", "Analytics"]
    )

    df = pd.read_sql(
        f"SELECT * FROM transactions WHERE username='{user}'",
        db.bind
    )

    # ---------------- DASHBOARD (INVESTOR VERSION) ----------------
    if menu == "Dashboard":

        st.header("📊 Investor Dashboard View")

        # SAFE HANDLING (important for empty data)
        if df.empty:
            st.info("No transactions yet. Add data to see insights.")
            st.stop()

        # BASIC FINANCIALS
        income = df[df["type"] == "Income"]["amount"].sum()
        expense = df[df["type"] == "Expense"]["amount"].sum()
        profit = income - expense

        # METRICS
        col1, col2, col3 = st.columns(3)

        col1.metric("Total Income", f"{income:,.2f}")
        col2.metric("Total Expenses", f"{expense:,.2f}")
        col3.metric("Net Profit", f"{profit:,.2f}")

        # FINANCIAL HEALTH SCORE
        score = financial_health_score(income, expense)

        st.progress(int(score))
        st.success(f"Financial Health Score: {score:.1f}/100")

        # ALERT SYSTEM
        st.info(spending_alert(expense, income))

        st.divider()

        # GROWTH VISUALS (INVESTOR IMPORTANT)
        fig = px.bar(
            df.groupby("type")["amount"].sum().reset_index(),
            x="type",
            y="amount",
            title="Revenue vs Expenses"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ---------------- ADD TRANSACTION ----------------
    elif menu == "Add Transaction":

        st.header("➕ Add Transaction")

        t_type = st.selectbox("Type", ["Income", "Expense"])
        category = st.text_input("Category")
        amount = st.number_input("Amount", min_value=0.0)

        if st.button("Save"):

            db.add(Transaction(
                username=user,
                date=str(datetime.now()),
                type=t_type,
                category=category,
                amount=amount
            ))
            db.commit()

            st.success("Saved successfully")
            st.rerun()

    # ---------------- ANALYTICS ----------------
    elif menu == "Analytics":

        st.header("📊 Analytics")

        if df.empty:
            st.info("No data available")
            st.stop()

        # PIE CHART
        fig1 = px.pie(
            df[df["type"] == "Expense"],
            names="category",
            values="amount",
            title="Expense Breakdown"
        )

        st.plotly_chart(fig1, use_container_width=True)

        # BAR CHART
        breakdown = expense_breakdown(df)

        fig2 = px.bar(
            breakdown,
            x="category",
            y="amount",
            title="Spending by Category"
        )

        st.plotly_chart(fig2, use_container_width=True)