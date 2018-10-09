# Josh Moody Computing 2
# Created 05/10/2018
#Last edit 05/10/2018



from copy import deepcopy  # copy 'target' to avoid modifying it
import utils  # it might be helpful to use 'utils.py'


def Tetris(target, limit_tetris):

	n = 1 #piece ID
	shapeID = 0


	#blank solution:

	M = deepcopy(target)
	for i in range(len(M)):
		for j in range(len(M[0])):
			M[i][j] = (0, 0)


	J = deepcopy(target)   # Array for placing in weights


	for i in range(len(J)):
		for j in range(len(J[0])):
			




	##########main loop to place pieces############


	##an approach of going piece by piece finding a spot for each one as you go
	while not all(value == 0 for value in limit_tetris.values()):    ##loops as long as there are still pieces left to place
		for key in limit_tetris:         #for each type of piece in the dictionary
			print("Key: {0}".format(key))
			if limit_tetris[key] != 0:		#if there's a piece of that type left then...
				print("Wooo!!! I'm here! The key is {0}. n = {1}.".format(key, n))
				print(limit_tetris)
				shape = utils.generate_shape(key)
				for i in range(len(M)):     #check each space in the grid
					for j in range(len(M[0])):   #check each space in the grid
						print("I'm here! The key is {0}, i = {1} and j = {2}. PieceID = {3}. ShapeID = {4}".format(key, i, j, n, shapeID))

						##if weight =3




						if target[i][j] == 1 and limit_tetris[key] !=0 :
							print("I've got here now!")
							try:        # To fix index error
								if target[i+shape[1][0]][j+shape[1][1]] == 1 and target[i+shape[2][0]][j+shape[2][1]] == 1 and target[i+shape[3][0]][j+shape[3][1]] == 1  :      #check if the shape fits
									print("Results from checking if shape fits: ({0}, {1}), ({2}, {3}), ({4}, {5}), ({6}, {7})".format(i, j, i+shape[1][0], j+shape[1][1], i+shape[2][0], j+shape[2][1], i+shape[3][0], j+shape[3][1]))
									if j+shape[1][1] < 0 or j+shape[2][1] < 0 or j+shape[2][1] < 0 :
										print("Negative index error")
										break

									###debugging


									shapeID = limit_tetris[key]




									###end of debugging





									#place shape into M:
									M[i][j] = (key, n)
									M[i+shape[1][0]][j+shape[1][1]] = (key, n)
									M[i + shape[2][0]][j + shape[2][1]] = (key, n)
									M[i+shape[3][0]][j+shape[3][1]] = (key, n)


									n += 1   #increase pieceID

									#remove the 1s from target:

									target[i][j] = 0
									target[i + shape[1][0]][j + shape[1][1]] = 0
									target[i + shape[2][0]][j + shape[2][1]] = 0
									target[i + shape[3][0]][j + shape[3][1]] = 0

									#remove the piece from the limit_tetris
									print(limit_tetris[key])
									limit_tetris[key] = limit_tetris[key] - 1

							except IndexError:
								pass







		return M

