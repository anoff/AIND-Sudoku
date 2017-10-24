assignments = []

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
    # Eliminate the naked twins as possibilities for their peers

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

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
    boxes = cross("ABCDFEGHI", "123456789")
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
    pass

def unitlist():
    """
    return list of units that belong together
    """
    rows = 'ABCDEFGHI'
    cols = '123456789'
    row_units = [cross(r, cols) for r in rows]
    column_units = [cross(rows, c) for c in cols]
    square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
    return row_units + column_units + square_units

def peers():
    """
    return peers dictionary
    taken from lesson 🙄
    """
    rows = 'ABCDEFGHI'
    cols = '123456789'
    boxes = cross(rows, cols)
    units = dict((s, [u for u in unitlist() if s in u]) for s in boxes)
    return dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)

def narrow_down_possibilities(values):
    """
    find boxes with only one value
    delete this from all it's peers
    """
    for box in [b for b in values.keys() if len(values[b]) == 1]:
        digit = values[box]
        for peer in peers()[box]:
            values = assign_value(values, box, values[peer].replace(digit, ""))
    return values

def assign_explicits(values):
    """
    if there is only one possible position for a value in a unit -> assign it
    """
    for unit in unitlist():
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
    def count_solved_boxes(values):
        return len([b for b in values.keys() if len(values[b] == 1)])
    improved = True
    while improved:
        improved = False
        previous = values
        values = assign_explicits(values)
        values = narrow_down_possibilities(values)
        if len([b for b in values.keys() if len(values[b]) == 0]) > 0:
            return False
        elif count_solved_boxes(previous) != count_solved_boxes(values):
            improved = True
    return values

def search(values):
    """
    recursively solve possible variations by assuming values in inexplicit boxes
    return False if unsolvable
    return values if solved
    """
    values = reduce_puzzle(values)
    if values == False:
        return False
    if len([b for b in values.keys() if len(values[b] > 1)]) == 0:
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

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
