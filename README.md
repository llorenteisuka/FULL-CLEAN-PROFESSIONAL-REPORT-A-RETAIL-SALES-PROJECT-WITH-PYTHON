# Retail Sales Analysis with Python
 Python-based retail sales data analysis using EDA, data cleaning, and visualizations to generate business insights.


## Project Overview

This repository contains a complete Python project focused on analyzing retail sales data to uncover customer behavior, product performance, and revenue trends.

The project covers:

* Data loading and understanding
* Data cleaning and preparation
* Exploratory Data Analysis (EDA)
* Basic statistical analysis
* Data visualizations (sales distribution & category analysis)
* Computation of key performance indicators (KPIs)
* Date formatting and column normalization

##  Project Objective

The main objectives of this project are to:

* Understand customer purchasing behavior
* Analyze product and category performance
* Study revenue patterns and trends
* Generate actionable business insights
* Build strong foundational Python analytics skills

This project follows the **Data Analytics Lifecycle**:

1. Define objectives
2. Load and understand data
3. Clean and prepare data
4. Perform exploratory data analysis
5. Visualize data and generate insights


## Dataset Description
Three datasets were used in this analysis:

# Sales Dataset
Contains transaction-level data:
* Order ID
* Date
* Customer ID
* Gender
* Age
* Product category
* Quantity
* Unit price
* Total amount

# Customer Dataset
Includes customer demographic information:
* Age
* Country
* Gender

# Product Dataset
Contains product details:
* Product name
* Category
* Supplier
* Price and cost

# Technologies Used

| Tool       | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Primary programming language |
| Pandas     | Data loading and cleaning    |
| NumPy      | Numerical operations         |
| Matplotlib | Data visualization           |
| Seaborn    | Statistical visualizations   |



# Project Workflow



### Project Workflow

### ✔ Step 1 — Import Libraries
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
````

### ✔ Step 2 — Load Datasets

```python
sales = pd.read_csv("sales_data.csv")
products = pd.read_csv("products_data.csv")
customers = pd.read_csv("customers_data.csv")
```

### ✔ Step 3 — Preview & Inspect Data

```python
sales.head()
sales.info()
products.info()
customers.info()
```

Purpose: Understand data structure, data types, and missing values.


### ✔ Step 4 — Data Cleaning

```python
sales.columns = sales.columns.str.replace(" ", "_")
sales['date'] = pd.to_datetime(sales['date'])
sales['total_sales'] = sales['quantity'] * sales['unitprice']
```

### ✔ Step 5 — Exploratory Data Analysis

```python
sales.describe()
customers.describe()
products.describe()
```

Key insights generated:

* Frequency of product categories
* Mean age of customers
* Average quantity purchased
* Product price range (min–max)
* Average selling amount
* Total customers
* 5 unique countries
* Age distribution and popular price ranges

---

##  Visualizations

###  Sales Distribution

```python
sns.histplot(sales['total_amount'], bins=30)
plt.title("Distribution of Total Sales")
plt.show()
```

### Product Category Frequency

```python
sns.countplot(data=sales, x='product_category')
plt.xticks(rotation=45)
plt.title("Product Category Frequency")
plt.show()
```


## 🔍 Key Insights

### Sales Insights

* Most purchases fall between **GHS 0–250**
* **Electronics** and **Fashion** show strong purchase volumes

### Customer Insights

* Customers aged **30–45** purchase the most
* Data includes **5 unique countries**

# Product Insights

* Certain categories dominate revenue
* Average quantity purchased is **2–3 items**



# Conclusion
This project demonstrates foundational Python analytics skills including:
* Data preparation
* Exploratory Data Analysis (EDA)
* Data visualization
* Generating actionable insights

```
