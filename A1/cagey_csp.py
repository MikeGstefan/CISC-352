# =============================
# Student Names: Calvin Birch, Mike Stephen, Cooper Moses 
# Group ID: 11
# Date: 2025-01-30
# =============================
# CISC 352 - W23
# cagey_csp.py
# desc: Implement CSP models for Cagey puzzles
#

import cspbase
import itertools

#Look for #IMPLEMENT tags in this file.
'''
All models need to return a CSP object, and a list of lists of Variable objects
representing the board. The returned list of lists is used to access the
solution.

For example, after these three lines of code

    csp, var_array = binary_ne_grid(board)
    solver = BT(csp)
    solver.bt_search(prop_FC, var_ord)

var_array is a list of all Variables in the given csp. If you are returning an entire grid's worth of Variables
they should be arranged linearly, where index 0 represents the top left grid cell, index n-1 represents
the top right grid cell, and index (n^2)-1 represents the bottom right grid cell. Any additional Variables you use
should fall after that (i.e., the cage operand variables, if required).

1. binary_ne_grid (worth 0.25/3 marks)
    - A model of a Cagey grid (without cage constraints) built using only
      binary not-equal constraints for both the row and column constraints.

2. nary_ad_grid (worth 0.25/3 marks)
    - A model of a Cagey grid (without cage constraints) built using only n-ary
      all-different constraints for both the row and column constraints.

3. cagey_csp_model (worth 0.5/3 marks)
    - a model of a Cagey grid built using your choice of (1) binary not-equal, or
      (2) n-ary all-different constraints for the grid, together with Cagey cage
      constraints.


Cagey Grids are addressed as follows (top number represents how the grid cells are adressed in grid definition tuple);
(bottom number represents where the cell would fall in the var_array):
+-------+-------+-------+-------+
|  1,1  |  1,2  |  ...  |  1,n  |
|       |       |       |       |
|   0   |   1   |       |  n-1  |
+-------+-------+-------+-------+
|  2,1  |  2,2  |  ...  |  2,n  |
|       |       |       |       |
|   n   |  n+1  |       | 2n-1  |
+-------+-------+-------+-------+
|  ...  |  ...  |  ...  |  ...  |
|       |       |       |       |
|       |       |       |       |
+-------+-------+-------+-------+
|  n,1  |  n,2  |  ...  |  n,n  |
|       |       |       |       |
|n^2-n-1| n^2-n |       | n^2-1 |
+-------+-------+-------+-------+

Boards are given in the following format:
(n, [cages])

n - is the size of the grid,
cages - is a list of tuples defining all cage constraints on a given grid.


each cage has the following structure
(v, [c1, c2, ..., cm], op)

v - the value of the cage.
[c1, c2, ..., cm] - is a list containing the address of each grid-cell which goes into the cage (e.g [(1,2), (1,1)])
op - a flag containing the operation used in the cage (None if unknown)
      - '+' for addition
      - '-' for subtraction
      - '*' for multiplication
      - '/' for division
      - '?' for unknown/no operation given

An example of a 3x3 puzzle would be defined as:
(3, [(3,[(1,1), (2,1)],"+"),(1, [(1,2)], '?'), (8, [(1,3), (2,3), (2,2)], "+"), (3, [(3,1)], '?'), (3, [(3,2), (3,3)], "+")])

'''

from cspbase import *
from math import prod

