import datetime

import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("output.csv")

# print(data.columns)

# print(data['file_size'])

# species = data['file_size'].unique()
# species = [
#     "5MB",
#     "10MB",
#     "20MB",
#     "50MB",
#     "100MB",
#     "200MB",
#     "512MB",
#     "1GB",
#     "2GB",
#     "5GB",
# ]

# Only use 5GB for this
data = data.loc[data["file_size"] == "5GB"]

# species = data["timestamp"].unique()

# print(species)

data["timestamp"] = data["timestamp"].map(datetime.datetime.fromisoformat).map(lambda x: getattr(x, 'hour'))



print(data["timestamp"])
# print(datetime.datetime())

STARTING_TIME_STAMP = datetime.datetime.fromisoformat('2025-04-03T00:00:00')
ENDING_TIME_STAMP = datetime.datetime.fromisoformat('2025-04-11T00:00:00')

# species = pd.date_range(start=STARTING_TIME_STAMP, end=ENDING_TIME_STAMP, freq='2h')
# species = pd.date_range(periods=24, freq='h')
species = range(25)

# print(species)

penguin_means = {
    x: [
        round(
            data
            .loc[data["type"] == x]
            .loc[data["timestamp"].between(row, species[index + 1])]
            ["total"].median(),
            2,
        )
        for index, row in enumerate(species[:-1])
    ]
    for x in data["type"].unique()
}


x = np.arange(len(species[:-1]))  # the label locations


# print(penguin_means["python"])
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(figsize=(20, 6))

for attribute, measurement in penguin_means.items():
    ax.scatter(x, measurement, label=attribute)
    # ax.legend()
# for attribute, measurement in penguin_means.items():
#     offset = width * multiplier
#     rects = ax.bar(list(x + offset), measurement, width, label=attribute)
#     ax.bar_label(rects, padding=3)
#     multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("Median Total Download Time for 5GB files (s)")
ax.set_xlabel("1 Hour bins for each Type")
ax.set_title("Data Download by Time")
ax.set_xticks(x + width, species[:-1])
ax.legend(loc="upper left", ncols=3)
ax.set_ylim(0, 300)

plt.show()
