import pandas as pd
import os
import json
from datetime import datetime
#import tqdm
import csv

directory = "/home/thunderpurtz/Desktop/MessengerAnalysis/JessMessengerAnalysis/jessicagiang_ejka7cjioq/"
directoryMac = "/Users/Thunderpurtz/Desktop/CSPROJECTS/MessengerDataAnalysis/jessicagiang_ejka7cjioq/"

# for filename in os.listdir(directoryMac):
#     if filename.endswith(".json"):
#         f = open(directoryMac + filename)
#         data = json.load(f)
#         for message in data["messages"]:
#             try:
#                 date = datetime.fromtimestamp(message["timestamp_ms"] / 1000).strftime("%Y-%m-%d %H:%M:%S")
#                 sender = message["sender_name"]
#                 content = message["content"]
#                 with open("output.csv", 'a') as csv_file:
#                     writer = csv.writer(csv_file)
#                     writer.writerow([date,sender,content])

#             except KeyError:
#                 pass

# df = pd.read_csv('output.csv')
# print(df.head())


#hist = df.hist(column=[''])
