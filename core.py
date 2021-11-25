# Disk seek algorithm
#
# 1. FCFS
# 2. SSTF
# 3. SCAN
# 4. C-SCAN
# 5. C-LOOK

class DSeek:
    """
    Main container
    """
    class DSeekType:
        """
        Instance for one type of disk seeking algorithm
        """
        def __init__(self, order: list, tracks: int):
            self.order = order
            self.tracks = tracks

    def __init__(self, queue:list, headpos:int, tracksize:int):
        # Initialize default values
        self.queue = queue
        self.headpos = headpos
        self.tracksize = tracksize

        # Initialize all the different algorithms values
        self._fcfs_init()
        self._sstf_init()
        self._scan_init()
        self._cscan_init()
        self._clook_init()


    def printall(self):
        print("FCFS: {} Head movement".format(self.fcfs.tracks))
        print(self.fcfs.order)
        print("")
        print("SSTF: {} Head movement".format(self.sstf.tracks))
        print(self.sstf.order)
        print("")
        print("SCAN: {} Head movement".format(self.scan.tracks))
        print(self.scan.order)
        print("")
        print("CSCAN: {} Head movement".format(self.cscan.tracks))
        print(self.cscan.order)
        print("")
        print("CLOOK: {} Head movement".format(self.clook.tracks))
        print(self.clook.order)

    def _totalTracks(self, order):
        # Calculating total head movement
        tracks = 0
        for i in range(0, order.__len__()-1):
            tracks = tracks + abs(order[i] - order[i+1])
        return tracks


    def _fcfs_init(self):
        # Calculating the order of the request
        order = self.queue[:]
        order.insert(0,self.headpos)

        # Calculating total head movement
        tracks = self._totalTracks(order)

        self.fcfs = DSeek.DSeekType(order, tracks)

    def _sstf_init(self):
        # Calculating the order of the request
        queue = self.queue[:] + [self.headpos]
        queue.sort()
        pointer = queue.index(self.headpos)
        order = []
        for _ in range(queue.__len__()):
            # Will loop until queue is empty
            if pointer == 0: order.append(queue.pop(0))
            elif 0 < pointer < queue.__len__()-1:
                if queue[pointer] - queue[pointer-1] < abs(queue[pointer] - queue[pointer+1]):
                    order.append(queue.pop(pointer))
                    pointer = pointer - 1
                else:
                    order.append(queue.pop(pointer))
            elif pointer == queue.__len__()-1:
                    order.append(queue.pop(pointer))
                    pointer = pointer - 1

        # Calculating total head movement
        tracks = tracks = self._totalTracks(order)
        
        self.sstf = DSeek.DSeekType(order, tracks)

    def _scan_init(self):
        # Calculating the order of the request
        if self.headpos - 0 <= self.tracksize - self.headpos:
            # Making sure headpos is not min
            queue = self.queue + ([0] if self.headpos == 0 else [0, self.headpos])
            queue.sort()
            headposIndex = queue.index(self.headpos)
            order = list(reversed(queue[:headposIndex+1])) + queue[headposIndex+1:]
        elif self.headpos - 0 > self.tracksize - self.headpos:
            # Making sure headpos is not max
            queue = self.queue + ([self.tracksize] if self.headpos == self.tracksize else [self.headpos, self.tracksize])
            queue.sort()
            headposIndex = queue.index(self.headpos)
            order = queue[headposIndex:] + list(reversed(queue[:headposIndex]))

        # Calculating total head movement
        tracks = self._totalTracks(order)

        self.scan = DSeek.DSeekType(order, tracks)


    def _cscan_init(self):
        # Calculating the order of the request
        # Making sure headpos is not min or max
        queue = self.queue + ([0, self.headpos, self.tracksize] if self.headpos != 0 and self.headpos != self.tracksize else list(set(0, self.headpos, self.tracksize)))
        queue.sort()
        headposIndex = queue.index(self.headpos)
        if self.headpos - 0 <= self.tracksize - self.headpos: order = list(reversed(queue[:headposIndex+1])) + list(reversed(queue[headposIndex+1:]))
        elif self.headpos - 0 > self.tracksize - self.headpos: order = queue[headposIndex:] + queue[:headposIndex]

        # Calculating total head movement
        tracks = self._totalTracks(order) - self.tracksize
        #                                - the move from end to end because it is insignificant and not counted as head movement

        self.cscan = DSeek.DSeekType(order, tracks)

    def _clook_init(self):
        # Calculating the order of the request
        queue = self.queue + [self.headpos]
        queue.sort()
        headposIndex = queue.index(self.headpos)
        if self.headpos - 0 <= self.tracksize - self.headpos: order = list(reversed(queue[:headposIndex+1])) + list(reversed(queue[headposIndex+1:]))
        elif self.headpos - 0 > self.tracksize - self.headpos: order = queue[headposIndex:] + queue[:headposIndex]

        # Calculating total head movement
        tracks = self._totalTracks(order) - (max(queue) - min(queue))

        self.clook = DSeek.DSeekType(order, tracks)
    


if __name__ == "__main__":
    queue = [95, 180, 34, 119, 11, 123, 62, 64]
    headpos = 50
    tracksize = 199

    dseek = DSeek(queue,headpos,tracksize)
    dseek.printall()
    # print("FCFS")
    # print(dseek.fcfs.order)
    # print(dseek.fcfs.tracks)

    # print("SSTF")
    # print(dseek.sstf.order)
    # print(dseek.sstf.tracks)

    # print("SCAN")
    # print(dseek.scan.order)
    # print(dseek.scan.tracks)

    # print("CSCAN")
    # print(dseek.cscan.order)
    # print(dseek.cscan.tracks)

    # print("CLOOK")
    # print(dseek.clook.order)
    # print(dseek.clook.tracks)