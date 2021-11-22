import pandas as pd 
import os
import json
from datetime import datetime
import tqdm

directory = "/home/thunderpurtz/Desktop/MessengerAnalysis/JessMessengerAnalysis/jessicagiang_ejka7cjioq/"

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        f = open(directory + filename)
        data = json.load(f)
        for message in data["messages"]:
            print(message)
