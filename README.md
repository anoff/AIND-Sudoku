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

PA fails because my code produced an `unexpected board`. Running the code locally returns a valid board though

```
▶ python solution.py
input:
 2345689   234568     7    |  34568      1      23689  |  234568   345689    2458
 2345689  1234568  1234569 |  345678  23456789  236789 | 2345678  3456789   124578
 2345689  1234568  1234569 |  345678  23456789  236789 | 2345678  3456789   124578
---------------------------+---------------------------+---------------------------
    36       9        8    |    1        36       5    |    47       2        47
   567      567       56   |    2       678       4    |    9        1        3
    1        24       24   |    9        37       37   |    58       58       6
---------------------------+---------------------------+---------------------------
 23456789 12345678 1234569 |  345678  23456789 1236789 | 2345678   345678   24578
 23456789 12345678 1234569 |  345678  23456789 1236789 | 2345678   345678   24578
 2345678  2345678   23456  |  345678  2345678   23678  |    1      345678     9

solution:
4 3 7 |5 1 9 |6 8 2
9 6 1 |3 2 8 |7 4 5
8 5 2 |6 4 7 |3 9 1
------+------+------
3 9 8 |1 6 5 |4 2 7
6 7 5 |2 8 4 |9 1 3
1 2 4 |9 7 3 |8 5 6
------+------+------
2 4 6 |7 9 1 |5 3 8
5 1 9 |8 3 6 |2 7 4
7 8 3 |4 5 2 |1 6 9
We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.
```