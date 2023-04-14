#!/usr/bin/env python
# coding: utf-8

# ## Amazon Sales Data for 2019 (Project Completed in 2021) ##

# In[1]:


# import necessary libraries to be used.
import pandas as pd


# In[2]:


# read in 2019 sales data set.

jan_2019 = pd.read_csv(r"****\Sales Project\Sales Dataset\Sales_January_2019.csv")
feb_2019 = pd.read_csv(r"****\Sales Project\Sales Dataset\Sales_February_2019.csv")
mar_2019 = pd.read_csv(r"****\Sales Project\Sales Dataset\Sales_March_2019.csv")
apr_2019 = pd.read_csv(r"****\Sales Project\Sales Dataset\Sales_April_2019.csv")
may_2019 = pd.read_csv(r"****\Sales Project\Sales Dataset\Sales_May_2019.csv")
jun_2019 = pd.read_csv(r"****\Sales Project\Sales Dataset\Sales_June_2019.csv")
jul_2019 = pd.read_csv(r"****\Sales Project\Sales Dataset\Sales_July_2019.csv")
aug_2019 = pd.read_csv(r"****\Sales Project\Sales Dataset\Sales_August_2019.csv")
sep_2019 = pd.read_csv(r"****\Sales Project\Sales Dataset\Sales_September_2019.csv")
oct_2019 = pd.read_csv(r"****\Sales Project\Sales Dataset\Sales_October_2019.csv")
nov_2019 = pd.read_csv(r"****\Sales Project\Sales Dataset\Sales_November_2019.csv")
dec_2019 = pd.read_csv(r"****\Sales Project\Sales Dataset\Sales_December_2019.csv")


# In[3]:


# take a quick glimpse of a data set
jan_2019.head()


# In[4]:


# Create a list of the sales data frames
dflist = [jan_2019, feb_2019 ,mar_2019, apr_2019, may_2019,
          jun_2019, jul_2019, aug_2019, sep_2019, oct_2019, 
          nov_2019, dec_2019]


# In[5]:


# create a loop to check for consistent data types in each data frame.
# enumerate creates a counter tuple with the dflist. EXAMPLE: (0, jan_2019)

for i, df in enumerate(dflist):
    print(dflist[i].dtypes)


# In[6]:


# Check to see how many rows in total exist

sum_rows=0
for i, df in enumerate(dflist):
    sum_rows += dflist[i].shape[0]
    print(dflist[i].shape)
print("\n" + "Total rows of sales data is: " + str(sum_rows))


# In[7]:


# Concatenate vertically all the data dataframes to create a 
# Master Sales data of 2019.

sales_2019 = pd.concat([jan_2021, feb_2021, mar_2021, apr_2021,
         may_2021, jun_2021, jul_2021, aug_2021,
         sep_2021, oct_2021, nov_2021, dec_2021])


# In[8]:


# Check if data sets concatentated correctely

sales_2019.shape


# In[9]:


# Clear leading and trailing whitespace from values

sales_2021["Order ID"].str.strip()
sales_2021["Product"].str.strip()
sales_2021["Quantity Ordered"].str.strip()
sales_2021["Price Each"].str.strip()
sales_2021["Order Date"].str.strip()
sales_2021["Purchase Address"].str.strip()


# In[10]:


# Check how many missing values there are in each column

sales_2019.isna().sum()


# In[11]:


# Drop rows with missing values

sales_2019.dropna(inplace=True)


# In[12]:


# verify that missing values were removed

sales_2019.isna().sum()


# In[13]:


# check for duplicates

sales_2019.duplicated().value_counts()


# In[14]:


# remove duplicate rows from the data set

sales_2019 = sales_2019.drop_duplicates()


# In[15]:


# verify duplicates have been dropped

sales_2019.duplicated().value_counts()


# In[16]:


# observe the unique values of Price Each

sales_2019['Price Each'].unique()


# In[17]:


# Check how many rows are affect with values ending with only .0

sales_2019["Price Each"].str.endswith(".0").sum()


# In[18]:


# Check how many rows end with a value of .00

sales_2019["Price Each"].str.endswith(".00").sum()


# In[19]:


# check how many rows ends with a value of 0

sales_2019["Price Each"].str.endswith("0").sum()


# In[20]:


# Remove values in "Price Each" column that ends with .0

sales_2019["Price Each"].replace(r"\.0$","", inplace=True, regex=True)


# In[21]:


# Replace values in "Price Each" column that ends with 0 and add 0.00

