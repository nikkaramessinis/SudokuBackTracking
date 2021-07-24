# SudokuBackTracking
IMPORTANT! FINAL IMPLEMENTATION IS IN JUPYTER
INITIAL.PY was a worse timewise attempt

Functions: 

sudoku_solver(sudoku) 
	Parameter sudoku 9*1 arrays of ints 

	Initialized three new arrays one for rows, one for columns and one for the 3*3 sub cells.
	It's one of those marks the existance or not (0,1) of an element 
	e.g
	if the row is  3 4 5 0 0 1 2 8 6 then the row bitset will be 
	111111010 since only the 7 and 9 are missing. 111111010 translates to a number but since we're gonna always do 
	bitwise operations we don't really care what the decimal representation is. More useful on the binary one
	 

	 or a column 
	 3 
	 4
	 5 
	 0
	 0
	 1 
	 2
	 8
	 6
	 
	 Same array would exist for a subcell 
	 3 4 5 
	 0 0 1 
	 2 8 6
	 For the 3*3 sub cells from 0 till 2 x and 0 till 2 y is the first sub call from 3 till 5 x and 0 till 2 y is the second and so on and so forth. 
	 So to put the corresponding sub cell to the corresponding rows we need to do this trick  
	 (y // 3)* 3 +x //3
	 For example 
	 
	 if try the fourth sub cell 
	 which spans on 0 till 2 x and 3 till 5 y 
	 lets say cell (1,3)
	 (3//3)*3+1//3 = 1*3 + 0 = 3
	 So the fourth row since arrays start from 0. 
	 This serves the every cell and the whole array.
	 
	 
	 
	 So these two for-loops propagate the whole array (suduko) and fill the new ones. This operation takes O(n^2). 
	 
	 
	 In detail 
	 if e.g. 3 is already filled then the sudoku is invalid
     To check that, we want to make a bitwise and operation with the existing  number.
     so then if for example in the bitset the number already exists this will result in the number itself.
	 So for example a 9,7,6,5,3,2,1 the number would be 101111011
     adding it with a bitwise and operation with 100(the 3 number has occured) would result in 100 meaning a 3 already exists in.
	 Else it would result in 0. 
	 
	 
	 if e.g. 3 occured in the sudoku then we want to fill the 3rd bit 100
     so then if for example in the bitset already exists a 9,7,6,5,2,1 the number would be 101110011
     adding  it with a bitwise or operation would result in 101111011 meaning a 3 exists in that row/column/subbox
 
	 Then we call dfs 
	 If the board has a zero in it then the is no valid solution and we should return a board of -1s 
	 Else return board
 
def dfs(board, rows, columns, sub_boxes):
	parameters 
	board 9*9 array_of_ints 
	rows size 9 array of occurence of a number (explained already)
	columns size 9 array of occurence of a number (explained already)
	sub_boxes size 9 array of occurence of a number (explained already)

	 
	checks whether the counter for non zero cells is 81 
	if so we already have a solution 

	then we call find_common_zeros which returns either a solution 
	for a cell or the lesser number of candidates that first occured in that sudoku ( hopefully this will prevent us from doing that many speculations) 
	Then having that list of candidates we pick the first one as if it was the correct one and call dfs for that one. This then returns other candidates 
	again picking the first one which calls dfs etc etc constructing a tree of decisions. if the first of the first of the first ....etc decision is False 
	we erase that last choice and check the first of the first of the .... of the second check if that is true . Going for all candidates in that last choice of choices.
	If that all last choices are invalid we go back one choice ... And so on and so forth until we find that right choice which fills all the cells. This is essentially an explanation 
	of how the backtracking propagation works. To undo our operation we just take the 1111111 number and subtracting our current selection. Adding this to the rows, columns would result in 
	"erasing" zeroing essentially the number that we pointed as being a 1 before.


def find_common_zeros(board, rows, columns, sub_boxes):
	is a two for loop which searches for the best next solution checking for the all the zero values
	Checking what already exists everywhere in the row, column, subcell for that element
	if there is a 0 then this means this position is a common non filled value
	if there is one single common solution for a cell. If not then return the second best you found.
	
	
def get_candidates(common_values):
	get_candidates check for every bit whether is a 0 or a 1. If this is a zero push it to the candidates list
	(common_values & 1) gets rid of all the bits just getting the first one 100010101 & 1 = 1 or 100010100 & 1  = 0
	Then its time we are doing a bitwise shift division meaning one element to the left
	
	
Going Beyond:
Initial Implementation was with lists instead of bitset operations which would result in worse results timewise. (Implementation is shown in initial.py)
But trying with bitwise operations gave us O(n^2) times where it was O(n^3) in some functions before. 




 
 
