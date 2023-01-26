import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
# add libraries


service1 = pd.read_csv('services1.csv')
service2 = pd.read_csv('services2.csv')
service3 = pd.read_csv('services3.csv')
accounting = pd.concat([service1, service2, service3], axis=0)
accounting.reset_index(drop=True)
# додаємо два файла та групуємо їх в єдину таблицю

# читати файл csv
fuel = pd.read_csv('price.csv')
# об'єднання змінних fuel and accounting
accounting = pd.merge(accounting, fuel)
# read csv file
gas_station = pd.read_csv('filling1.csv')
# merge accounting and gas_station
accounting = pd.merge(accounting, gas_station)
print(accounting)
# додаємо ще 2 файла з даними і маємо фінальну таблицю


accounting['bonus_95'] = accounting[accounting['Patrol']=='PULLS_95']['Quantity']*1
accounting['bonus_Disel'] = accounting[accounting['Patrol']=='PULLS_Disel']['Quantity']*1
accounting['income'] = accounting['Quantity']*accounting['Price']
accounting = accounting.fillna(0)
print(accounting)
#  вираховуємо бонуси та дохід

income_bar = accounting.groupby('Idnumber')['income'].sum()
print(income_bar)
# групуємо та маємо результат для кожної заправки

income_bar.plot.bar(color='g')
# будуємо діаграму

def proceeds(Name):
    proceeds_ = (accounting[accounting['Name']==Name]['income']).sum()
    return proceeds_
widgets.interact(proceeds, Name = accounting['Name'].unique())
#створємо функцію в якій ділимо по містах і для кожного окремо знаходимо заробіток
#вивводимо за допомогою бібліотеки ipywidgets

def ret(Name, Date):
    proceeds = (accounting[accounting['Name']==Name] [accounting['Date']==Date]['income']).sum()
    return proceeds
widgets.interact(ret, Name = accounting['Name'].unique(), Date = accounting['Date'].unique())

shark = accounting['bonus_Disel'].sum() + accounting['bonus_95'].sum()
print("for charity: " + str(shark))
#сумуємо благодійні кошти за різне пальне і маємо результат