sales_2019["Price Each"].replace(r"0$", "0.00", inplace=True, regex=True)


# In[22]:


# Verify that the changes were accurately completed

print(sales_2019["Price Each"].str.endswith(".0").sum())
print(sales_2019["Price Each"].str.endswith("0").sum())
print(sales_2019["Price Each"].str.endswith(".00").sum())


# In[23]:


# Check the Price Each column to make sure all values end with 2 decimal places

sales_2019["Price Each"].unique()


# In[24]:


# Check data set to make sure no data was lost during modifications

print(sales_2019.shape)
sales_2019


# In[25]:


# Reorder columns

sales_2019 = sales_2019[['Order ID', 'Product', 'Quantity Ordered', 'Price Each', 'Order Date', 'Purchase Address']]


# In[26]:


# Split Current Address Values into 3 new Columns

sales_2019[['Address', 'City', 'State/Zip']] = sales_2021['Purchase Address'].str.split(",", expand=True)


# In[27]:


# Clear whitespace from "State/Zip" column

sales_2019['State/Zip'].str.strip()


# In[28]:


# Create new columns 3 State/Zip column

sales_2019[['blank','State', 'Zip Code']] = sales_2019['State/Zip'].str.split(" ", expand=True)


# In[29]:


# Drop any unneeded columns

sales_2019 = sales_2019.drop(['Address', 'State/Zip', 'blank'], axis=1)


# In[30]:


# Check Changes of adjustments to new columns

sales_2019


# In[31]:


sales_2019


# In[32]:


# Convert Order Date column to datetime datatype

sales_2019['Order Date'] = pd.to_datetime(sales_2019['Order Date'], errors='coerce')


# In[33]:


# Convert Order Date column to type String

sales_2019 = sales_2019.astype({"Order Date": "string"})


# In[35]:


# Convert Order Date column to datetime datatype

sales_2019['Order Date'] = pd.to_datetime(sales_2019['Order Date'], errors='coerce')


# In[36]:


# Check adjustments to Order Date column

sales_2019


# In[37]:


# Remove row where error value found in Order ID column

sales_2019.drop(sales_2019[sales_2019["Order ID"] == "Order ID"].index, inplace=True)


# In[38]:


# Check if error value was correctly removed.

sales_2019[sales_2019['Quantity Ordered'].str.contains("Quantity")]


# In[39]:


# Check for any errors in Product columns

sales_2019['Product'].value_counts()


# In[40]:


# Check for any errors in Quantity Ordered Column

sales_2019['Quantity Ordered'].value_counts()


# In[41]:


# Check for any errors in Price Each Column


sales_2019['Price Each'].value_counts()


# In[42]:


# Check for any errors in City Column


sales_2019['City'].value_counts()


# In[43]:


# Check for any errors in State Column


sales_2019['State'].value_counts()


# In[44]:


# Check for any errors in Zip Code Column


sales_2019['Zip Code'].value_counts()


# In[45]:


# Change data types of all columns through a dictionary paramenter pass.

sales_2019 = sales_2019.astype({"Order ID": "string", "Product": "string", "Quantity Ordered": "int32",
                               "Price Each": "float64", "Purchase Address": "string", "City":"string",
                                "State":"string", "Zip Code": "string"})


# In[46]:


# Check accuracy of data type adjustments.

sales_2019.dtypes


# In[47]:


# Final check on data set.

sales_2019.head(10)


# In[48]:


# save a copy of the sales 2021 data set as .csv

sales_2019.to_csv(r"C:\Users\yanri\OneDrive\Desktop\Sales Project\Amazon_Sales_2019.csv", encoding='utf-8', index=False)


# In[49]:


## This is a list of the changes made.
## Changelog

# Concatentate Monthly Datasets into one Year dataset
    # Calculate total rows and columns that exist from all data sets
    # Concatentate datasets and then compare rows/columns to check accuracy of concat.
    
# Clean data set.
    # Clear whitespace from values
    # Check how many missing values
    # Check for duplicates
    # Check accuracy of column values
        # Price Each column has inconsistent values. Make changes.
    # Separate Purchase Address into multiple new columns
        # Create new Pruchase Address column
        # Create new City column
        # Create new State column
        # Create new Zip Code column
        
# Change columns to be accurate data types
    # Order ID - String
    # Product ID - String
    # Quantity Ordered - Integer
        # Quantity Order that had a bad value existed: Removed*
    # Price Each - Float
    # Order Date - DateTime
    # Purchase Address - String
    # City - String
    # State - String
    # Zip Code - String
    
# Anything else?

