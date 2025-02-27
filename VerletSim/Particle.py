class Particle:
    def __init__(self, mass, x, y, xVel = 0, yVel = 0, xAcc = 0, yAcc = 0, fixed = False):
        self.mass = mass

        self.xAcc, self.yAcc = xAcc, yAcc
        self.x, self.y = x, y
        self.oldX = x - xVel * self.simulation.timeStep
        self.oldY = y - yVel * self.simulation.timeStep
        
        
        self.fixed= fixed

    def update(self):
        if not self.pinned:
            self.physicsStep()

    def physicsStep(self,forces):
        # Verlet integration is
        # x(t+dt) = 2*x(t) - x(t-dt) + a*(dt**2)
        self.xAcc = forces[0]/self.mass+self.xAcc
        self.yAcc = forces[1]/self.mass+self.yAcc
        self.x = 2*self.x - self.oldX + self.xAcc * (self.simulation.timeStep**2)
        self.y = 2*self.y - self.oldY + self.yAcc * (self.simulation.timeStep**2)

    
