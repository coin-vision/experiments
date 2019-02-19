import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# draw histogram with items per class distribution
def printDatasetInfo (datasetFileName):
    coinsDataset = pd.read_csv(datasetFileName)
    coinGroupId = coinsDataset['coinGroupId'].value_counts()
    axarr = coinGroupId.hist(bins=20)
    axarr.set_title('Histogram with items per class distribution')
    axarr.set_xlabel('items per class')
    axarr.set_ylabel('amount')

    print('Total classes: {}, min items per class: {}, max items per class: {}'.format(len(coinGroupId), coinGroupId.min(), coinGroupId.max()))

    
# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()
        
        