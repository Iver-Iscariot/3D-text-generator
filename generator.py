import numpy as np
import matplotlib.pyplot as plt
import textwrap
 

zero_distance = 30  # defining zero-point away from the face
eye_spacing   = 7.5 # distance between the eyes

horlen = 11.5
verlen = 10
padding = 0.5

# distances you want demonstrated
distances = [0,1,2.5, 4,-1,-2.5, -4]

# set the font size
cm = 0.6  # height in centimeters
font_size_in_points = cm * 72 / 2.54 * 2.7


def getOffset(dist):
    ratio  = dist/zero_distance     # ratio of same-angle triangles 
    offset = eye_spacing/2 * ratio  # offset from center line that a eye will see when focusing at zero distance
    return offset


offsets   = np.array([[getOffset(d), d, -1*getOffset(d)] for d in distances])

def parse_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()  # Read entire text, keeping manual \n line breaks

# Load text
filename = "input.txt"
paragraph = parse_text_file(filename)


wrap_width = int(horlen * 1.14 / cm)


# Wrap each line individually, preserving empty lines
wrapped_text = []
for line in paragraph.splitlines():
    if line.strip() == "":
        wrapped_text.append("")  # preserve blank lines
    else:
        wrapped_text.extend(textwrap.wrap(line, width=wrap_width))


fig, ax = plt.subplots(figsize=(horlen, verlen), dpi=300, nrows=2, ncols=2)
fig.set_size_inches(horlen*2, verlen*2)

# plot a side. they are very similar so its mostly just switching the direction of the offset per eye
def plotSub(k):
    if k == 0:
        mul = 1
    else:
        mul = -1


    for i in range(len(wrapped_text)):
        ax[0][k].text( padding, verlen - padding -cm - cm*i*1.8, wrapped_text[i], fontsize=font_size_in_points, ha='left', va='bottom', color='black')


    ax[0][k].plot([0.05, 4.05], [0.05,0.05], color='red', lw=2)  # horizontal line
    ax[0][k].plot([0.05, 0.05], [0.05,4.05], color='red', lw=2)  # vertical line

    ax[0][k].set_xlim(0, horlen); ax[0][k].set_ylim(0, verlen)
    ax[0][k].set_xticks([]);      ax[0][k].set_yticks([])
    ax[0][k].set_aspect('equal')  # Lock aspect ratio

    for i in range(len(offsets)):
        height = verlen/(len(distances)+1)
        
        if k == 0: #venstre bilde
            ax[1][k].scatter(horlen/2 + offsets[i][0], [verlen - height*(i+1)], s=50, label = f"{distances[i]} cm avstand")
            ax[1][k].plot([horlen/2,horlen/2], [0, verlen], color='black', linestyle = "dashed", lw=1, alpha = 0.2)
        else: #hoyre bilde
            ax[1][k].scatter(horlen/2 + offsets[i][2], [verlen - height*(i+1)], s=50, label = f"{distances[i]} cm avstand")
            ax[1][k].plot([horlen/2,horlen/2], [0, verlen], color='black', linestyle = "dashed", lw=1, alpha = 0.2)
    
    ax[1][k].set_xlim(0, horlen); ax[1][k].set_ylim(0, verlen)
    ax[1][k].set_xticks([]);      ax[1][k].set_yticks([])
    ax[1][k].set_aspect('equal')  # Lock aspect ratio

plotSub(0)
plotSub(1)

ax[1][1].legend(loc='upper left', fontsize=font_size_in_points, bbox_to_anchor=(1.05, 1), borderaxespad=0.)

plt.savefig("output.png", dpi=300, bbox_inches='tight', pad_inches=0.1)