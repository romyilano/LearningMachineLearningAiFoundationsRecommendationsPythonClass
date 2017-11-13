import pandas
import webbrowser
import os

# Read the csv file from metacritic into a data table using Pandas
# the index_col uses the director_id column as the identifier column
data_table = pandas.read_csv("directing_chicks.csv", index_col="director_id")

# create a webby page to view the data
html_code = data_table.to_html()

# save the html to a website file
with open("director_list.html", "w") as f:
    f.write(html_code)

# open the webby page inside our web browser
full_filename = os.path.abspath("director_list.html")
webbrowser.open("file://{}".format(full_filename))