class Expense:
    def __init__(self, num_expense, category, description):
        self.num_expense = num_expense
        self.category = category
        self.description = description
        
ex_storage = []   

def add_expense():
    num_expense = input("Введите свой расход: ")
    category = input("Категория: ")
    description= input("Описание: ")
    expense = Expense(num_expense, category, description)
    ex_storage.append(expense)
    print("Транзакция успешно добавлена")
    
def delete_expense():
    print("Транзакция успешно удалена.")
    num_expense = None
    category = None
    description = None


        
    