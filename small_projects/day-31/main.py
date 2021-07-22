import re
import pandas as pd

with open("frequency_words_from_TV.txt", "r") as data_file:
    data = data_file.read()

temp = re.sub('[^a-zA-Z]+', ' ', data)

temp1 = temp.split(" ")
result = [element for element in temp1 if len(element) != 0]

df = pd.DataFrame(result)
df.to_csv("2000_frequency_words.csv")
