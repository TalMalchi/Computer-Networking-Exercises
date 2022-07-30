import matplotlib.pyplot as plt
import numpy as np


def graph_plot():
    cubic = {}
    reno = {}

    cubic2 = {}
    reno2 = {}
    with open("times.txt",'r') as time_file:
        for j in range(2):
            for i in range(4):
                a = time_file.readline()
                b = time_file.readline()
                if j == 0:
                    cubic[(i+2)*5] = float(a.strip())
                    reno[(i + 2) * 5] = float(b.strip())
                else:
                    cubic2[(i + 2) * 5] = float(a.strip())
                    reno2[(i + 2) * 5] = float(b.strip())

    # set width of bar
    barWidth = 0.25
    fig = plt.subplots(figsize=(12, 8))

    # Set position of bar on X axis
    br1 = np.arange(len(cubic))
    br2 = [x + barWidth for x in br1]

    # Make the plot
    plt.bar(br1, cubic.values(), color='#a5a391', width=barWidth,
            edgecolor='grey', label='Cubic')
    plt.bar(br2, reno.values(), color='#acc2d9', width=barWidth,
            edgecolor='grey', label='Reno')

    # Adding Xticks
    plt.xlabel('Drop Precentage', fontweight='bold', fontsize=15)
    plt.ylabel('Times in Seconds', fontweight='bold', fontsize=15)
    plt.xticks([r + barWidth for r in range(len(cubic))],
               [x.__str__()+"%" for x in cubic.keys()], fontweight='bold', fontsize=14)
    plt.margins(y=0.00001, tight=None)
    plt.legend()
    plt.savefig("Graph.png")
    plt.show()

    fig2 = plt.subplots(figsize=(12, 8))

    # Set position of bar on X axis
    br1 = np.arange(len(cubic2))
    br2 = [x + barWidth for x in br1]

    # Make the plot
    plt.bar(br1, cubic2.values(), color='#a5a391', width=barWidth,
            edgecolor='grey', label='Cubic')
    plt.bar(br2, reno2.values(), color='#acc2d9', width=barWidth,
            edgecolor='grey', label='Reno')

    # Adding Xticks
    plt.xlabel('Drop Precentage', fontweight='bold', fontsize=15)
    plt.ylabel('Times in Seconds', fontweight='bold', fontsize=15)
    plt.xticks([r + barWidth for r in range(len(cubic2))],
               [x.__str__()+"%" for x in cubic2.keys()], fontweight='bold', fontsize=14)

    plt.margins(y=0.00001, tight=None)
    plt.legend()
    plt.savefig("Graph2.png")
    plt.show()


if __name__ == '__main__':
    graph_plot()
