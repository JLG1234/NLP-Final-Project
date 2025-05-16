# %%
from sentence_transformers import SentenceTransformer
import pandas as pd
from analyze import labels
# %%

def generate_label_embeddings(labels):
    """
    Generate label embeddings using SentenceTransformer.
    
    Args:
        labels (list): List of labels to generate embeddings for.
        
    Returns:
        pd.DataFrame: DataFrame containing label embeddings and their corresponding labels.
    """
    # Load the model
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Will auto-download if not present

    # Encode label embeddings
    embeddings = model.encode(labels) # Each embedding has 384 dimensions.
    print(f"Each embedding has {len(embeddings[0])} dimensions.")

    # Make column names: embed_0, embed_1, ..., embed_383 (MiniLM-L6-v2 is 384-dim)
    embed_cols = [f'embed_{i}' for i in range(len(embeddings[0]))]

    # Create DataFrame
    df = pd.DataFrame(embeddings, columns=embed_cols)
    df['label'] = labels

    # Move 'label' to the first column
    cols = ['label'] + embed_cols
    df = df[cols]

    return df
# Generate the label embeddings
df = generate_label_embeddings(labels)
# Write them to CSV
df.to_csv('label_embeddings.csv', index=False)
# %%

