import pandas
import webbrowser
import os

# be reading this csv stuff and then you're like
# DUDE. I want the identifier to be the director id dude
data_table = pandas.read_csv("chick_directors.csv", index_col="director_id")

# anything to avoid excel formulas
html = data_table.to_html()

# save the html to a temporary file
with open("chick_list.html", "w") as tempie_file:
    tempie_file.write(html)

# open the web page in our web browser this is so cool
full_filename = os.path.abspath("chick_list.html")
webbrowser.open("file://{}".format(full_filename))