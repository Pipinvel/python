
from income import Income, income_storage
from expense import Expense, ex_storage

def display_statistics():
    display_incomes = sum(float(income.num_income) for income in income_storage)
    display_expenses = sum(float(expense.num_expense) for expense in ex_storage)
    balance = display_incomes - display_expenses
    
    print(f"Общий доход: {display_incomes}")
    print(f"Общий расход: {display_expenses}")
    print(f"Баланс: {balance}")
    
def view_transitions():
    print("Доходы:")
    for income in income_storage:
        print(f"{income.category}: {income.num_income} сом")
        print(f"{income.description}\n")
    
    print("Расходы:")
    for expense in ex_storage:
        print(f"{expense.category}: {expense.num_expense} сом")
        print(f"{expense.description}\n")
   
    

    