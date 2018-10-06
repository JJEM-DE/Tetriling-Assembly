# Josh Moody Computing 2
# Created 05/10/2018
#Last edit 05/10/2018



from copy import deepcopy  # copy 'target' to avoid modifying it
import utils  # it might be helpful to use 'utils.py'


def Tetris(target, limit_tetris):

	n = 1 #piece ID


	#blank solution:

	M = deepcopy(target)
	for i in range(len(M)):
		for j in range(len(M[0])):
			M[i][j] = (0, 0)

	##########main loop to place pieces############

	##looks for places only certain pieces can be placed







	##an approach of going piece by piece finding a spot for each one as you go
	while not all(value == 0 for value in limit_tetris.values()):    ##loops as long as there are still pieces left to place
		for key in limit_tetris:         #for each type of piece in the dictionary
			print("Key: {0}".format(key))
			if limit_tetris[key] != 0:		#if there's a piece of that type left then...
				print("Wooo!!! I'm here! The key is {0}. n = {1}".format(key, n))
				print(limit_tetris)
				shape = utils.generate_shape(key)
				for i in range(len(M)):     #check each space in the grid
					for j in range(len(M[0])):   #check each space in the grid
						print("I'm here! The key is {0}, i = {1} and j = {2}. n = {3}".format(key, i, j, n))
						if target[i][j] == 1 and limit_tetris[key] !=0 :
							print("I've got here now!")
							try:        # To fix index error
								if target[i+shape[1][0]][j+shape[1][1]] == 1 and target[i+shape[2][0]][j+shape[2][1]] == 1 and target[i+shape[3][0]][j+shape[3][1]] == 1  :      #check if the shape fits




										#place shape into M:
										M[i][j] = (key, n)
										M[i+shape[1][0]][j+shape[1][1]] = (key, n)
										M[i + shape[2][0]][j + shape[2][1]] = (key, n)
										M[i+shape[3][0]][j+shape[3][1]] = (key, n)


										n += 1   #increase shapeID

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

