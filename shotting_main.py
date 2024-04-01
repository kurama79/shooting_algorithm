'''
Tarea 6 - Shooting Algorithm.
    Implementar el algortimo shooting para juego de persecusion y evasion con el metodo de 
    optimizacion PMP.
'''

import numpy as np

from shooting_alg import shooting_algorithm
from plot_all import show_shoot


if __name__ == "__main__":

    # Parametros del probelma 
    v_e = 1
    v_p = 2
    rho = v_e / v_p
    L = 1.0
    x_e = 1.0
    lambdas = [-1.0, 0.41]
    dx = 0.01

    # Condiciones inciales del evasor
    theta = np.pi
    x = 0
    y = 0

    shoot = shooting_algorithm(lambdas, theta, x, y, rho, L, x_e)

    iteration = 0
    max_iterations = int((x_e/dx)*1.5)
    solved = 'Not'
    while solved != 'Reached' and solved != 'Missed':

        solved = shoot.shoot_iteration(dx)

        if solved == 'Reached' or solved == 'Missed':
            print('Termino el algoritmo y el estado fue: ', solved)

        if iteration > max_iterations:

            print('No se encontro solucion')
            break

        iteration += 1

    # Posiciones del perseguidor 
    pusrsuit_states = []
    for index, state in enumerate(shoot.states):

        x = state[0] + L*np.cos(shoot.theta[index])
        y = state[1] + L*np.sin(shoot.theta[index])

        pusrsuit_states.append([x, y])
    
    # Mostramos el resultado del algoritmo
    show_shoot(shoot.states, pusrsuit_states, x_e)