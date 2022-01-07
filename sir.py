"""

SIR disease model

Youtube References:
Part 1/2: https://www.youtube.com/watch?v=mwJXjxMTwAw
Part 2/2: https://www.youtube.com/watch?v=MJlKfaU206Q&t=0s


S' = -beta*S*I, susceptible people in contact with infected people
I' = beta*S*I - nu*I, + infected people recovering
R' = nu*I, people recovering
"""

import numpy as np
from ODESolver import ForwardEuler
from matplotlib import pyplot as plt

class SIR:
    def __init__(self, nu, beta, S0, I0, R0):
        """
        nu, beta: parameters in the ODE system
        S0, I0, R0: initial values
        """

        # making the transmission rates vary with time
        # check if float, int, or is it a function?
        if isinstance(nu, (float, int)):
            self.nu = lambda t: nu  # make it a function (for any t get nu)
        elif callable(nu):
            self.nu = nu

        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta

        # need to store initial conditions
        self.initial_conditions = [S0, I0, R0]

    def __call__(self, u, t):

        S, I, _ = u

        return np.asarray([
            -self.beta(t)*S*I, # Susceptibles
            self.beta(t)*S*I - self.nu(t)*I, # Infected
            self.nu(t)*I # Recovered
        ])

if __name__ == "__main__":

    beta = lambda t: 0.0005 if t <=10 else 0.0001  # make tranmission rate a function
    # Transmission rate goes down by 5x. After 10 days ppl start washing their hands

    sir = SIR(0.1, beta, 1500, 1, 0)
    solver = ForwardEuler(sir)
    solver.set_initial_conditions(sir.initial_conditions)

    time_steps = np.linspace(0,60,1001)
    u, t, = solver.solve(time_steps)

    plt.plot(t, u[:, 0], label="Susceptible")
    plt.plot(t, u[:, 1], label="Infected")
    plt.plot(t, u[:, 2], label="Recovered")
    plt.legend()
    plt.show()
