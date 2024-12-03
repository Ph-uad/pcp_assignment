
from data_module import load_dataset_module as loader
# from data_module import statistics_module as statistics


data = loader("./dataset/data.csv")
genre_data = loader("./dataset/data_genres.csv")
print(data[0])
print(genre_data[0])