import random
import time
from percolation import Percolation
import matplotlib.pyplot as plt
from config import NUMTESTS as numtests

# Returns the (row,col) tuple for given index and size of grid
def get_row_col(i, n) :
    return (i//n, i%n)

# Computes mean value
def mean(arr) :
    return sum(arr)/len(arr)

# Computes standard deviaiton
def std_dev(arr) :
    x = mean(arr)
    dev = [abs(x-i)**2 for i in arr]
    return (sum(dev)/len(dev))**0.5

# Computes mean deviation
def mean_dev(arr) :
    x = mean(arr)
    dev = [abs(x-i) for i in arr]
    return sum(dev)/len(dev)

# Counts the number of values in a given range
def counter(arr, mean, tol) :
    count = 0
    for i in arr :
        if i >= mean-tol and i <= mean+tol :
            count += 1
    return count

class Simulator :

    def __init__(self, size) :
        self.size   = size

    # Simulates percolation testing without graphics, for a given order of sites
    def simulate(self, order) :
        iteration = 0
        t0 = time.time()
        while True:
            next_open   = get_row_col(random_order[iteration], size)
            percolation.open(next_open[0], next_open[1])
            iteration += 1

            if percolation.percolates() :
                opened = percolation.numberOfOpenSites()
                break
        return {'num': opened,'perc': opened*100/size/size}

if __name__ == '__main__' :

    size = int(input("Enter size of percolation grid: "))
    t0 = time.time()

    # 2 lists To store results
    numsites_res = []
    percentage_res = []

    # Test runs
    for testrun in range(numtests) :
        percolation = Percolation(size)
        random_order = [i for i in range(size*size)]
        random.shuffle(random_order)
        sim = Simulator(size)
        di = sim.simulate(random_order)
        numsites_res.append(di['num'])
        percentage_res.append(di['perc'])

        if testrun%100 == 0 :
            print(testrun,'out of',numtests,'completed.')

    print('\n',' '*30, 'ANALYSIS\n')
    print(numtests,'runs of size',str(size)+'x'+str(size),'took',round(time.time()-t0,3),'sec')

    # Basic stats of result
    avg     = mean(percentage_res)
    stdDev  = std_dev(percentage_res)
    meanDev = mean_dev(percentage_res)
    print('Mean Percetage:',avg)
    print('Std. Deviation:',stdDev)
    print('Mean Deviation:',meanDev)

    # 95% Confidence stats
    confidence_tolerance_95 = 1.96*stdDev#/(numtests**0.5)
    print('95% confidence limits: [',round(avg-confidence_tolerance_95,3),',',round(avg+confidence_tolerance_95,3),']')
    print('Perctage of tests runs within the 95% confidence interval:', counter(percentage_res, avg, confidence_tolerance_95)*100/numtests)

    # Graph showing histogram (approximating Gaussian curve)
    plt.hist(percentage_res,bins=(max(numsites_res)-min(numsites_res)+1))
    plt.ylabel('Frequecy')
    plt.xlabel('percentage of sites opened')
    plt.title(str(numtests)+' tests for size '+str(size))
    plt.show()
