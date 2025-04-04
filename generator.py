import numpy as np
import matplotlib.pyplot as plt

texts = [
    ["Hewwo world", 0],
    ["close to face", 5],
    ["far from face", -5]
]

zero_distance = 30  # defining zero-point away from the face
eye_spacing   = 7.5 # distance between the eyes

# Calculate the offset for each text based on the distance from the zero point
for line in texts:
    dist   = line[1]                # distance from zero point
    ratio  = dist/zero_distance     # ratio of same-angle triangles 
    offset = eye_spacing/2 * ratio  # offset from center line that a eye will see when focusing at zero distance

    line.append(offset)  # add offset to the line for plotting

print(texts)

# set the font size
cm = 0.5  # height in centimeters
font_size_in_points = cm * 72 / 2.54 * 2.7

horlen = 12
verlen = 8
fig, ax = plt.subplots(figsize=(horlen, verlen), dpi=300, nrows=1, ncols=2)
fig.set_size_inches(horlen*2, verlen)

# plot a side. they are very similar so its mostly just switching the direction of the offset per eye
def plotSub(k):
    if k == 0:
        mul = 1
    else:
        mul = -1


    for i in range(len(texts)):
        ax[k].text( horlen/2 + mul*texts[i][2], verlen - (len(texts) - i), texts[i][0], fontsize=font_size_in_points, ha='left', va='bottom', color='black')


    ax[k].plot([0.1, 1.1], [0.1,0.1], color='red', lw=1)  # horizontal line
    ax[k].plot([0.1, 0.1], [0.1,1.1], color='red', lw=1)  # vertical line
    ax[k].plot([0.1, horlen-0.1], [verlen-0.1, verlen-0.1], color='red', lw=1)  # horizontal line

    ax[k].set_xlim(0, horlen); ax[k].set_ylim(0, verlen)
    ax[k].set_xticks([]);      ax[k].set_yticks([])
    plt.gca().set_aspect('equal')  # Lock aspect ratio

plotSub(0)
plotSub(1)

plt.savefig("output.png", dpi=300, bbox_inches='tight', pad_inches=0.1)