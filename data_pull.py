# Import necessary libraries
from datasets import load_dataset
import pandas as pd
from sklearn.model_selection import train_test_split
import json
import os
import shutil

# Load the entire amazon_massive_intent dataset
dataset = load_dataset("mteb/amazon_massive_intent")

# Filter for English language samples
train_samples = dataset["train"].filter(lambda x: x["lang"] == "en")

# Select only the required columns
train_samples = train_samples.select_columns(["text", "label_text"])

# Convert to pandas DataFrame
train_df = pd.DataFrame(train_samples)

# Function to remove labels with less than 200 samples and limit each label to 600 samples
def process_labels(df, min_samples=200, max_samples=600):
    label_counts = df["label_text"].value_counts()
    labels_to_keep = label_counts[label_counts >= min_samples].index
    df = df[df["label_text"].isin(labels_to_keep)]

    # Limit each label to max_samples
    balanced_df = pd.DataFrame()
    for label in labels_to_keep:
        label_samples = df[df["label_text"] == label].sample(
            n=min(len(df[df["label_text"] == label]), max_samples), random_state=42
        )
        balanced_df = pd.concat([balanced_df, label_samples])

    return balanced_df

# Process labels in the dataset
train_df = process_labels(train_df)

# Split into train (80%), temp (20%)
train_df, temp_df = train_test_split(
    train_df, test_size=0.2, random_state=42, stratify=train_df["label_text"]
)

# Split temp into validation (10%) and test (10%)
valid_df, test_df = train_test_split(
    temp_df, test_size=0.5, random_state=42, stratify=temp_df["label_text"]
)

# Function to save a DataFrame to JSONL with required format
def save_to_jsonl(df, filename):
    with open(filename, "w") as f:
        for _, row in df.iterrows():
            json_record = {"prompt": row["text"], "completion": row["label_text"]}
            f.write(json.dumps(json_record) + "\n")

# Save the datasets to JSONL files
save_to_jsonl(train_df, "train.jsonl")
save_to_jsonl(valid_df, "valid.jsonl")
save_to_jsonl(test_df,  "test.jsonl")

# Create directory and move files
os.makedirs("data", exist_ok=True)
shutil.move("train.jsonl", "data/train.jsonl")
shutil.move("valid.jsonl", "data/valid.jsonl")
shutil.move("test.jsonl",  "data/test.jsonl")
