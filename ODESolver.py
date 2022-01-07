import numpy as np


class ODESolver:
    """ODESolver superclass

    Any classes inheriting from this superclass must implement
    advance() method

    """

    def __init__(self, f):
        self.f = f
        # takes in the model

    def advance(self):
        """Advance solution on time step."""
        raise NotImplementedError
        # main method of this class
        # """We will implement this in a subclass so this will be
        # the parent class ."""

    def set_initial_conditions(self, U0):
        if isinstance(U0, (int, float)): # if we only get one number int or float
            # Scalar ODE
            self.number_of_eqns = 1
            U0 = float(U0)
        else:
            # System of equations
            U0 = np.asarray(U0)
            self.number_of_eqns = U0.size
        self.U0 = U0 # store within class

    def solve(self, time_points):

        self.t = np.asarray(time_points)
        n = self.t.size

        self.u = np.zeros((n, self.number_of_eqns))

        self.u[0, :] = self.U0

        # Integrate
        for i in range(n -1):
            self.i = i
            self.u[i + 1] = self.advance()

        return self.u[:i + 2], self.t[:i + 2]

class ForwardEuler(ODESolver):
    # Integrator?
    def advance(self):
        u, f, i, t, = self.u, self.f, self.i, self.t
        dt = t[i + 1] - t[i]
        return u[i, :] + dt * f(u[i, :], t[i])
