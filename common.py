import matplotlib.pyplot as plt

COLORS = {'curl': "blue", "python": "orange", "python_jit": "yellow", "wget": "red"}

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)