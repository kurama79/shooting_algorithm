# Shotting Algorithm Class

import numpy as np
from copy import copy

class shooting_algorithm:
    def __init__(self, lambdas, theta, x, y, rho, L, xe):

    	# Parametros iniciales del algoritmo
        self.lambdas = lambdas
        self.theta = [theta]
        self.j = 0.0
        self.L = L
        self.rho = rho
        self.states = [[x, y]]
        self.xe = xe

    def shoot_iteration(self, dx):

        # Se obtiene el alpha que minimza el Hamiltoniano
        alpha = self.get_alpha_minimizer()

        # Se integran las ecuacion de la evoluscion de los esatdos para obtener los siguientes estados
        [x, y, theta] = self.states_integration(dx, alpha)

        # Agregando en los arreglos
        self.states.append([x, y])
        self.theta.append(theta)

        # Solucion de la ecuacion adjunta para obtener lambda_2(j+1)
        self.adjoint_equation(dx, alpha)

        # Condiciones para determinar finzalizacion del algortimo
        if np.sign(self.states[-2][1]) == np.sign(self.states[-1][1]):
            return 'Not'

        else:

            if np.abs(self.states[-1][0] - self.xe) < 0.01:
                return 'Reached'

            elif np.abs(self.states[-1][0] - self.states[-2][0]) > 0.01:
                return 'Missed'

    # Funcion para encontrar el alpha que minimice el Hamiltoniano
    def get_alpha_minimizer(self):

        # alphas = np.linspace(-np.pi/2, np.pi/2, 1000)
        alphas = np.linspace(-np.pi/2, np.pi/2, 1000)
        min_cost = np.inf 

        for alpha in alphas:

            cost = self.hamiltonian(alpha)

            if cost < min_cost:

                min_cost = cost
                alpha_minimizer = alpha

        return alpha_minimizer

    # Hamiltoniano para obtener el costo dada un control - alpha
    def hamiltonian(self, alpha):

        H = self.lambdas[0]*np.tan(alpha) + (1 + self.lambdas[1])*((-self.rho*np.sin(alpha - self.theta[-1]) +
            np.sqrt(1 - (self.rho**2)*(np.cos(alpha - self.theta[-1])**2)))/(self.L*self.rho*np.cos(alpha)))

        return H

    # Integrando las ecaucion de evolucion de los estados para obtener el siguiente estado
    def states_integration(self, dx, alpha):

        x = self.states[-1][0] + dx
        y = self.states[-1][1] + np.tan(alpha)*dx
        theta = self.theta[-1] + ((-self.rho*np.sin(alpha - self.theta[-1]) + np.sqrt(1 - (self.rho**2)*(np.cos(alpha - self.theta[-1])**2)))/
                      (self.L*self.rho*np.cos(alpha)))*dx

        return x, y, theta

    # Solucion a la ecuacion adjunta para lambda_2
    def adjoint_equation(self, dx, alpha):

        self.lambdas[1] += (-(1 + self.lambdas[1])*(np.cos(alpha - self.theta[-1])/(self.L*np.cos(alpha)))*(1 - (self.rho*np.sin(alpha - self.theta[-1])/
                           np.sqrt(1 - (self.rho**2)*(np.cos(alpha - self.theta[-1])**2)))))*dx