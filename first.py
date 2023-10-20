# print("Консольная игра 'Угадай число'")
# import random
# min = int(input("Введите начальный диапазон: "))
# max = int(input ("Введите конечный диапазон: "))

# random_number =  random.randint(min, max)
# attempts = 0
# print ("Мы сгенерировали случайное число в указанном вами диапазоне! Попробуйте его угадать!")


# while True:
#     response = int(input("Введите число: "))
#     attempts += 1
#     if response < random_number:
#         print ("Случайное число больше, попробуйте снова")
#     elif response > random_number:
#         print ("Случайное число меньше, попробуйте снова")
#     else: 
#         print (f'Ура! Вы угдали загаданное число за {attempts} попыток.')
#         break


# print ("Конвертер валют")
# choose = {
#     "KGS": 1,
#     "USD": 2,
#     "RUB": 3,
#     "JPY": 4
# }
# for key, value in choose.items():
#     print(value, key)
# convert_from = int(input("Выберите номер валюты из выше перечисленных С котрой нужно перевести: "))
# convert_to = int(input("Выберите валюту НА которую нужно перевести: "))
# amount = float(input("Введите сумму: "))

# exchange = {
#     "KGS": 1,
#     "USD": 88.25,
#     "RUB": 0.92, 
#     "JPY": 0.61
# }

# def converter(convert_to, amount):
#     try:
#         if convert_to not in choose.values():
#             raise "Неверный номер валюты"
#         if convert_to == 1:
#             print(f'{amount}KGS = {amount/exchange["KGS"]} KGS') 
#         elif convert_to == 2:
#             print(f'{amount}KGS = {amount/exchange["USD"]:.2f} USD') 
#         elif convert_to == 3:
#             print(f'{amount}KGS = {amount/exchange["RUB"]:.2f} RUB') 
#         elif convert_to == 4:
#             print(f'{amount}KGS = {amount/exchange["JPY"]:.2f} JPY') 
#     except Exception:
#         print ("Убедитесь, что выбрали номер валюты из вышеперечисленного")
        
# converter(convert_to, amount)




from income import  add_income, delete_income
from expense import add_expense, delete_expense
from show import display_statistics, view_transitions
while True:
    choose_functions = {
            1: "Добавление дохода",
            2: "Добавление расхода",
            3: "Удаление транзакции: Доход ",
            4: "Удаление транзакции: Расход ",
            5: "Просмотр списка транзакций",
            6: "Анализ и отображение статистики"
        }
    for key, value in choose_functions.items():
        print(key, value)
        
    action = int(input("Выберите действие: "))  
    
    if action == 1:
        add_income()
    elif action == 2:
        add_expense()
    elif action == 3:
        delete_income()
    elif action == 4:
        delete_expense()
    elif action == 5:
        view_transitions()
    elif action == 6:
        display_statistics()
    else:
        print("Убедитесь, что выбрали число из вышеуказанных")
