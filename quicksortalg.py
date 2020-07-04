import time

def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]
    
    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)
    
    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(
                len(data), head, tail, border, j, True))
            time.sleep(timeTick)
            data[border], data[j] = data[j], data[border]
            border+=1
            
        drawData(data, getColorArray(
            len(data), head, tail, border, j))
        time.sleep(timeTick)
            
    # SWAP PIVOT WITH BORDER VALUE
    drawData(data, getColorArray(
        len(data), head, tail, border, tail, True))
    time.sleep(timeTick)
    data[border], data[tail] = data[tail], data[border]
    
    return border

def quick_sort(data, head, tail, drawData, timeTick):
    
    if head < tail:
        partitionidx = partition(data, head, tail, drawData, timeTick)

        # LEFT PARTITION
        quick_sort(data, head, partitionidx-1, drawData, timeTick)

        # RIGHT PARTITION
        quick_sort(data, partitionidx+1, tail, drawData, timeTick)

def getColorArray(datalen, head, tail, border, currIdx, isSwaping = False):
    
    ColorArray = []
    for i in range(datalen):
        # base color
        if i >= head and i <=tail:
            ColorArray.append('gray')
        else:
            ColorArray.append('white')
            
        if i == tail:
            ColorArray[i] = 'blue'
        elif i == border:
            ColorArray[i] = 'red'
        elif i == currIdx:
            ColorArray[i] = 'yellow'
            
        if isSwaping:
            if i == border or i == currIdx:
                ColorArray[i] = 'green'
                
    return ColorArray
