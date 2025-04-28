import datetime

import pandas as pd

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from common import COLORS

matplotlib.rcParams.update({"font.size": 18})

data = pd.read_csv("output.csv")

# Only use 5GB for this
data = data.loc[data["file_size"] == "5GB"]

data["timestamp"] = (
    data["timestamp"].map(datetime.datetime.fromisoformat).map(lambda x: x.weekday())
)

# print(data["timestamp"])

# STARTING_TIME_STAMP = datetime.datetime.fromisoformat("2025-04-03T00:00:00")
# ENDING_TIME_STAMP = datetime.datetime.fromisoformat("2025-04-11T00:00:00")

species = range(7)

keys = ["wget", "curl", "python"]

penguin_means = {
    x: [
        round(
            data.loc[data["type"] == x]
            .loc[data["timestamp"] == index]["real"]
            .median(),
            2,
        )
        for index, row in enumerate(species)
    ]
    for x in keys
}


x = np.arange(len(species))  # the label locations

WIDTH = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(figsize=(20, 6))

for attribute, measurement in penguin_means.items():
    offset = WIDTH * multiplier
    multiplier += 1
    bpl = ax.plot(x, measurement, label=attribute, color=COLORS[attribute])
    # set_box_color(bpl, COLORS[attribute])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("Total Download Time for 5GB files (s)")
ax.set_xlabel("Days of the Week")
ax.set_title("Data Download Time by Day")
ax.legend(loc="upper left", ncols=4)
ax.set_xticks(
    x, ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)
# ax.set_ylim(160, 175)

plt.show()
