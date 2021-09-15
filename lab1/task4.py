from sys import argv


capacity = int(argv[1])
weights = list(map(int,argv[2:]))

def bestKnapsack(capacity, weights):
    '''
    bestKnapsack - it's a function for mading a matrix (which help us to decide which bar of gold take).
    It's named dynamic programming.
    '''

    bars = [0]+weights
    barsDict = {}
    for i in range(0, capacity+1):
        barsDict[(i, 0)] = 0
    for i in range(0, len(bars)):
        barsDict[(0, i)] = 0
    for i in range(1, len(bars)):
        for mass in range(1, capacity+1):
            barsDict[(mass, i)] = barsDict[(mass, (i-1))]
            if bars[i]<=mass:
                tempMass = barsDict[(mass-bars[i]),i-1]+bars[i]
                if barsDict[(mass,i)]<tempMass:
                    barsDict[(mass,i)]=tempMass
    return max(barsDict.values())


print(bestKnapsack(capacity,weights))