# Josh Moody Computing 2
# Created 05/10/2018
#Last edit 05/10/2018



from copy import deepcopy  # copy 'target' to avoid modifying it
import utils  # it might be helpful to use 'utils.py'


def Tetris(target, limit_tetris):

	#blank solution:

	M = target
	for i in range(len(M)):
		for j in range(len(M[0])):
			M[i][j] = (0, 0)

	#main loop to place pieces

	while not all(value == 0 for value in limit_tetris.values()):    ##loops as long as there are still pieces left to place
		for key in limit_tetris:         #for each type of piece in the dictionary
			if limit_tetris[key] != 0:		#if there's a piece of that type left then...
				



	return M

