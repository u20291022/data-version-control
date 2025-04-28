import random
import re
import os
import csv

FILE_PATH = "data/raw/9.csv"
PREPARED_DIR = "data/prepared"

def save_dataset(data, filename):
    filepath = os.path.join(PREPARED_DIR, filename)
    with open(filepath, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\t')
        for item in data:
            writer.writerow(item)
    print(f"Saved {len(data)} records to {filepath}")

data = []
with open(FILE_PATH, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter='\t')
    for row in csv_reader:
        label = row[0].strip()
        comment = row[1].strip()
        comment_length = row[2].strip()
        data.append([label, comment, comment_length])

random.shuffle(data)

train_size = int(0.7 * len(data))
val_size = int(0.15 * len(data))
test_size = len(data) - train_size - val_size

train_data = data[:train_size]
val_data = data[train_size:train_size + val_size]
test_data = data[train_size + val_size:]

save_dataset(train_data, "train.csv")
save_dataset(val_data, "val.csv")
save_dataset(test_data, "test.csv")