def binary_ne_grid(cagey_grid):
    ##IMPLEMENT
    n, cages = cagey_grid

    variables = [[None for _ in range(n)] for _ in range(n)]

    # Step 1: Disect the input and make variables for each cell (no variables for operator or cages because we ignore cage constraints)
    #print("step 1")
    for row in range(n):
        for col in range(n):
            #create a variable for each cell (name, domain(1 (inclusive) to n+1 (exclusive) ))
            #print(f"Cell({row},{col})")
            # print
            variables[row][col] = cspbase.Variable(f"Cell({row+1},{col+1})", [i for i in range(1, n+1)])
        
    #print("step 2")
    # Step 2: Create the CSP with the newly created variables
    flatVariables = [var for row in variables for var in row] # Convert 2D array to 1D array
  

    csp = cspbase.CSP("Binary csp", flatVariables)

    # print(csp.get_all_vars())

    # Step 3: Create constraints
    # binary not-equal constraints for both the row and column constraints.
    # 0,0 != 0,1, 0,0 != 0,2, 01 != 0,2 (for row 0) and so on for all rows and columns
    
    # print(len(variables))
    # print(len(variables[0]))
    # print(variables[2][2])
    #print("step 3.1")
    # Row constraints
    for row in range(n): # For all cells
        for j in range(n): # for every item in row
            for k in range(j+1, n): # create constraint with every other item in row
                constraint = cspbase.Constraint(f"Constraint({row+1},{j+1})-({row+1},{k+1})", [variables[row][j], variables[row][k]])
                # print("AHH",row, j,k, "bing" , [variables[row][j], variables[row][k]])
                # Generate all valid pairs of values
                satisfyingTuples = [(a, b) for a in range(1, n+1) for b in range(1, n+1) if a != b]
                # print(satisfyingTuples)
                constraint.add_satisfying_tuples(satisfyingTuples)
                # print(constraint.get_scope())
                csp.add_constraint(constraint)

    #print("step 3.2")
    # Column constraints
    for col in range(n): # For all cells
        for j in range(n): # for every item in column
            for k in range(j+1, n): # create constraint with every other item in column
                constraint = cspbase.Constraint(f"Constraint({j+1},{col+1})-({k+1},{col+1})", [variables[j][col], variables[k][col]])
                
                # Generate all valid pairs of values
                satisfyingTuples = [(a, b) for a in range(1, n+1) for b in range(1, n+1) if a != b]
                constraint.add_satisfying_tuples(satisfyingTuples)
                
                csp.add_constraint(constraint)
    
    return csp, flatVariables


def nary_ad_grid(cagey_grid):
    ## IMPLEMENT
    n, cages = cagey_grid

    variables = [[None for _ in range(n)] for _ in range(n)]

    # Step 1: Disect the input and make variables for each cell (no variables for operator or cages because we ignore cage constraints)
    #print("step 1")
    for row in range(n):
        for col in range(n):
            #create a variable for each cell (name, domain(1 (inclusive) to n+1 (exclusive) ))
            #print(f"Cell({row},{col})")
            # print
            variables[row][col] = cspbase.Variable(f"Cell({row+1},{col+1})", [i for i in range(1, n+1)])
        
    #print("step 2")
    # Step 2: Create the CSP with the newly created variables
    flatVariables = [var for row in variables for var in row] # Convert 2D array to 1D array

    csp = cspbase.CSP("Binary csp", flatVariables)

    # Step 3: Create constraints
    # instead of pairwise constraints, we use all diff for each row and column
    for row in range(n):
        constraint = cspbase.Constraint(f"RowConstraint({row+1})", [variables[row][i] for i in range(n)])

        # Add all satisfying tuples
        satisfyingTuples = list(itertools.permutations(range(1, n+1)))
        constraint.add_satisfying_tuples(satisfyingTuples)
        csp.add_constraint(constraint)

    for col in range(n):
        constraint = cspbase.Constraint(f"ColConstraint({col+1})", [variables[i][col] for i in range(n)])

        # Add all satisfying tuples
        satisfyingTuples = list(itertools.permutations(range(1, n+1)))
        constraint.add_satisfying_tuples(satisfyingTuples)
        csp.add_constraint(constraint)

    return csp, flatVariables

