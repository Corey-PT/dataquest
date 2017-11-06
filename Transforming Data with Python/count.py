import read
from collections import Counter

df = read.load_data()

string = ""
for w in df["headline"]:
    string = string + " " + str(w)

str_list = string.lower().split()
print(Counter(str_list).most_common(100))