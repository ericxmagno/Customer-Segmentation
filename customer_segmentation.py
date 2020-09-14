#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

from bokeh.plotting import figure, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral
from bokeh.palettes import Spectral6, Magma, Inferno
from bokeh.themes import built_in_themes
from bokeh.io import curdoc

from datetime import date, timedelta
from PIL import Image


# In[2]:


st.title('Customer Segmentation')


# In[6]:


def get_contributors():
    st.subheader('Contributors')
    st.write('-----------------------------')
    st.markdown("<ul>"                "<li>Albert Yumol</li>"                "<li>Alphonso Balagtas</li>"                "<li>Danilo Gubaton</li>"                "<li>Elissa Mae Cabal</li>"                "<li>Emerson Chua</li>"                "<li>Franz Taborlupa</li>"                "<li>Gabriel Ong</li>"                "<li>Janina Reyes</li>"                "<li>John Barrion</li>"                "<li>Joleil Villena</li>"                "<li>Jonas Beltran</li>"                "<li>Justine Guino</li>"                "<li>Justine Brian Santoalla</li>"                "<li>Kemp Po</li>"                "<li>Kenrick Nocom</li>"                "<li>Paul Allen Chavit</li>"                "<li>Rai Ferrer</li>"                "<li>Rhey Ann Magcalas</li>"                "<li>Roberto Banadera</li>"                "<li>Ruth Ann Cabria</li>"                "<li>William Revilla</li>"                "</ul>", 
                unsafe_allow_html=True)


# In[ ]:


## Side Bar Information
image = Image.open('eskwelabs.png')
st.sidebar.image(image, caption='', use_column_width=True)
st.sidebar.markdown("<h1 style='text-align: center;margin-bottom:50px'>DS Cohort V</h1>", unsafe_allow_html=True)


add_selectbox = st.sidebar.radio(
    "",
    ("Introduction and Problem Statement", "Data Set", "Outline", "List of Tools", "Data Cleaning", 
     "Exploratory Data Analysis", "RFM Model", "K-Means Clustering and Validation", "Market Basket Analysis", "Contributors")
)


# In[ ]:


if add_selectbox == 'Introduction and Problem Statement':
    st.write('')
    st.subheader('Introduction')
    st.write('-----------------------------------------------------------------------') 
    st.write('An e-commerce company which sells souvenirs wants to segment its customers and determine marketing '             'strategies according to these segments')
    st.write('For this purpose, we will define the behavior of customers and we will put the customers into same '             'groups who exhibit common behaviors and then we will try to develop sales and marketing techniques '             'specific to these groups:')
    st.markdown('<b style="margin-left:7%">PROFIT </b> (to increase) = <b>REVENUE</b> (to increase) - <b>COST</b> (to decrease)'
                , unsafe_allow_html=True)
    st.write('However, there are a lot of things that the company does not know with regard to its own business. '             'First, the company does not know who its customers are. Some of the questions, but not limited to, '             'are: what countries are they from, what do they tend to buy given the choices, and, what day of the '             'week they usually transact? Next problem is the company has little idea what product sells versus what '             'does not sell on a given quarter or season.')


# In[ ]:


