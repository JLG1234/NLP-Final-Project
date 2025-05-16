import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load DataFrame
df = pd.read_csv('label_embeddings.csv')

# Get numeric embeddings
embeddings = df.drop(columns=['label']).values
labels = df['label'].tolist()

def create_pca_plot(embeddings, labels):
    """
    Create a PCA plot of the embeddings.
    
    Args:
        embeddings (np.ndarray): The embeddings to plot.
        labels (list): The labels corresponding to the embeddings.
    """
    # Reduce to 2D with PCA
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(embeddings)  # shape: (60, 2)

    # Plot
    plt.figure(figsize=(10, 8))
    plt.scatter(reduced[:, 0], reduced[:, 1])

    # Add labels
    for i, label in enumerate(labels):
        plt.text(reduced[i, 0], reduced[i, 1], label, fontsize=8)

    plt.title('2D PCA Projection of Label Embeddings')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.tight_layout()
    plt.savefig('results_/label_embeddings_pca.png')
# Reduce to 2D with PCA

import pandas as pd
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('label_embeddings.csv')
labels = df['label'].tolist()
embeddings = df.drop(columns=['label']).values

# Compute linkage
distance_matrix = pdist(embeddings, metric='cosine')
Z = linkage(distance_matrix, method='average')

# Plot dendrogram and get the coordinates
fig, ax = plt.subplots(figsize=(20, 8))
ddata = dendrogram(Z, labels=labels, leaf_rotation=90, leaf_font_size=10, ax=ax, color_threshold=None)

# Z has shape (n-1, 4): [idx1, idx2, dist, sample_count]
icoord = ddata['icoord']
dcoord = ddata['dcoord']
leaves = ddata['leaves']

# For each internal node, place a label at its coordinates
for i, (xs, ys) in enumerate(zip(icoord, dcoord)):
    x = 0.5 * (xs[1] + xs[2])  # Middle x
    y = ys[1]                  # Height
    ax.text(x, y, str(i), va='bottom', ha='center', fontsize=8, color='black')  # cluster index

plt.title('Semantic Hierarchy of Labels (with Internal Node Indices)')
plt.ylabel('Cosine Distance')
plt.tight_layout()
plt.savefig('results_/label_semantic_hierarchy_dendrogram_with_internal_labels.png')

create_pca_plot(embeddings, labels)