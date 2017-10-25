# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Identify naked twins by checking for identical two digits in two peers. Propagate the constraint that these digits may not appear in any peers that the two twins have in common (inner join each peers)

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Include the diagonals into the units list

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - Fill in the required functions in this file to complete the project.
* `test_solution.py` - You can test your solution by running `python -m unittest`.
* `PySudoku.py` - This is code for visualizing your solution.
* `visualize.py` - This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the `assign_value` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login) for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

## Problemo 🔥🔥

Unit Test and PA fails because my solution is incorrect. PA says
>Not all of the tests passed.  Let me see what I can do to help.

>Your submission failed a test that sees whether the solve method
produces a valid solution.  One of the original values was changed.
Try your code on the following example:

>9.1....8.8.5.7..4.2.4....6...7......5..............83.3..6......9.....
...........

However running a solve on the above code shows that no original values of the input were modified in the solution.

```
▶ python solution.py
input:
    9   .   1|.   .   . |.   8   .
    8   .   5|.   7   . |.   4   .
    2   .   4|.   .   . |.   6   .
   ----------+----------+---------
    .   .   7|.   .   . |.   .   .
    .   .   .|.   .   . |8   3   .
    5   .   .|.   .   . |.   .   .
   ----------+----------+---------
    3   .   .|6   .   . |.   .   .
    .   9   .|.   .   . |.   .   .
    .   .   .|.   .   . |.   .   .

solution:
9 6 1 |4 5 5 |7 8 3
8 3 5 |9 7 6 |2 4 1
2 7 4 |8 1 3 |5 6 9
------+------+------
6 4 7 |2 3 8 |9 1 5
1 2 9 |5 6 4 |8 3 7
5 8 3 |1 9 7 |4 2 6
------+------+------
3 5 2 |6 8 9 |1 7 4
4 9 6 |7 2 1 |3 5 8
7 1 8 |3 4 2 |6 9 5
```