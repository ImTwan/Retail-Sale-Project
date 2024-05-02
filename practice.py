import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

class RetailSaleAnalyzer:
    def __init__(self):
        #read the data
        self.data  = pd.read_csv("retail_sales.csv")
        self.data['Date'] = pd.to_datetime(self.data['Date'])


    def clean_data(self):
        self.data.dropna(inplace = True ) #Check for and remove rows with missing values in any column. 

    def total_sales_per_product(self):
        return self.data.groupby('Product')['Sales'].sum()
    
    def best_selling_product(self): 
        return self.total_sales_per_product().sort_values(ascending = False).index[0]
    
    def average_daily_sales(self):
        return self.data['Sales'].mean() #calculate average sales 
    
    #Data visualization
    def plot_sales_trend(self):
        self.data.groupby('Date')['Sales'].sum().plot(kind = 'line')
        plt.title('Sales Trend Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Sales')
        plt.show()

    def plot_sales_per_product(self):
        self.total_sales_per_product().plot(kind = 'bar')
        plt.title('Total Sales per Product')
        plt.xlabel('Product')
        plt.ylabel('Total Sales')
        plt.show()

analyzer = RetailSaleAnalyzer()
print("Total Sales per Product: \n", analyzer.total_sales_per_product())
print("Best Selling Product: ", analyzer.best_selling_product())
print("Average Daily Sales: ", analyzer.average_daily_sales())
analyzer.plot_sales_trend()
analyzer.plot_sales_per_product()
