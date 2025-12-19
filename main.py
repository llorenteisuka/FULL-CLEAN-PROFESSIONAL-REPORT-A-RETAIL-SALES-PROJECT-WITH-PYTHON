import pandas as pd

sales = pd.read_csv(r"C:\Users\DELL\Desktop\proWithPy\sales_data .csv")
customer =  pd.read_csv(r"C:\Users\DELL\Desktop\proWithPy\customers_data.csv")
product = pd.read_csv(r"C:\Users\DELL\Desktop\proWithPy\products_data.csv")

print(sales)
print(sales.info())
print(sales.head())

print (customer)
print(customer.info())
print(customer.head())

print(product)
print(product.info())
print(product.head())

desc = sales.describe(include='all') 
print(desc)

custdesc = customer.describe(include='all') 
print(custdesc)

produtdesc = customer.describe(include='all') 
print(custdesc)

total_sales = sales['Quantity'] * sales['UnitPrice']
print(total_sales)
sales['Total_amount'] = total_sales




import datetime as dt
ref_date = dt.datetime(2024, 1, 1)
print(ref_date)

sales['Date'] = pd.to_datetime(sales['Date'], errors='coerce')
print(sales['Date'].dtype)

sales['recency'] = (ref_date - sales['Date']).dt.days
print(sales[['Date', 'recency']].head())



import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize=(10, 6))
sns.histplot(sales['Total_amount'], bins=20, color='skyblue', kde=True)
plt.title('sales Distribution')
plt.xlabel('TOTAL AMOUNT')
plt.ylabel('frecuency')
plt.show()


sales.groupby('Category') ['total_amount'].sum().plot(kind='bar') 
plt.title("REVENUE BY PRODUCT")
plt.show()



