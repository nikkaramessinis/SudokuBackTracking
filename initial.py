import numpy as np
import copy

def sudoku_solver(sudoku):
    solved_sudoku = copy.deepcopy(sudoku)
    rows = np.zeros([9, 9]).astype(int)
    columns = np.zeros([9, 9]).astype(int)
    sub_boxes = np.zeros([9, 9]).astype(int)
    num_of_filled = 0
    for x in range(0, 9):
        for y in range(0, 9):
            if (solved_sudoku[x][y]) != 0:
                num_of_filled += 1
                if rows[x][solved_sudoku[x][y] - 1] == 1 or columns[y][solved_sudoku[x][y] - 1] == 1 or \
                        sub_boxes[(y // 3) * 3 + x // 3][solved_sudoku[x][y] - 1] == 1:
                    return np.full((9, 9), -1)
                rows[x][solved_sudoku[x][y] - 1] = columns[y][solved_sudoku[x][y] - 1] = sub_boxes[(y // 3) * 3 + x // 3][solved_sudoku[x][y] - 1] = 1
    board = dfs(solved_sudoku, num_of_filled, rows, columns, sub_boxes)[1]
    if 0 in board:
        return np.full((9, 9), -1)
    return board


def find_common_zeros(board, rows, columns, sub_boxes):
    best = ([], 0, 0)
    chosen_x = chosen_y = 0
    for x in range(0, 9):
        for y in range(0, 9):
            candidates = []
            if (board[x][y]) != 0:
                continue
            for k in range(0, 9):
                if rows[x][k] == columns[y][k] == sub_boxes[(y // 3) * 3 + x // 3][k] == 0:
                    candidates.append(k + 1)
                    chosen_x = x
                    chosen_y = y
            if len(candidates) == 1 or len(candidates) == 0:
                return candidates, chosen_x, chosen_y
            # if there is none initialized or if current candidates found are less than before
            if len(best[0]) == 0 or len(best[0]) > len(candidates):
                best = (candidates, chosen_x, chosen_y)
    return best

def dfs(board, num_of_filled, rows, columns, sub_boxes):
    if num_of_filled == 81:
        return True, board
        best = None
    candidates, x, y = find_common_zeros(board, rows, columns, sub_boxes)
    for cand in candidates:
        board[x][y] = cand
        rows[x][cand - 1] = columns[y][cand - 1] = sub_boxes[(y // 3) * 3 + x // 3][cand - 1] = 1
        num_of_filled += 1
        if dfs(board, num_of_filled, rows, columns, sub_boxes)[0]:
            return True, board
        board[x][y] = rows[x][cand - 1] = columns[y][cand - 1] = sub_boxes[(y // 3) * 3 + x // 3][cand - 1] = 0
        num_of_filled -= 1
    return False, board


SKIP_TESTS = False

if not SKIP_TESTS:
    import time

    difficulties = ['very_easy', 'easy', 'medium', 'hard']

    for difficulty in difficulties:
        print(f"Testing {difficulty} sudokus")

        sudokus = np.load(f"data/{difficulty}_puzzle.npy")
        solutions = np.load(f"data/{difficulty}_solution.npy")

        count = 0
        for i in range(len(sudokus)):
            sudoku = sudokus[i].copy()
            print(f"This is {difficulty} sudoku number", i)
            print(sudoku)

            start_time = time.process_time()
            your_solution = sudoku_solver(sudoku)
            end_time = time.process_time()

            print(f"This is your solution for {difficulty} sudoku number", i)
            print(your_solution)

            print("Is your solution correct?")
            if np.array_equal(your_solution, solutions[i]):
                print("Yes! Correct solution.")
                count += 1
            else:
                print("No, the correct solution is:")
                print(solutions[i])

            print("This sudoku took", end_time - start_time, "seconds to solve.\n")

        print(f"{count}/{len(sudokus)} {difficulty} sudokus correct")
        if count < len(sudokus):
            break
