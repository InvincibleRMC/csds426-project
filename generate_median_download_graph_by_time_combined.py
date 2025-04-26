import datetime

import pandas as pd

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


matplotlib.rcParams.update({"font.size": 18})

data = pd.read_csv("output.csv")

# Only use 5GB for this
data = data.loc[data["file_size"] == "5GB"]

data["timestamp"] = (
    data["timestamp"]
    .map(datetime.datetime.fromisoformat)
    .map(lambda x: getattr(x, "hour"))
)

# print(data["timestamp"])

# STARTING_TIME_STAMP = datetime.datetime.fromisoformat("2025-04-03T00:00:00")
# ENDING_TIME_STAMP = datetime.datetime.fromisoformat("2025-04-11T00:00:00")

species = range(25)

keys = ["wget", "curl", "python"]

penguin_means = {
    x: [
        round(
            data.loc[data["timestamp"].between(row, species[index + 1])][
                "real"
            ].median(),
            2,
        )
        for index, row in enumerate(species[:-1])
    ]
    for x in ["Data"]
}


x = np.arange(len(species[:-1]))  # the label locations

WIDTH = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(figsize=(20, 6))

for attribute, measurement in penguin_means.items():
    offset = WIDTH * multiplier
    multiplier += 1
    bpl = ax.plot(x, measurement)
    # set_box_color(bpl, COLORS[attribute])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("Total Download Time for 5GB files (s)")
ax.set_xlabel("1 Hour Bins")
ax.set_title("Data Download by Time")
ax.set_xticks(x, species[:-1])
ax.set_ylim(160, 175)

plt.show()
