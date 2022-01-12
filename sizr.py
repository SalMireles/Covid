"""

SIZR disease model - Humans are infected or killed by zombies. Zombies can
also be killed by humans.

Youtube Reference:
Part 2/2: https://www.youtube.com/watch?v=MJlKfaU206Q&t=0s

S' = sigma - beta*S*Z - delta_S*S, human - becoming zombie - dying
I' = beta*S*Z - rho*I - delta_I*I, s infected - infected becoming zombie - infected dying
Z' = rho*I - alpha*S*Z, infected becoming zombies OR humans becoming zombies
R' = delta_S*S + delta_I*I + alpha*S*Z, people dying - by z killing s, infected, or s killing z
"""

import numpy as np
from matplotlib import pyplot as plt
from ODESolver import ForwardEuler

class SIZR:
    def __init__(self, sigma, beta, rho, delta_S, delta_I, alpha, S0, I0, Z0, R0)
        """
        The Zombie Class

        initial value: S0, I0, Z0, R0
        """
        if isinstance(sigma, (float, int)):
            self.sigma = lambda t: sigma
        elif callable(sigma):
            self.sigma = sigma
        #TODO review updated code
        # https://github.com/gregwinther/youtube/blob/master/disease_simulations/sizr.py
