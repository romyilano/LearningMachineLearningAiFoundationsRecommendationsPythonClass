import pandas as pd
import numpy as np
import os
import webbrowser

# read dataset into a data table using pandas
hacked_dataset = pd.read_csv("movie_ratings_data_set_COPY.csv")

# create a web page view of the data for easy viewing
hacked_html = hacked_dataset[0:100].to_html()

# save the hacky hack to a tempie temp filie file
with open("hacked_data.html", "w") as filie_file:
    filie_file.write(hacked_html)

# open the webbie page in the browser browser
full_filename = os.path.abspath("hacked_data.html")
webbrowser.open("file://{}".format(full_filename))