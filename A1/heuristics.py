# =============================
# Student Names: Calvin Birch, Mike Stephen, Cooper Moses 
# Group ID: 11
# Date: 2025-01-30
# =============================
# CISC 352 - W23
# heuristics.py
# desc:
#


#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete problem solution.

'''This file will contain different constraint propagators to be used within
   the propagators

1. ord_dh (worth 0.25/3 points)
    - a Variable ordering heuristic that chooses the next Variable to be assigned 
      according to the Degree heuristic

2. ord_mv (worth 0.25/3 points)
    - a Variable ordering heuristic that chooses the next Variable to be assigned 
      according to the Minimum-Remaining-Value heuristic


var_ordering == a function with the following template
    var_ordering(csp)
        ==> returns Variable

    csp is a CSP object---the heuristic can use this to get access to the
    Variables and constraints of the problem. The assigned Variables can be
    accessed via methods, the values assigned can also be accessed.

    var_ordering returns the next Variable to be assigned, as per the definition
    of the heuristic it implements.
   '''

def ord_dh(csp):
    ''' return next Variable to be assigned according to the Degree Heuristic '''
    all_unassigned = csp.get_all_unasgn_vars()
    max_count=0
    next_up = all_unassigned[0]

    for i in all_unassigned:
        count=0
        var_constraints = csp.get_cons_with_var(i) # List of all constraints with variable
        for n in var_constraints:
            if len(n.get_scope())>1: # Makes sure constraint has multiple variables on it
                count+=1
        if count>max_count:
            max_count=count # Saves highest degree
            next_up=i
    return next_up




def ord_mrv(csp):
    ''' return Variable to be assigned according to the Minimum Remaining Values heuristic '''
    all_unassigned = csp.get_all_unasgn_vars()
    minimum = all_unassigned[0]

    for i in all_unassigned[1:]: 
        if len(i.cur_domain()) < len(minimum.cur_domain()): # Saves variable with most constrained domain
            minimum = i
    return minimum

