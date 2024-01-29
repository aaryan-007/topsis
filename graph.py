
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import result
data = pd.read_csv("result.csv")


# Display the table
print("Model Ranking Table:")
print(
    data[["Model", "Maximum_Length", "Vocabulary_Size", "Embedding_Size", "Training_Time", "Rank"]].sort_values(
        by="Rank"
    )
)

# Bar chart
labels = data["Model"]
num_models = len(labels)

# Parameters for bar chart
Maximum_Length = data["Maximum_Length"]
Vocabulary_Size = data["Vocabulary_Size"]
Embedding_Size = data["Embedding_Size"]
Training_Time = data["Training_Time"]
ranks = data["Rank"]

# Normalize ranks to a scale of 0 to 1 for better comparison
normalized_ranks = ranks / np.max(ranks)

# Plot the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.2
index = range(num_models)

ax.bar(index,Maximum_Length,width=bar_width,label="Maximum_Length")
ax.bar(index,Vocabulary_Size,width=bar_width,label="Vocabulary_Size",bottom=Maximum_Length,)
ax.bar(index, Embedding_Size, width=bar_width, label="Embedding_Size",bottom=Maximum_Length + Vocabulary_Size,)
ax.bar(index,Training_Time,width=bar_width,label="Training_Time",bottom=Maximum_Length + Vocabulary_Size + Embedding_Size,)
ax.bar(
    index,
    normalized_ranks,
    width=bar_width,
    label="Normalized Rank",
    color="black",
    alpha=0.5,
)

ax.set_xticks(index)
ax.set_xticklabels(labels)
ax.set_ylabel("Metrics")
ax.set_title("Text Classification Model Comparison Through Topsis")

ax.legend()
plt.savefig("BarChart.png")
plt.show()