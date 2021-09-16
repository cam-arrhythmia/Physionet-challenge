import pandas as pd
import os

ref_df = pd.read_csv('data/validation/REFERENCE.csv')

def get_class_directory(Class):
    if Class == "N":
        return "normal"
    elif Class == "A":
        return "af"
    elif Class == "O":
        return "other"
    elif Class == "~":
        return "noisy"
    else:
        raise "invalid class"

for index, row in ref_df.iterrows():
    for ext in ['mat', 'hea']:
        curr_file = f"data/validation/{row['File']}.{ext}"
        if os.path.isfile(curr_file):
            os.replace(curr_file, f"data/validation/{get_class_directory(row['Class'])}/{row['File']}.{ext}")
