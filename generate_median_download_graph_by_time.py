import datetime

import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

from common import COLORS, set_box_color


data = pd.read_csv("output.csv")

# Only use 5GB for this
data = data.loc[data["file_size"] == "5GB"]

data["timestamp"] = (
    data["timestamp"]
    .map(datetime.datetime.fromisoformat)
    .map(lambda x: getattr(x, "hour"))
)

print(data["timestamp"])

# STARTING_TIME_STAMP = datetime.datetime.fromisoformat("2025-04-03T00:00:00")
# ENDING_TIME_STAMP = datetime.datetime.fromisoformat("2025-04-11T00:00:00")

species = range(25)

penguin_means = {
    x: [
        # round(
        data.loc[data["type"] == x].loc[
            data["timestamp"].between(row, species[index + 1])
        ]["total"]
        # .median()
        # ,
        #     2,
        # )
        for index, row in enumerate(species[:-1])
    ]
    for x in data["type"].unique()
}


x = np.arange(len(species[:-1]))  # the label locations

WIDTH = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(figsize=(20, 6))

for attribute, measurement in penguin_means.items():
    offset = WIDTH * multiplier
    multiplier += 1
    bpl = ax.boxplot(measurement, positions=x + offset, widths=WIDTH, label=attribute)
    set_box_color(bpl, COLORS[attribute])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("Total Download Time for 5GB files (s)")
ax.set_xlabel("1 Hour bins for each Type")
ax.set_title("Data Download by Time")
ax.set_xticks(x + WIDTH, species[:-1])
ax.legend(loc="upper left", ncols=3)
ax.set_ylim(0, 700)

plt.show()
