
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
import mat73
import time  # Import time for the delay
import livePlotter as lp

file_path = 'C:\\uni stuff\\GDP\\RobotSimulink\\recQData.mat'

data_dict = mat73.loadmat(file_path, use_attrdict=True)

rawData = data_dict['ans']

nodeCount = int(rawData.shape[0]/2)

xNodes = rawData[1:nodeCount+1,  :].transpose()
yNodes = rawData[nodeCount+1:, :].transpose()

# format: t1[ 1[x, y], 2[x, y] ... ]

  
i = 0
iMax  = xNodes.shape[0]
mTime = 30

""
wSize = 10
window = lp.PlotWindow( wSize, wSize )
 
graphDisp = lp.LineGraphDisplay( 0, 0, wSize, wSize, window, np.min(xNodes), np.max(xNodes), np.min(yNodes), np.max(yNodes) ) 
window.render()  
graphDisp.parseData( [0,1], [0,1] ) 
window.render()  

skipPeriod = 1000

for xSet, ySet in zip( xNodes, yNodes ):
    if ( i%skipPeriod == 0 ):
        lp.delay(0.05)  
        print( 'time=',mTime*i/iMax,'s' )
        
        #graphDisp.parseData( xNodes[0,:], yNodes[0,:] ) 
        graphDisp.parseData( xSet, ySet ) 
        
        window.render()  

    i+=1
    ""


""