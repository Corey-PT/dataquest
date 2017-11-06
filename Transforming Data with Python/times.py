import read
from dateutil.parser import parse

df = read.load_data()

def extract_hour(x):
    t = parse(x)
    return t.hour

df["hour"] = df["submission_time"].apply(extract_hour)
num_hour = df["hour"].value_counts()

print(num_hour)