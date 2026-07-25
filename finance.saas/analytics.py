def financial_summary(df):

    income = df[df["type"] == "Income"]["amount"].sum()
    expense = df[df["type"] == "Expense"]["amount"].sum()

    return income, expense, income - expense


def expense_breakdown(df):
    expenses = df[df["type"] == "Expense"]
    breakdown = expenses.groupby("category")["amount"].sum()
    return breakdown.reset_index()
