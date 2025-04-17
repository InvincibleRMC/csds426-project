import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("output.csv")

# print(data.columns)

# print(data['file_size'])

# species = data['file_size'].unique()
species = [
    "5MB",
    "10MB",
    "20MB",
    "50MB",
    "100MB",
    "200MB",
    "512MB",
    "1GB",
    "2GB",
    "5GB",
]

penguin_means = {
    x: [
        round(data.loc[data["file_size"] == y].loc[data["type"] == x]["total"].median(), 2)
        for y in species
    ]
    for x in data["type"].unique()
}

x = np.arange(len(species))  # the label locations


print(penguin_means["python"])
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(figsize=(20, 4))

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(list(x + offset), measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("Median Total Download Time (s)")
ax.set_title("Data Download by Type")
ax.set_xticks(x + width, species)
ax.legend(loc="upper left", ncols=3)
ax.set_ylim(0, 250)

plt.show()
