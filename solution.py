assignments = []

rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonals = [[rows[i]+cols[i] for i in range(9)], [rows[i]+cols[8-i] for i in range(9)]]
unitlist = row_units + column_units + square_units + diagonals
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    for box in [b for b in values.keys() if len(values[b]) == 2]: # all boxes with 2 digits
        twins = [b for b in peers[box] if values[b] == values[box]]
        for twin in twins:
            peers_1 = peers[box]
            peers_2 = peers[twin]
            joined_peers = [b for b in peers_1 if b in peers_2 if len(values[b]) > 1]
            for peer in joined_peers:
#                print(values[box], values[peer], values[peer].replace(values[box][0], ""), values[peer].replace(values[box][0], "").replace(values[box][1], ""))
                if len(values[peer]) > 2:
                    values = assign_value(values, peer, values[peer]
                                          .replace(values[box][0], "").replace(values[box][1], ""))
    return values

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value,
                then the value will be '123456789'.
    """
    if (type(grid) == type({})):
        return grid
    d = dict(zip(boxes, grid))
    for k, v in d.items():
        if v == ".":
            d[k] = "123456789"
    return d

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in values.keys())
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def narrow_down_possibilities(values):
    """
    find boxes with only one value
    delete this from all it's peers
    """
    for box in [b for b in values.keys() if len(values[b]) == 1]:
        digit = values[box]
        for peer in peers[box]:
            values = assign_value(values, peer, values[peer].replace(digit, ""))
    return values

def assign_explicits(values):
    """
    if there is only one possible position for a value in a unit -> assign it
    """
    for unit in unitlist:
        for number in "123456789":
            box_with_number = [box for box in unit if number in values[box]]
            if len(box_with_number) == 1:
                values = assign_value(values, box_with_number[0], number)
    return values

def reduce_puzzle(values):
    """
    iterate over the puzzle until no boxes change
    if completed or stalled return the list of values
    if unsolvable (box without values) return False
    """
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = narrow_down_possibilities(values)
        values = naked_twins(values)
        values = assign_explicits(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    """
    recursively solve possible variations by assuming values in inexplicit boxes
    return False if unsolvable
    return values if solved
    """
    values = reduce_puzzle(values)
    if not values:
        return False
    if not [b for b in values.keys() if len(values[b]) > 1]: # no boxes with multiple digits
        return values
    # find an unsolved (>1) box with the least amount of possible digits
    _, box = min([(len(values[b]), b) for b in values.keys() if len(values[b]) > 1])
    for digit in values[box]:
        sudoku_star = values.copy()
        sudoku_star[box] = digit
        result = search(sudoku_star)
        if result: # not False (= unsolvable)
            return result

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    return search(values)

if __name__ == '__main__':
#    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
#    diag_sudoku_grid = "9.1....8.8.5.7..4.2.4....6...7......5..............83.3..6......9................"
    sudoku = {"I6": "23678", "D4": "1", "F6": "37", "E6": "4", "B7": "2345678",
        "E4": "2", "B2": "1234568", "D1": "36", "C2": "1234568", "G8":
        "345678", "I1": "2345678", "G1": "23456789", "H5": "23456789", "B1":
        "2345689", "H7": "2345678", "F7": "58", "A5": "1", "C9": "124578",
        "A8": "345689", "E2": "567", "H3": "1234569", "I8": "345678", "B3":
        "1234569", "I5": "2345678", "I7": "1", "A7": "234568", "C7":
        "2345678", "E5": "678", "F1": "1", "I3": "23456", "D6": "5", "C3":
        "1234569", "A9": "2458", "G6": "1236789", "D7": "47", "G9": "24578",
        "E3": "56", "E7": "9", "C5": "23456789", "D3": "8", "B5": "23456789",
        "A2": "234568", "H6": "1236789", "H2": "12345678", "H1": "23456789",
        "D9": "47", "D8": "2", "G7": "2345678", "E9": "3", "H4": "345678",
        "B8": "3456789", "G4": "345678", "B4": "345678", "A4": "34568", "F5":
        "37", "G3": "1234569", "C6": "236789", "C8": "3456789", "G5":
        "23456789", "D2": "9", "G2": "12345678", "B6": "236789", "A1":
        "2345689", "I9": "9", "B9": "124578", "F9": "6", "E1": "567", "C4":
        "345678", "A6": "23689", "F3": "24", "A3": "7", "E8": "1", "D5": "36",
        "F8": "58", "H8": "345678", "F2": "24", "H9": "24578", "I4": "345678",
        "F4": "9", "C1": "2345689", "I2": "2345678"}
    print("input:")
    display(sudoku)
    print("\nsolution:")
    display(solve(sudoku))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
