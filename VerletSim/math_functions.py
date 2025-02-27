from math import sqrt
import numpy as np
from scipy.optimize import fsolve

def distance_2d(xy1,xy2):
    return sqrt ((xy1[0]-xy2[0])**2 + (xy1[1]-xy2[1])**2)

def get_catenary_cable(xy1, xy2, ropeLength, num_points=4):
    # Function creates line of points following the catenary curve for a rope of given length
    ###########
    distance = distance_2d(xy1,xy2)

    #Solve for catenary constant a to create rope formula
    def equation(a):
        return 2 * a * np.sinh(distance/(2 * a)) - ropeLength
    a = fsolve(equation, distance/2 )[0]

    # Generate spacings
    particles = np.linspace(0, distance, num_points)
    
    # Catenary curve equation
    catenary_y = a * np.cosh((particles - distance/2) / a) - a

    # Adjust the catenary to pass through the endpoints
    y_shift = xy1[1] - catenary_y[0]
    catenary_y += y_shift

    # Rotate and shift the curve to match the endpoints
    angle = np.arctan2(xy2[1]-xy1[1], xy2[0]-xy1[0])
    particle_x = xy1[0] + particles * np.cos(angle) - catenary_y * np.sin(angle)
    particle_y = xy1[1] + particles * np.sin(angle) + catenary_y * np.cos(angle)

    return particle_x, particle_y
