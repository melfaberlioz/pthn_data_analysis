import pandas as pd
import matplotlib.pyplot as pltdf
from matplotlib import pyplot as plt=pd.read_csv("gasstation.csv")

df1=pd.read_csv("gasprice.csv")
df2=pd.read_csv("gasmanage.csv")
df3=pd.read_csv("gasmanage1.csv")
#зчитую усі дані в окремі датафрейми

concataccount=pd.concat([df2,df3])
#з двох облікових файлів роблю один

merged=pd.merge(concataccount,df,on="id")
#з'єдную датафрейми, щоб додати назву заправки
mergednew=pd.merge(merged,df1,on="gasname")
#з'єдную датафрейми, щоб додати ціну за бензину
mergednew["finalsum"]=mergednew["amountofgas"]*mergednew["price"]
#роблю новий стовпець з фінальною сумою за операцію
totalamount = mergednew.groupby(by=['id','cityname'])['finalsum'].sum().sort_values()
#групую за номером та назвою і сумую усі суми операцій
print(totalamount.to_frame())

totalamount.plot(kind="bar",color=['black', 'red', 'green', 'blue', 'cyan',"orange","purple"])
#роблю стовпичкову діаграму з різними кольорами

plt.show()