elif add_selectbox == 'Data Set':
    st.write('')
    st.subheader('Data Set')
    st.write('-----------------------------------------------------------------------') 
    st.write('This is a transnational data set which contains all the transactions occurring between 01/12/2010 '             'and 09/12/2011 for a UK-based and registered non-store online retail. &nbsp;The company mainly sells '             'unique all-occasion gifts. Many customers of the company are wholesalers.')
    
    st.write('')
    st.markdown('<b>Sample Data Set:</b>', unsafe_allow_html=True)
    dataset_sample = {
                      'InvoiceNo': ['536365', '536365', '536365', '536365', '536365'], 
                      'StockCode': ['85123A', '71053', '84406B', '84029G', '84029E'],
                      'Description': ['WHITE HANGING HEART T-LIGHT HOLDER', 'WHITE METAL LANTERN', 
                                      'CREAM CUPID HEARTS COAT HANGER', 'KNITTED UNION FLAG HOT WATER BOTTLE',
                                     'RED WOOLLY HOTTIE WHITE HEART'],
                      'Quantity': [6, 6, 8, 6, 6],
                      'InvoiceDate': ['2010-12-01 08:26:00', '2010-12-01 08:26:00', '2010-12-01 08:26:00',
                                     '2010-12-01 08:26:00', '2010-12-01 08:26:00'],
                      'UnitPrice': ['2.55', '3,39', '2,75', '3,39', '3,39'],
                      'CustomerID': ['536365', '536365', '536365', '536365', '536365'],
                      'Country': ['United Kingdom', 'United Kingdom','United Kingdom','United Kingdom','United Kingdom'],
                     }
    
    st.table(dataset_sample)
    
    st.markdown('<b>Data Dimensions:</b> Rows: 541909 Columns: 8', unsafe_allow_html=True)
    
    st.markdown('<b>Data Description:</b>', unsafe_allow_html=True)
    data_details = {
        'columns': ['Invoice number', 'StockCode', 'Description', 'Quantity', 'Invoice Date and Time',
                    'Unit Price', 'Customer Number', 'Country'],
        'Description': ['A unique number that is assigned to each invoice', 
                        'Unique number assigned to each distinct product. ', 
                        'Product name ', 
                        'The quantities of each product per transaction',
                        'The day and time when each transaction was generated. ', 
                        'Product price per unit ', 
                        'A unique number assigned to each customer ', 
                        'The name of the country where each customer resides. ']
    }
    
    st.table(pd.DataFrame(data_details).set_index('columns'))


# In[ ]:


elif add_selectbox == 'Outline':
    st.write('')
    st.subheader('Outline')
    st.write('-----------------------------------------------------------------------') 
    outline = """
    <div style="margin-left:10%;">
           1. Data Set <br>
           2. Data Cleaning <br>
           3. Exploratory Data Analysis <br>
           4. Feature Engineering  <br>
           5. Goal: Customer Segmentation <br>
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A. RFM & Validation <br>
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B. K Means <br>
           6. Deployment + Demo <br>
           7. Conclusion <br>
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A. Results <br>
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B. Market Basket Analysis <br>
    </div>
    """
    st.write(outline, unsafe_allow_html=True)


# In[ ]:


elif add_selectbox == 'List of Tools':
    st.write('')
    st.subheader('List of Tools')
    st.write('-----------------------------------------------------------------------') 
    image = Image.open('logo/jupyter.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/pandas.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/heroku.jpg').convert('RGB')
    st.image(image, caption='', width=150, height=50)
    image = Image.open('logo/streamlit.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/bokeh.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/github.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/regex.jpeg').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/scipy.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/seaborn.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/matplotlib.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/numpy.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)


# In[ ]:


