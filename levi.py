import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("output.csv")


data_ads = [gx_false, chrome_false]
data_no_ads = [gx_true, chrome_true]

ticks = data["type"].unique()

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

plt.figure()

bpl = plt.boxplot(data_ads, positions=np.array(range(len(data_ads)))*2.0-0.4, sym='', widths=0.6)
bpr = plt.boxplot(data_no_ads, positions=np.array(range(len(data_no_ads)))*2.0+0.4, sym='', widths=0.6)
set_box_color(bpl, '#D7191C') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#2C7BB6')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='Ads')
plt.plot([], c='#2C7BB6', label='No Ads')
plt.legend()

plt.xticks(range(0, len(ticks) * 2, 2), ticks)
plt.xlim(-2, len(ticks)*2)
plt.ylabel('Time Until Network Idle (ms)')
plt.xlabel('Browser')
plt.title('Box and Whisker Plot of Time Until Network Idle')
plt.tight_layout()
plt.savefig('boxcompare.png')