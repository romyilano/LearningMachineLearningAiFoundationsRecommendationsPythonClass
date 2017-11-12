import pandas
import webbrowser
import os

# read dataset into a data table because it is more fun than a spreadsheet
data_table = pandas.read_csv("directors_who_happen_to_be_CHICKS.csv")

# create a webpage free of css
html = data_table[0:25].to_html()

# save the table to a TEMP file
with open("films.html", "w") as filie_file:
    filie_file.write(html)

# open the web page in our web browser DUDE
full_filename = os.path.abspath("films.html")
webbrowser.open("file://{}".format(full_filename))