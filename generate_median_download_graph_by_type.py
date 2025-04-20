import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from common import COLORS, set_box_color

data = pd.read_csv("output.csv")


species = [
    "5MB",
    "10MB",
    "20MB",
    "50MB",
    "100MB",
    "200MB",
    # "512MB",
    # "1GB",
    # "2GB",
    # "5GB",
]

penguin_means = {
    x: [
        # round(
        data.loc[data["file_size"] == y].loc[data["type"] == x]["total"]
        # .median(), 2
        # )
        for y in species
    ]
    for x in data["type"].unique()
}

x = np.arange(len(species))  # the label locations


WIDTH = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(figsize=(20, 4))

for attribute, measurement in penguin_means.items():
    offset = WIDTH * multiplier
    multiplier += 1
    bpl = ax.boxplot(
        measurement, positions=x + offset, sym="", widths=WIDTH, label=attribute
    )
    set_box_color(bpl, COLORS[attribute])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("Total Download Time (s)")
ax.set_title("Data Download by Type")
ax.set_xticks(x + WIDTH, species)
ax.legend(loc="upper left", ncols=3)
ax.set_ylim(0, 20)
# ax.set_ylim(0, 450)

plt.show()
