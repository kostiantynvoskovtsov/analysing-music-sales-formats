#import all the libraries needed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display

#check if data loaded correctly
def load_and_check(sales_formats):
    if sales_formats.shape[0]!=1058:
        print('Houston, we have problems!')
    else:
        print('All hunky dory')
sales_formats = pd.read_csv('https://drive.google.com/uc?id=1cVRNNx_HR3ahuX1TBf6UkYAoBU-Gf8IZ&export=download')
load_and_check(sales_formats)

#set first column as index and get rid of redundant one
sales_formats.index = sales_formats['index']
sales_formats.drop(columns = ['index'], inplace=True)

#calculate format by sale
average_format = sales_formats.groupby('Format')['Revenue'].mean().sort_values(ascending=False)

# Display sales_sorted without scientific notation
pd.set_option('display.float_format', lambda x: '%.0f' % x)

# Plot the average revenue per format
plt.figure(figsize=(20,12))
plt.bar(average_format.index, average_format.values)
plt.ylabel('Revenue, in billion')
plt.xlabel('Format')
plt.title('Average Revenue per Format')
plt.xticks(rotation=55)
plt.show()

display(average_format.to_string())
