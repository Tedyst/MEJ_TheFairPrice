import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

savetofile = False

f = open("samples.txt", "r")
v = []
i = 0
for line in f:
    i += 1
    v.append(float(line))

fig, ax = plt.subplots(figsize=(10, 6))


def animate(i):
    plt.cla()

    plt.xlabel("Number of samples taken")
    plt.ylabel("Percent of winning games")

    ax.set(xlim=(0, len(v)), ylim=(0, 50))
    if i < 3:
        i = 3
    index = int(i*(len(v)/100))
    # print(index)
    ax.plot(v[:index])


anim = animation.FuncAnimation(
    fig, animate, interval=1, frames=int(len(v)/100)+1)

if savetofile:
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=-1)
    anim.save('mic.mp4', writer=writer)
else:
    plt.show()
