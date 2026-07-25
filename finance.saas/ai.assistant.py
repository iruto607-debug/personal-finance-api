def ai_financial_advisor(income, expense, df):

    if income == 0:
        return "No financial data available yet."

    savings_rate = (income - expense) / income * 100

    insights = []

    # Spending logic
    if expense > income:
        insights.append("⚠ Critical: You are spending more than you earn.")
    elif expense > income * 0.7:
        insights.append("⚠ Warning: High spending ratio detected.")
    else:
        insights.append("✅ Healthy spending pattern.")

    # Savings analysis
    if savings_rate < 20:
        insights.append("💡 Advice: Try saving at least 20% of income.")
    else:
        insights.append("💰 Good savings discipline detected.")

    # Category insight
    if not df.empty:
        expense_by_category = (
            df[df["type"] == "Expense"].groupby("category")["amount"].sum()
        )
        top_category = expense_by_category.idxmax()
        insights.append(f"📊 Highest spending category: {top_category}")

    return "\n".join(insights)
