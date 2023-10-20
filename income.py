class Income:

    def __init__(self, num_income, category, description):
        self.num_income = num_income
        self.category = category
        self.description = description
         
income_storage = []   

def add_income():
    num_income = input("Введите свой доход: ")
    category = input("Категория: ")
    description= input("Описание: ")
    income = Income(num_income, category, description)
    income_storage.append(income)
    print("Транзакция успешно добавлена")
    
def delete_income():
    print("Транзакция успешно удалена.")
    num_income = None
    category = None
    description = None
        

 