elif add_selectbox == 'Data Cleaning':
    st.write('')
    st.subheader('Data Cleaning')
    st.write('-----------------------------------------------------------------------') 
    st.write('1. Check Null Values Per Column:')
    
    
    source1 = ColumnDataSource(data=dict(column_values=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 
                                                        'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'], 
                                         column_null_count=[0, 0, 0, 100, 0, 0, 10000, 0], 
                                         color=['#35193e', '#35193e', '#701f57','#701f57', '#ad1759', '#e13342', 
                                                '#f37651', '#f6b48f']))
    
    null_plot= figure(x_range=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 
                                                        'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'], plot_height=600, title='Column Null Counts')
    
    null_plot.vbar(x='column_values', top='column_null_count', width=0.5, color='color', 
                   legend_field='column_values', source=source1)
    
    null_plot.xaxis.axis_label = 'Columns'
    null_plot.yaxis.axis_label = 'Null Counts'
    null_plot.xaxis.major_label_orientation = 1.2
    st.bokeh_chart(null_plot)
    
    st.write('Conclusion: We Need To Remove Null Values from CustomerID Column')    

    
    source1 = ColumnDataSource(data=dict(column_values=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 
                                                        'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'], 
                                         column_null_count=[406829, 406829, 406829, 406829, 406829, 406829, 406829, 406829], 
                                         color=['#35193e', '#35193e', '#701f57','#701f57', '#ad1759', '#e13342', 
                                                '#f37651', '#f6b48f']))
    clean_p= figure(x_range=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 
                             'CustomerID', 'Country'], plot_height=600, title='Clean Data Count')
    clean_p.vbar(x='column_values', top='column_null_count', width=0.5, color='color', legend_field='column_values', 
           source=source1)
    clean_p.xaxis.axis_label = 'Columns'
    clean_p.yaxis.axis_label = 'Null Counts'
    clean_p.xaxis.major_label_orientation = 1.2
    clean_p.legend.visible = False
    st.bokeh_chart(clean_p)
    
    
    st.write('2. Checking Float Field Minimum And Maximum Values')
    number_data = {
        'Column':  ['Quantity', 'UnitPrice'],
        'Minimum': [-80995, -11062.06],
        'Maximum': [80995, 38970.0]
    }
    
    st.write('Conclusion: We Need To Remove Negative Values from Quantity Column')
    
    st.write('3. Creating Total Amount Column: Quantity * UnitPrice')
    st.write('4. We Need to Convert Invoice Date to Datetime Field')
    st.write('New Data Dimensions: Rows:397924, Columns: 9')
    
    
    dataset_sample = {
                      'InvoiceNo': ['536365', '536365', '536365', '536365', '536365'], 
                      'StockCode': ['85123A', '71053', '84406B', '84029G', '84029E'],
                      'Description': ['WHITE HANGING HEART T-LIGHT HOLDER', 'WHITE METAL LANTERN', 
                                      'CREAM CUPID HEARTS COAT HANGER', 'KNITTED UNION FLAG HOT WATER BOTTLE',
                                     'RED WOOLLY HOTTIE WHITE HEART'],
                      'Quantity': [6, 6, 8, 6, 6],
                      'InvoiceDate': ['2010-12-01 08:26:00', '2010-12-01 08:26:00', '2010-12-01 08:26:00',
                                     '2010-12-01 08:26:00', '2010-12-01 08:26:00'],
                      'UnitPrice': ['2.55', '3,39', '2,75', '3.39', '3,39'],
                      'CustomerID': ['536365', '536365', '536365', '536365', '536365'],
                      'Country': ['United Kingdom', 'United Kingdom','United Kingdom','United Kingdom','United Kingdom'],
                      'Total Amount': ['15.3', '20.34', '22', '20.34', '20.34']
                    }
    
    st.table(dataset_sample)


# In[ ]:


