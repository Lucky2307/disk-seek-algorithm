from core import DSeek
import matplotlib.pyplot as plt
import random


print("Disk seek algorithm simulator")
print("/////////////////////////////")
print("The following program will generate the following algorithms:")
print("1. FCFS")
print("2. SSTF")
print("3. SCAN")
print("4. CSCAN")
print("5. CLOOK")
print("")

print("Input format: int")
print("Example: 199")
print("Input 0 to randomize everything")
tracksize = int(input("Input tracksize: "))
if tracksize == 0:
    tracksize = random.randrange(1, 200)
    headpos = random.randrange(1, tracksize)
    queue = [random.randrange(0, tracksize) for i in range(random.randint(5, 20))]
else:   
    print("Input format: int")
    print("Example: 50")
    headpos = int(input("Head starting position: "))
    while(headpos > tracksize or headpos < 0):
        print("Head position out of range! Pos range: 0 - {}, Head pos: {}".format(tracksize, headpos))

    print("Input format: list separated with space")
    print("Example: 95 180 34 119 11 123 62 64")
    queue = list(map(int, input("Input queue sequence: ").rsplit()))
# Input checking
outofrange = True
while(outofrange):
    for track in queue:
        if track > tracksize or track < 0:
            print("Track out of range! Track range: 0 - {}, track: {}".format(tracksize, track))
            queue = list(map(int, input("Input queue sequence: ").rsplit(",")))
            break
    outofrange = False


dseek = DSeek(queue, headpos, tracksize)
dseek.printall()

fig, ax = plt.subplots(2, 3, figsize=(12, 8))
fig.canvas.manager.set_window_title("Disk seek algorithm")
ax[0,0].set_axis_off()
ax[0,0].text(0, 0.5, "Tracksize = {}\nInit head pos = {}\nQueue = {}".format(tracksize, headpos, queue), wrap=True)

ax[0,1].plot(dseek.fcfs.order, range(dseek.fcfs.order.__len__()), 'ob-', mfc='r')
ax[0,1].xaxis.set_ticks(dseek.fcfs.order)
ax[0,1].title.set_text("FCFS")

ax[0,2].plot(dseek.sstf.order, range(dseek.sstf.order.__len__()), 'ob-', mfc='r')
ax[0,2].xaxis.set_ticks(dseek.sstf.order)
ax[0,2].title.set_text("SSTF")

ax[1,0].plot(dseek.scan.order, range(dseek.scan.order.__len__()), 'ob-', mfc='r')
ax[1,0].xaxis.set_ticks(dseek.scan.order)
ax[1,0].title.set_text("SCAN")

ax[1,1].plot(dseek.cscan.order, range(dseek.cscan.order.__len__()), 'ob-', mfc='r')
ax[1,1].xaxis.set_ticks(dseek.cscan.order)
ax[1,1].title.set_text("CSCAN")

ax[1,2].plot(dseek.clook.order, range(dseek.clook.order.__len__()), 'ob-', mfc='r')
ax[1,2].xaxis.set_ticks(dseek.clook.order)
ax[1,2].title.set_text("CLOOK")

for i in range(2):
    for j in range(3):
        ax[i,j].set_xlim([0,tracksize])
        ax[i,j].xaxis.tick_top()
        ax[i,j].invert_yaxis()
        ax[i,j].yaxis.set_visible(False)

plt.show()