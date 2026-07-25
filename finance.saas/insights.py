def financial_health_score(income, expense):

    if income == 0:
        return 0

    score = ((income - expense) / income) * 100

    return max(0, min(100, score))


def spending_alert(expense, income):

    if expense > income:
        return "🚨 High Risk: Overspending detected"
    elif expense > income * 0.7:
        return "⚠ Warning: High spending ratio"
    else:
        return "✅ Healthy financial behavior"
