from math_functions import distance_2d, get_catenary_cable
from .Particle import Particle
import numpy as np

class Simulation:
    def __init__(self, nodeCount, nodeMass):
        self.nodeCount = nodeCount
        self.nodeMass = nodeMass

        #initialise attributes
        self.timeStep = None
        self.catenary_c = None
        self.nodes = []

    # def initialise_sim(self,horizontalOffset,verticalOffset = 0):
    #     self.leftNodes.append(Particle(self.nodeMass, 0, 0, fixed = True))
    #     self.rightNodes.append(Particle(self.nodeMass, horizontalOffset, verticalOffset, fixed = True))

    def reset_sim(self, Length1, Length2, robotx, roboty, horizontalOffset, verticalOffset):
        self.nodes = []

        distanceRobot = distance_2d([robotx,roboty])
        if Length1 > distanceRobot:
            node_x, node_y = get_catenary_cable([robotx,roboty],[0,0],Length1,self.nodeCount/2)
        else:
            node_x = np.linspace(0,robotx,self.nodeCount/2)
            node_y = np.linspace(0,roboty,self.nodeCount/2)
        # remove common element in list
        node_x.pop()
        node_y.pop()

        if Length2 > distanceRobot:
            node_x, node_y = get_catenary_cable([robotx,roboty], [horizontalOffset, verticalOffset], Length1, self.nodeCount/2)
        else:
            node_x = np.linspace(robotx,horizontalOffset,self.nodeCount/2)
            node_y = np.linspace(robotx,verticalOffset,self.nodeCount/2)

        for i in range(self.nodeCount):
            self.nodes.append(Particle(self.nodeMass, node_x[i], node_y[i]))
        
        self.nodes[0] = Particle(self.nodeMass, 0, 0, fixed = True)




            
