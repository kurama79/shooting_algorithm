# Funcion para graficar

import matplotlib.pyplot as plt

def show_shoot(evader, pursuit, xe):

	fig, ax = plt.subplots()
	ax.plot(evader[0][0], evader[0][1], 'o', color='blue', lw=3)
	ax.text(evader[0][0], evader[0][1]+0.05, 'x_0', fontsize=10)

	ax.plot(xe, 0, 'o', color='black', lw=3)
	ax.text(xe, 0.05, 'x_e', fontsize=10)

	for index, pos_ev in enumerate(evader):

		if (index%8) == 0:

			ax.plot([pos_ev[0], pursuit[index][0]], [pos_ev[1], pursuit[index][1]], color='orange')
			ax.plot(pos_ev[0], pos_ev[1], 'o', color='green', lw=2)
			ax.plot(pursuit[index][0], pursuit[index][1], 'o', color='red', lw=2)

	plt.show()