import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

f = open("samples.txt", "r")
v = []
i = 0
for line in f:
    i += 1
    v.append(float(line))

fig, ax = plt.subplots(figsize=(10, 6))


def animate(i):
    plt.cla()

    line1 = plt.axhline(np.e-2, label="e-2", color="red")
    plt.legend([line1], ["e-2"])
    plt.xlabel("Number of samples taken")
    plt.ylabel("Median Money taken")

    ax.set(xlim=(0, len(v)), ylim=(0, 1))
    if i < 3:
        i = 3
    index = int(i*(len(v)/100))
    # print(index)
    ax.plot(v[:index], color='black')


anim = animation.FuncAnimation(
    fig, animate, interval=1, frames=int(len(v)/100)+1)

# plt.draw()
# plt.show()


Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=-1)
anim.save('mic.mp4', writer=writer)
