import pandas
import webbrowser
import os

# Read the csv file from metacritic into a data table using Pandas
data_table = pandas.read_csv("directing_chicks.csv", index_col="")