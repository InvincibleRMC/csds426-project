import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

from common import COLORS


data = pd.read_csv("output.csv")

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

file_size_mapping = {
    "5MB": 5,
    "10MB": 10,
    "20MB": 20,
    "50MB": 50,
    "100MB": 100,
    "200MB": 200,
    "512MB": 512,
    "1GB": 1024,
    "2GB": 1024 * 2,
    "5GB": 1024 * 5,
}

data["file_size"] = data["file_size"].map(lambda x: file_size_mapping[x])

# print(data['file_size'])

x_axis = [file_size_mapping[i] for i in species]  # the label locations


penguin_means = {
    x: [
        round(
            data.loc[data["file_size"] == y].loc[data["type"] == x]["real"].median(), 2
        )
        for y in x_axis
    ]
    for x in data["type"].unique()
}


WIDTH = 0.25  # the width of the bars
multiplier = 0

# fig, ax = plt.subplots(figsize=(20, 4))
fig, ax = plt.subplots()

label_remap = {
    "wget": "wget",
    "curl": "curl",
    "python": "python",
    "python_jit": "pre-compiled python",
}


for attribute, measurement in penguin_means.items():
    coefficients = np.polyfit(x_axis, measurement, 1)
    print(coefficients)
    polynomial = np.poly1d(coefficients)
    y_line = polynomial(x_axis)
    bpl = ax.scatter(
        x_axis, measurement, label=label_remap[attribute], color=COLORS[attribute]
    )
    ax.plot(x_axis, y_line, color=COLORS[attribute])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("Total Download Time (s)")
ax.set_xlabel("File Size (MB)")
ax.set_title("Data Download Best Fit")
# ax.set_xticks(x,)
ax.legend(loc="upper left", ncols=4)
# ax.set_ylim(0, 40)
ax.set_ylim(0, 250)

plt.show()