def cagey_csp_model(cagey_grid):
    ##IMPLEMENT

    csp, variables = nary_ad_grid(cagey_grid)
    has_guess = False


    n, cages = cagey_grid
    operations = ["+", "-", "*", "/", "?"]

    for cage in cages:
        value, cells, operator = cage

        scope = [variables[(cell[1]-1) + (n*(cell[0]-1))] for cell in cells]
        
        cage_variable = cspbase.Variable(f"Cage_op({value}:{operator}:{scope})", operations )
        csp.add_var(cage_variable)
        variables.append(cage_variable)
        scope.append(cage_variable)

        # print(variables)
        goodPerms = []
        constraint = cspbase.Constraint(f"Cage{value}", scope)
        
        if len(cells)==1:
            goodPerms.append((value))
            # constraint = cspbase.Constraint(f"Cage{value}+", scope)
            # constraint.add_satisfying_tuples((value))
            # csp.add_constraint(constraint)
        
        elif operator=='+' or operator=='?':
            # print("AHHHH")
            # all_perms = itertools.permutations([i for i in range(1, n+1)]*n, len(cells))
            all_perms = itertools.product([i for i in range(1, n+1)], repeat=len(cells))
            # print(cells)
            # print(all_perms)
            
            for perm in all_perms:
                # print(perm)
                if sum(perm) == value:
                    # tuple( list(perm).append('+'))
                    perm_list = list(perm)
                    perm_list.append('+')
                    goodPerms.append(perm_list)
                    has_guess = True

            # if len(goodPerms) != 0: 
            #     constraint = cspbase.Constraint(f"Cage{value}+", scope)
                
            #     constraint.add_satisfying_tuples(goodPerms)
            #     csp.add_constraint(constraint)

        elif operator=='-' or operator=='?':
            all_perms = itertools.product([i for i in range(1, n+1)], repeat=len(cells))
            # goodPerms=[]
            for perm in all_perms:
                print(perm)
                total=perm[0]
                for i in perm[1:]:
                    total-=i
                if total == value:
                    perm_list = list(perm)
                    perm_list.append('-')
                    goodPerms.append(perm_list)
                    has_guess = True
                    

            # if len(goodPerms) != 0: 
            #     constraint = cspbase.Constraint(f"Cage{value}-", scope)
                
            #     constraint.add_satisfying_tuples(goodPerms)
            #     csp.add_constraint(constraint)

        elif operator=='*' or operator=='?':
            all_perms = itertools.product([i for i in range(1, n+1)], repeat=len(cells))
            # goodPerms=[]
            for perm in all_perms:
                if prod(perm) == value:
                    perm_list = list(perm)
                    perm_list.append('*')
                    goodPerms.append(perm_list)
                    has_guess = True
                    
                
            # if len(goodPerms) != 0: 
            #     constraint = cspbase.Constraint(f"Cage{value}*", scope)
                
            #     constraint.add_satisfying_tuples(goodPerms)
            #     csp.add_constraint(constraint)

        elif operator=='/' or operator=='?':
            all_perms = itertools.product([i for i in range(1, n+1)], repeat=len(cells))

            # goodPerms=[]
            for perm in all_perms:
                total=perm[0]
                for i in perm[1:]:
                    if total%i != 0:
                        break
                    total/=i
                if total == value:
                    perm_list = list(perm)
                    perm_list.append('/')
                    goodPerms.append(perm_list)
                    has_guess = True
                    

            # if len(goodPerms) != 0:        
            #     constraint = cspbase.Constraint(f"Cage{value}/", scope)
                
            #     constraint.add_satisfying_tuples(goodPerms)
            #     csp.add_constraint(constraint)
        
        # if len(goodPerms) == 0 and operator != '?':
        #     constraint = cspbase.Constraint(f"No Answer", [])
                
        #     constraint.add_satisfying_tuples([])
        #     csp.add_constraint(constraint)
        
                
        constraint.add_satisfying_tuples(goodPerms)
        csp.add_constraint(constraint)
    

    return csp, variables

tester, var_tester = cagey_csp_model((3,[(10, [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)], '*')]))
# for c in tester.get_all_cons():
#     print("here", len(c.scope))
#     print("rahhh", c.scope)
# guess = [c for c in tester.get_all_cons() if len(c.scope) == 7]
# print("guess", guess)
# print("here2", guess[0].scope[0].dom)
# # print(guess[0])
# for g in guess:
#     print("guess", g)
#     print("guess", g.sat_tuples)

