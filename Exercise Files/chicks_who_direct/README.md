# Metacritic table

* [Metacritic: Ranked - the Best Women Film Directors](http://www.metacritic.com/feature/best-women-film-directors-and-movies)

	Admittedly, we shouldn't have to publish this article. But even in a year where a woman took home the Academy Award for best director (for the first time), female filmmakers still aren't getting the same recognition or opportunities that male directors do.

# HTML

the webbrowser plug-in creates a really nice website. 

* [Director website](director_list.html)

```
import pandas
import webbrowser
import os

# Read the dataset into a data table using Pandas
data_table = pandas.read_csv("movies.csv", index_col="movie_id")

# Create a web page view of the data for easy viewing
html = data_table.to_html()

# Save the html to a temporary file
with open("movie_list.html", "w") as f:
    f.write(html)

# Open the web page in our web browser
full_filename = os.path.abspath("movie_list.html")
webbrowser.open("file://{}".format(full_filename))
``` 
