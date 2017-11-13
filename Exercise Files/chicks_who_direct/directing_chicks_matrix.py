import pandas as pd
import numpy as np
import os
import webbrowser

# read dataset into a data table using pandas
dataset = pd.read_csv("directing_chicks.csv")

# create a web page view of the data for easy viewing
html = dataset[0:50].to_html()

# save the hacky hack to a tempie temp file
with open("matrix_chicks.html", "w") as filie_file:
    filie_file.write(html)

# open the webpage in a browser
full_filename = os.path.abspath("matrix_chicks.html")
webbrowser.open("file://{}".format(full_filename))