import csv
from collections import defaultdict
import operator

r = open("AviationData.txt")
aviation_data = r.readlines()
aviation_list = [i.split(" | ") for i in aviation_data]
lax_code = [i for i in aviation_list if "LAX94LA336" in i]
print (lax_code)

# 1. Above algorithm took exponential time (loops through each row first and then each column)

lax_lines = [x for x in open("AviationData.txt", "r") if "LAX94LA336" in x]
print(lax_lines)

# 2. Above searches each row first to see if string LAX94LA336 is present

headers = aviation_data[0].split(" | ")
aviation_dict_list = [dict(zip(headers, row.split(" | "))) for row in aviation_data[1:]]
lax_dict = [row for row in aviation_dict_list if "LAX94LA336" in row.values()]
print (lax_dict)

# 3. Easier to search through a list of dictionaries due to clear key:value pairs

state_accidents = defaultdict(int)
for row in aviation_dict_list:
    if row["Country"] == "United States" and ", " in row["Location"]:
        state = row["Location"].split(", ")[1]
        state_accidents[state] += 1
state_accidents = dict(state_accidents)
soted_state_accidents = sorted(state_accidents.items(), key=operator.itemgetter(1), reverse=True)

# 4. Highest accident state is California

monthly_injuries = defaultdict(lambda: [0,0])
for row in aviation_dict_list:
    month = row["Event Date"].split("/")[0]
    for i, v in enumerate(['Total Fatal Injuries', 'Total Serious Injuries']):
        if row[v] != '':
            monthly_injuries[month][i] += int(row[v])
        else:
            monthly_injuries[month][i] += 0
print (monthly_injuries) 

# 5. Fatalities and injuries by month