elif add_selectbox == 'Exploratory Data Analysis':
    st.write('')
    st.subheader('Exploratory Data Analysis')
    st.write('-----------------------------------------------------------------------') 

    top_10_country_purchase_source = ColumnDataSource(data=dict(
        column_values=['United Kingdom', 'Netherlands', 'EIRE', 'Germany', 'France','Australia', 'Spain', 
                       'Switzerland', 'Belgium', 'Sweden'],
                                        column_null_count=[7308391.55400306,  285446.34,265545.9,228867.14 ,  
                                                           209024.05,  138521.31, 61577.11, 56443.95, 41196.34,
                                                           38378.33], 
                                         color=['#35193e','#35193e','#701f57','#701f57',
                                                '#ad1759','#ad1759','#ad1759', '#e13342', '#f37651', '#f6b48f']))
    top_10_country_purchase = figure(x_range=['United Kingdom', 'Netherlands', 'EIRE', 'Germany', 'France',
                                              'Australia', 'Spain', 'Switzerland', 'Belgium', 'Sweden'], plot_height=500, plot_width=600, 
                                title='Top 10 Highest Purchasing Countries')
    
    top_10_country_purchase.vbar(x='column_values', top='column_null_count', width=0.5,
                            legend_field='column_values', color='color', source=top_10_country_purchase_source)
                                         
                                         
    top_10_country_purchase.xaxis.axis_label = 'Countries'
    top_10_country_purchase.yaxis.axis_label = 'Total Purchases'
    top_10_country_purchase.xaxis.major_label_orientation = 1.2
    st.bokeh_chart(top_10_country_purchase)
    
    st.subheader('UK Vs Other Countries')
    st.write('-----------------------------------------------------------------------')
    uk_purchases_day_source = ColumnDataSource(data=dict(column_values=['6am','7am','8am','9am','10am','11am','12pm',
                                                                        '1pm','2pm','3pm', '4pm','5pm','6pm','7pm',
                                                                        '8pm'], 
                                        column_null_count=[0.006007, 0.138163, 2.715204, 7.178471, 11.617709,
                                                          12.482730, 17.216315, 14.308884, 12.218418, 11.131135,
                                                          6.139244, 2.967502, 0.949120, 0.822971, 0.108128], 
                                         color=['#35193e','#35193e','#35193e', '#701f57','#701f57','#701f57',
                                                '#ad1759','#ad1759','#ad1759', '#e13342', '#e13342', '#e13342',
                                                '#f37651','#f37651','#f37651', '#f6b48f',  '#f6b48f']))
    uk_purchases_day = figure(x_range=['6am','7am','8am','9am','10am','11am','12pm',
                                       '1pm','2pm','3pm', '4pm','5pm','6pm','7pm','8pm'], plot_height=500, 
                              plot_width=600, title='No of purchases on certain times within the day on UK')
    uk_purchases_day.vbar(x='column_values', top='column_null_count', width=0.5,
                            legend_field='column_values', color='color', source=uk_purchases_day_source)
                                         
                                         
    uk_purchases_day.xaxis.axis_label = 'Hour'
    uk_purchases_day.yaxis.axis_label = 'Percentage of Purchases'
    uk_purchases_day.xaxis.major_label_orientation = 1.2
    st.bokeh_chart(uk_purchases_day)
    
    non_uk_purchases_day_source = ColumnDataSource(data=dict(column_values=['7am','8am','9am','10am','11am','12pm',
                                                                        '1pm','2pm','3pm', '4pm','5pm','6pm','7pm'], 
                                        column_null_count=[0.318134, 5.461294, 10.498409, 15.482503, 10.551432,
                                                          13.997879, 13.467656, 12.725345, 9.756098, 4.135737, 
                                                          2.651113, 0.583245, 0.37115], 
                                         color=['#35193e','#35193e','#35193e', '#701f57','#701f57','#701f57',
                                                '#ad1759','#ad1759','#ad1759', '#e13342', '#e13342', '#e13342',
                                                '#f37651','#f37651','#f37651', '#f6b48f',  '#f6b48f']))
    non_uk_purchases_day = figure(x_range=['7am','8am','9am','10am','11am','12pm','1pm','2pm','3pm', 
                                           '4pm','5pm','6pm','7pm'], plot_height=500, plot_width=600, 
                                title='No of purchases on certain times within the day on Other Countries')
    
    non_uk_purchases_day.vbar(x='column_values', top='column_null_count', width=0.5,
                            legend_field='column_values', color='color', source=non_uk_purchases_day_source)
                                         
                                         
    non_uk_purchases_day.xaxis.axis_label = 'Hour'
    non_uk_purchases_day.yaxis.axis_label = 'Percentage of Purchases'
    non_uk_purchases_day.xaxis.major_label_orientation = 1.2
    st.bokeh_chart(non_uk_purchases_day)     

    st.write('Conclusion: People buy more stuff at 12pm (UK), 10am(Other Countries) ')
    st.write('-----------------------------------------------------------------------')
    
    uk_purchases_week_source = ColumnDataSource(data=dict(column_values=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sun'], 
                                        column_null_count=[15.336097, 17.342464, 18.567910, 21.619511, 
                                                          14.885565, 12.242446], 
                                         color=['#35193e', '#701f57', '#ad1759', '#e13342', '#f37651', '#f6b48f']))
    uk_purchases_week = figure(x_range=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sun'], plot_height=500, plot_width=600, 
                                title='Percentage of purchases on certain days of the week on UK')
    
    uk_purchases_week.vbar(x='column_values', top='column_null_count', width=0.5,
                            legend_field='column_values', color='color', source=uk_purchases_week_source)
                                            
    uk_purchases_week.xaxis.axis_label = 'Day'
    uk_purchases_week.yaxis.axis_label = 'Percentage of Purchases'
    uk_purchases_week.xaxis.major_label_orientation = 1.2
    st.bokeh_chart(uk_purchases_week)
    
    nonuk_purchases_week_source = ColumnDataSource(data=dict(column_values=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sun'], 
                                        column_null_count=[16.436903, 15.747614, 19.300106,  22.958643, 18.610817,
                                                          6.945917], 
                                         color=['#35193e', '#701f57', '#ad1759', '#e13342', '#f37651', '#f6b48f']))
    nonuk_purchases_week = figure(x_range=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sun'], plot_height=500, plot_width=600, 
                                title='Percentage of purchases on certain days of the week on other countries')
    
    nonuk_purchases_week.vbar(x='column_values', top='column_null_count', width=0.5,
                            legend_field='column_values', color='color', source=nonuk_purchases_week_source)
                                            
    nonuk_purchases_week.xaxis.axis_label = 'Day'
    nonuk_purchases_week.yaxis.axis_label = 'Percentage of Purchases'
    nonuk_purchases_week.xaxis.major_label_orientation = 1.2
    st.bokeh_chart(nonuk_purchases_week)
    
    st.write('Conclusion: People buy more stuff on Thursdays.')
    st.write('-----------------------------------------------------------------------')
  
    uk_purchases_year_source = ColumnDataSource(data=dict(column_values=['Jan','Feb','Mar','Apr','May','Jun','Jul',
                                                                         'Aug','Sep','Oct','Nov','Dec'], 
                                        column_null_count=[5.250195, 5.382351, 7.070343, 6.355499, 8.427945, 7.502853,
                                                          7.208506, 6.806031,  9.419115, 10.242086, 14.332913, 
                                                          11.996155], 
                                         color=['#35193e', '#701f57', '#ad1759', '#e13342', '#f37651', '#f6b48f']))
    uk_purchases_year = figure(x_range=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], 
                               plot_height=500, plot_width=600, 
                                title='Percentage of purchases within the year on UK')
    
    uk_purchases_year.vbar(x='column_values', top='column_null_count', width=0.5,
                            legend_field='column_values', color='color', source=uk_purchases_year_source)
                                            
    uk_purchases_year.xaxis.axis_label = 'Month'
    uk_purchases_year.yaxis.axis_label = 'Percentage of Purchases'
    uk_purchases_year.xaxis.major_label_orientation = 1.2
    st.bokeh_chart(uk_purchases_year)
    
    nonuk_purchases_year_source = ColumnDataSource(data=dict(column_values=['Jan','Feb','Mar','Apr','May','Jun','Jul',
                                                                         'Aug','Sep','Oct','Nov','Dec'], 
                                        column_null_count=[5.991516, 5.355249, 7.635207, 4.825027, 8.059385, 7.635207,
                                                          6.945917, 7.794274, 9.915164, 11.876988, 14.369035, 9.597031], 
                                         color=['#35193e', '#701f57', '#ad1759', '#e13342', '#f37651', '#f6b48f']))
    nonuk_purchases_year = figure(x_range=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], 
                                  plot_height=500, plot_width=600, 
                                title='Percentage of purchases within the year on other countries')
    
    nonuk_purchases_year.vbar(x='column_values', top='column_null_count', width=0.5,
                            legend_field='column_values', color='color', source=nonuk_purchases_year_source)
                                            
    nonuk_purchases_year.xaxis.axis_label = 'Month'
    nonuk_purchases_year.yaxis.axis_label = 'Percentage of Purchases'
    nonuk_purchases_year.xaxis.major_label_orientation = 1.2
    st.bokeh_chart(nonuk_purchases_year)
    
    st.write('Conclusion: People buy more stuff from September to December')
    st.write('-----------------------------------------------------------------------')
    
    st.subheader('Average Purchase per Continent')
    st.write('-----------------------------------------------------------------------')
    
    purchase_continent_source = ColumnDataSource(data=dict(column_values=['Oceania', 'Asia', 'North America', 
                                                                         'Europe', 'South America', 'Unspecified '], 
                                        column_null_count=[70.982234, 28.070746, 15.821212, 12.756739, 11.125000, 
                                                          7.331967], 
                                         color=['#35193e', '#701f57', '#ad1759', '#e13342', '#f37651', '#f6b48f']))
    purchase_continent = figure(x_range=['Oceania', 'Asia', 'North America', 'Europe', 'South America', 
                                         'Unspecified '], plot_height=500, plot_width=600, 
                                title='Average Quantity Purchase per Continent')
    
    purchase_continent.vbar(x='column_values', top='column_null_count', width=0.5,
                            legend_field='column_values', color='color', source=purchase_continent_source)
                                            
    purchase_continent.xaxis.axis_label = 'Continent'
    purchase_continent.yaxis.axis_label = 'Average Quantity Purchase'
    purchase_continent.xaxis.major_label_orientation = 1.2
    st.bokeh_chart(purchase_continent)
    
    st.write('Oceania is notably purchasing higher quantities of items per transaction compared to the other continents.')
    purchase_continent_average_source = ColumnDataSource(data=dict(column_values=['Oceania', 'Asia', 'South America', 
                                                                                 'Europe', 'North America', 'Africa',
                                                                                 'Unspecified'], 
                                        column_null_count=[117.192310, 53.935596, 35.737500, 21.994580, 21.959909,
                                                          17.584386, 10.930615], 
                                         color=['#35193e', '#701f57', '#ad1759', '#e13342', '#f37651', '#f6b48f']))
    
    purchase_continent_average = figure(x_range=['Oceania', 'Asia', 'South America', 'Europe', 'North America', 'Africa',
                                                 'Unspecified'], plot_height=500, plot_width=600, 
                                title='Average Total Purchases per Continent')
    
    purchase_continent_average.vbar(x='column_values', top='column_null_count', width=0.5,
                            legend_field='column_values', color='color', source=purchase_continent_average_source)
                                            
    purchase_continent_average.xaxis.axis_label = 'Continent'
    purchase_continent_average.yaxis.axis_label = 'Total Purchases'
    purchase_continent_average.xaxis.major_label_orientation = 1.2
    st.bokeh_chart(purchase_continent_average)
    st.write('While N. America buys higher quantities of items than S. America & Africa in general, S. America '             '& Africa actually have a higher total £ value purchase on a per transaction basis.')
    
    st.subheader('Product Metrics per Continent')
    st.write('-----------------------------------------------------------------------')
    
    top10_product_source = ColumnDataSource(data=dict(column_values=['BAG', 'CAKE', 'T-LIGHT', 'WRAP', 'JAR', 'CANDLE',
                                                                    'TISSUE', 'PAPER CRAFT, LITTLE BIRDIE', 'BOTTLE',
                                                                    'DOILY'], 
                                        column_null_count=[502502, 290159, 211065, 162125, 143921, 105471, 101615,
                                                          80995, 63171, 58910], 
                                         color=['#35193e', '#701f57', '#ad1759', '#e13342', '#f37651', '#f6b48f']))
    
    top10_product = figure(x_range=['BAG', 'CAKE', 'T-LIGHT', 'WRAP', 'JAR', 'CANDLE','TISSUE', 
                                    'PAPER CRAFT, LITTLE BIRDIE', 'BOTTLE',
                                    'DOILY'], plot_height=500, plot_width=600, 
                                title='Top 10 Products Categories')
    
    top10_product.vbar(x='column_values', top='column_null_count', width=0.5,
                            legend_field='column_values', color='color', source=top10_product_source)
                                            
    top10_product.xaxis.axis_label = 'Product'
    top10_product.yaxis.axis_label = 'Quantity Purchased'
    top10_product.xaxis.major_label_orientation = 1.2
    top10_product.legend.visible = False
    st.bokeh_chart(top10_product)
    
    
    df_europe_top10_qty_source = ColumnDataSource(data=dict(column_values=['BAG', 'CAKE', 'T-LIGHT', 'WRAP', 'JAR', 'CANDLE',
                                                                    'TISSUE', 'PAPER CRAFT, LITTLE BIRDIE', 'BOTTLE',
                                                                    'DOILY'], 
                                        column_null_count=[494017, 282697, 210052, 156177, 141346, 103008, 99059,
                                                          80995, 62072,  56847], 
                                         color=['#35193e', '#701f57', '#ad1759', '#e13342', '#f37651', '#f6b48f']))
    
    df_europe_top10 = figure(x_range=['BAG', 'CAKE', 'T-LIGHT', 'WRAP', 'JAR', 'CANDLE', 'TISSUE', 'PAPER CRAFT, LITTLE BIRDIE', 'BOTTLE',
                                      'DOILY'], plot_height=500, plot_width=600, 
                                title='Top 10 Product Categories in Europe (QTY)')
    
    df_europe_top10.vbar(x='column_values', top='column_null_count', width=0.5,
                            legend_field='column_values', color='color', source=df_europe_top10_qty_source)
                                            
    df_europe_top10.xaxis.axis_label = 'Product'
    df_europe_top10.yaxis.axis_label = 'Quantity Purchased'
    df_europe_top10.xaxis.major_label_orientation = 1.2
    df_europe_top10.legend.visible = False
    st.bokeh_chart(df_europe_top10)
    
    st.write('Europe’s Top 10 list matches the worldwide Top 10.')
    st.write('Bags are way ahead at #1, followed by Cake and T-Light.')
    
    df_oceania_top10_source = ColumnDataSource(data=dict(column_values=['BAG', 'CAKE', 'WRAP', 'MINI PAINT SET VINTAGE',
                                                                        'JAR', 'RABBIT NIGHT LIGHT',
                                                                    'RED  HARMONICA IN BOX', 'CANDLE', 'CASES', 'DOILY'], 
                                        column_null_count=[5291, 4722, 4412, 2952, 2030, 1884, 1704, 1608, 1536, 1470], 
                                         color=['#35193e', '#701f57', '#ad1759', '#e13342', '#f37651', '#f6b48f']))
    
    df_oceania_top10 = figure(x_range=['BAG', 'CAKE', 'WRAP', 'MINI PAINT SET VINTAGE', 'JAR', 'RABBIT NIGHT LIGHT',
                                       'RED  HARMONICA IN BOX', 'CANDLE', 'CASES', 'DOILY'], plot_height=500, plot_width=600, 
                                title='Top 10 Product Categories in Oceania (QTY)')
    
    df_oceania_top10.vbar(x='column_values', top='column_null_count', width=0.5,
                            legend_field='column_values', color='color', source=df_oceania_top10_source )
                                            
    df_oceania_top10.xaxis.axis_label = 'Product'
    df_oceania_top10.yaxis.axis_label = 'Quantity Purchased'
    df_oceania_top10.xaxis.major_label_orientation = 1.2
    df_oceania_top10.legend.visible = False
    st.bokeh_chart(df_oceania_top10)
    
    st.write('-Oceania also lists Bag as their #1 product category.')
    st.write('Mini Paint Set Vintage and Rabbit Night Light are items which are popular in Oceania and Asia only.')
    
    
    df_asia_top10_qty_source = ColumnDataSource(data=dict(column_values=['RABBIT NIGHT LIGHT', 'BAG', 'CAKE', 'ROUND SNACK BOXES SET OF 4 FRUITS', 'PACK OF 12 TRADITIONAL CRAYONS',
    'TISSUE', 'BUNTING', 'T-LIGHT', 'MINI PAINT SET VINTAGE', 'WRAP']  , 
                                        column_null_count=[3408, 2836, 2130, 1506, 1201, 972, 789, 779, 613, 587], 
                                         color=['#35193e', '#701f57', '#ad1759', '#e13342', '#f37651', '#f6b48f']))
    
    df_asia_top10 = figure(x_range=['RABBIT NIGHT LIGHT', 'BAG', 'CAKE', 'ROUND SNACK BOXES SET OF 4 FRUITS', 'PACK OF 12 TRADITIONAL CRAYONS',
    'TISSUE', 'BUNTING', 'T-LIGHT', 'MINI PAINT SET VINTAGE', 'WRAP'], plot_height=500, plot_width=600, 
                                title='Top 10 Product Categories in Asia (QTY)')
    
    df_asia_top10.vbar(x='column_values', top='column_null_count', width=0.5,
                            legend_field='column_values', color='color', source=df_asia_top10_qty_source)
                                            
    df_asia_top10.xaxis.axis_label = 'Product'
    df_asia_top10.yaxis.axis_label = 'Quantity Purchased'
    df_asia_top10.xaxis.major_label_orientation = 1.2
    df_asia_top10.legend.visible = False
    st.bokeh_chart(df_asia_top10)
    
    st.write('Rabbit Night Lights exceed the popular Bag Category from other continents.')
    st.write('Snack Boxes of Fruits, as well as Crayons, are popular only in Asia.')
    
    
    df_northamerica_top10_qty_source = ColumnDataSource(data=dict(column_values=['RETRO COFFEE MUGS ASSORTED', 
                                                                                'WRAP', 'CAKE', 'CANDLE', 
                                                                                'WORLD WAR 2 GLIDERS ASSTD DESIGNS',
                                                                                'BAG', 'TISSUE', 'JAR', 'DOILY', 
                                                                                 'CASES'], 
                                        column_null_count=[504, 449, 372, 304, 288, 212, 180, 126, 108, 106], 
                                         color=['#35193e', '#701f57', '#ad1759', '#e13342', '#f37651', '#f6b48f']))
    
    df_northamerica_top10 = figure(x_range=['RETRO COFFEE MUGS ASSORTED', 'WRAP', 'CAKE', 'CANDLE', 
                                            'WORLD WAR 2 GLIDERS ASSTD DESIGNS','BAG', 'TISSUE', 'JAR', 'DOILY', 
                                            'CASES'], plot_height=500, plot_width=600, 
                                title='Top 10 Product Categories in North America (QTY)')
    df_northamerica_top10.vbar(x='column_values', top='column_null_count', width=0.5,
                            legend_field='column_values', color='color', source=df_northamerica_top10_qty_source)
                                            
    df_northamerica_top10.xaxis.axis_label = 'Product'
    df_northamerica_top10.yaxis.axis_label = 'Quantity Purchased'
    df_northamerica_top10.xaxis.major_label_orientation = 1.2
    df_northamerica_top10.legend.visible = False
    st.bokeh_chart(df_northamerica_top10)
    
    st.write('Retro Coffee Mugs and World War 2 Gliders are popular items in North America not found in the Top 10 of any other continent.')
    
    
    df_southamerica_top10_qty_source = ColumnDataSource(data=dict(column_values=['SAUCER', 'SMALL HEART FLOWERS HOOK', 
                                            'SET/3 RED GINGHAM ROSE STORAGE BOX', 'SET OF 6 SPICE TINS PANTRY DESIGN',
                                           'SET OF 4 PANTRY JELLY MOULDS', 'DOLLY GIRL LUNCH BOX', 'BAG', 'CAKE',
                                           'CHALKBOARD', 'CLOCK'], 
                                        column_null_count=[72, 24, 24, 24, 24, 24, 20, 16, 12, 12], 
                                         color=['#35193e', '#701f57', '#ad1759', '#e13342', '#f37651', '#f6b48f']))
    
    df_southamerica_top10 = figure(x_range=['SAUCER', 'SMALL HEART FLOWERS HOOK', 
                                            'SET/3 RED GINGHAM ROSE STORAGE BOX', 'SET OF 6 SPICE TINS PANTRY DESIGN',
                                           'SET OF 4 PANTRY JELLY MOULDS', 'DOLLY GIRL LUNCH BOX', 'BAG', 'CAKE',
                                           'CHALKBOARD', 'CLOCK'], plot_height=500, plot_width=600, 
                                title='Top 10 Product Categories in South America (QTY)')
    
    df_southamerica_top10.vbar(x='column_values', top='column_null_count', width=0.5,
                            legend_field='column_values', color='color', source=df_southamerica_top10_qty_source)
                                            
    df_southamerica_top10.xaxis.axis_label = 'Product'
    df_southamerica_top10.yaxis.axis_label = 'Quantity Purchased'
    df_southamerica_top10.xaxis.major_label_orientation = 1.2
    df_southamerica_top10.legend.visible = False
    st.bokeh_chart(df_southamerica_top10)
    
    st.write('Saucer is an extremely popular category in South America.')
    st.write('The other items that make up the Top 10 list in South America are almost all equally tied.')
    
    
    df_africa_top10_qty_source = ColumnDataSource(data=dict(column_values=['BAG', 'DOILY', 'JAR', 'CAKE', 'BUNTING', '4 TRADITIONAL SPINNING TOPS', 'PACK OF 6 BIRDY GIFT TAGS', 
     'BOTTLE', 'SET OF 20 KIDS COOKIE CUTTERS', 'WOODEN BOX OF DOMINOES'], 
                                        column_null_count=[71, 26, 16, 14, 13, 12, 12, 12, 12, 12], 
                                         color=['#35193e', '#701f57', '#ad1759', '#e13342', '#f37651', '#f6b48f']))
    
    df_africa_top10 = figure(x_range=['BAG', 'DOILY', 'JAR', 'CAKE', 'BUNTING', '4 TRADITIONAL SPINNING TOPS', 'PACK OF 6 BIRDY GIFT TAGS', 
     'BOTTLE', 'SET OF 20 KIDS COOKIE CUTTERS', 'WOODEN BOX OF DOMINOES'], plot_height=500, plot_width=600, 
                                title='Top 10 Product Categories in Africa (QTY)')
    
    df_africa_top10.vbar(x='column_values', top='column_null_count', width=0.5,
                            legend_field='column_values', color='color', source=df_africa_top10_qty_source)
                                            
    df_africa_top10.xaxis.axis_label = 'Product'
    df_africa_top10.yaxis.axis_label = 'Quantity Purchased'
    df_africa_top10.xaxis.major_label_orientation = 1.2
    df_africa_top10.legend.visible = False
    st.bokeh_chart(df_africa_top10)
    
    st.write('Bag is the clear winner for Africa.')
    st.write('The other items that make up the Top 10 list in South America are almost all equally tied.')
