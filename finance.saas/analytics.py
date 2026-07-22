import pandas as pd

def financial_summary(df):

    income = df[df["type"] == "Income"]["amount"].sum()
    expense = df[df["type"] == "Expense"]["amount"].sum()

    return income, expense, income - expense


def expense_breakdown(df):
    return df[df["type"] == "Expense"].groupby("category")["amount"].sum().reset_index()