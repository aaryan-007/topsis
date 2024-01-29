import pandas as pd
import numpy as np

data = pd.read_csv("data.csv")

# Extract relevant columns
Maximum_Length = data["Maximum_Length"].values
Vocabulary_Size = data["Vocabulary_Size"].values     			
Embedding_Size = data["Embedding_Size"].values
Training_Time = data["Training_Time"].values

# Weights for each parameter
weights = np.array([0.25, 0.25, 0.25, 0.25])

# Normalize the matrix
normalized_matrix = np.column_stack(
    [
        Maximum_Length / np.max(Maximum_Length),
        Vocabulary_Size / np.max(Vocabulary_Size),
        Embedding_Size / np.max(Embedding_Size),
        Training_Time / np.max(Training_Time),
    ]
)

# Calculate the weighted normalized decision matrix
weighted_normalized_matrix = normalized_matrix * weights

# Ideal and Negative Ideal solutions
ideal_solution = np.max(weighted_normalized_matrix, axis=0)
negative_ideal_solution = np.min(weighted_normalized_matrix, axis=0)

# Calculate the separation measures
distance_to_ideal = np.sqrt(
    np.sum((weighted_normalized_matrix - ideal_solution) ** 2, axis=1)
)
distance_to_negative_ideal = np.sqrt(
    np.sum((weighted_normalized_matrix - negative_ideal_solution) ** 2, axis=1)
)

# Calculate the TOPSIS scores
topsis_scores = distance_to_negative_ideal / (
    distance_to_ideal + distance_to_negative_ideal
)

# Rank the models based on TOPSIS scores
data["TOPSIS_Score"] = topsis_scores
data["Rank"] = data["TOPSIS_Score"].rank(ascending=False)

# Print the results
print("Model Ranking:")
print(data[["Model", "TOPSIS_Score", "Rank"]].sort_values(by="Rank"))

data.to_csv("result.csv", index=False)


