import sys 
sys.path.insert(0,'/')

from data import load_dataset_module as loader
from statistics import statistics_module as stats


data = loader("./data/data.csv")
genre_data = loader("./data/data_genres.csv")

# Introduction
# print("Hello there!")
# print("My name is Phuad, Welcom to my PCP assignment demonstration")
# print("We are going to analyze a musical dataset by performing a number of stastical equations.")
print("What is your name ¿")
name = input()

print(f"Hello, {name}!")
analyse= input("What would you like to do? (Options: '1. analyze', '0. quit')")

if analyse == '1':
    print("Let's start with some basic statistics on the dataset.")
    option = input("What would you like to calculate? \n Pick an options \n \n------------------------------------------------------\n 1: Mode \t 2: Maximum Value  \n 3: Average \t 4: Minimum Value \n 5: Variance \t 6: Standard Deviation  \n------------------------------------------------------\n:")
    parameter = input("Which Feauture would you like to analyze? \n Pick an options \n \n------------------------------------------------------\n 1: Valence \t 2: Energy \n 3: Danceability \t 4: Loudness \n 5: Acousticness \t 6: Instrumentalness \n 7: Liveness \t 8: Tempo \n 9: Duration \t 10: Time signature \n------------------------------------------------------\n \n:")


    print(option, parameter)
    result = stats(data, parameter, option)
    print(f"The {option} of {parameter} is {result}")

print(data[132541])
# print(genre_data[0])