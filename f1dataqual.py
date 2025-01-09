#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import csv

# Read a CSV file into df
f1results = pd.read_csv('/users/results.csv')

print(f1results)


# In[15]:


from ydata_profiling import ProfileReport


# In[36]:


import pandas as pd
from ydata_profiling import ProfileReport
import webbrowser
import os

# Generate the profiling report
f1profile = ProfileReport(f1results, title="F1 Data Profiling Report")


# Save the report as an HTML file
file_path = "data_profiling_report.html"
f1profile.to_file(file_path)

# Open the report in the default web browser
webbrowser.open(f"file://{os.path.abspath(file_path)}")


# In[ ]:




