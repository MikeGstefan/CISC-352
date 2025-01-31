# =============================
# Student Names:
# Group ID:
# Date:
# =============================
# CISC 352 - W23
# propagators.py
# desc:
#


#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete problem solution.

'''This file will contain different constraint propagators to be used within
   bt_search.

    1. prop_FC (worth 0.5/3 marks)
        - a propagator function that propagates according to the FC algorithm that 
          check constraints that have exactly one Variable in their scope that has 
          not assigned with a value, and prune appropriately

    2. prop_GAC (worth 0.5/3 marks)
        - a propagator function that propagates according to the GAC algorithm, as 
          covered in lecture

   propagator == a function with the following template
      propagator(csp, newly_instantiated_variable=None)
           ==> returns (True/False, [(Variable, Value), (Variable, Value) ...]

      csp is a CSP object---the propagator can use this to get access
      to the variables and constraints of the problem. The assigned Variables
      can be accessed via methods, the values assigned can also be accessed.

      newly_instaniated_variable is an optional argument.
      if newly_instantiated_variable is not None:
          then newly_instantiated_variable is the most
           recently assigned Variable of the search.
      else:
          progator is called before any assignments are made
          in which case it must decide what processing to do
           prior to any Variables being assigned. SEE BELOW

       The propagator returns True/False and a list of (Variable, Value) pairs.
       Return is False if a deadend has been detected by the propagator.
       in this case bt_search will backtrack
       return is true if we can continue.

      The list of Variable values pairs are all of the values
      the propagator pruned (using the Variable's prune_value method).
      bt_search NEEDS to know this in order to correctly restore these
      values when it undoes a Variable assignment.

      NOTE propagator SHOULD NOT prune a value that has already been
      pruned! Nor should it prune a value twice

      PROPAGATOR called with newly_instantiated_variable = None
      PROCESSING REQUIRED:
        for plain backtracking (where we only check fully instantiated
        constraints)
        we do nothing...return true, []

        for forward checking (where we only check constraints with one
        remaining Variable)
        we look for unary constraints of the csp (constraints whose scope
        contains only one Variable) and we forward_check these constraints.

        for gac we establish initial GAC by initializing the GAC queue
        with all constaints of the csp


      PROPAGATOR called with newly_instantiated_variable = a Variable V
      PROCESSING REQUIRED:
         for plain backtracking we check all constraints with V (see csp method
         get_cons_with_var) that are fully assigned.

         for forward checking we forward check all constraints with V
         that have one unassigned Variable left

         for gac we initialize the GAC queue with all constraints containing V.
   '''

def prop_BT(csp, newVar=None):
    '''Do plain backtracking propagation. That is, do no
    propagation at all. Just check fully instantiated constraints'''

    if not newVar:
        return True, []
    for c in csp.get_cons_with_var(newVar):
        if c.get_n_unasgn() == 0:
            vals = []
            vars = c.get_scope()
            for var in vars:
                vals.append(var.get_assigned_value())
            if not c.check_tuple(vals):
                return False, []
    # print("setting", newVar, "pruning", newVar.get_assigned_value(), "from")
    return True, []

def prop_FC(csp, newVar=None):
    '''Do forward checking. That is check constraints with
       only one uninstantiated Variable. Remember to keep
       track of all pruned Variable,value pairs and return '''
    #IMPLEMENT
    # csp.print_all()
    # for c in csp.get_all_cons():
    #     for v in c.get_scope():
    #         print(v.cur_domain())
    vals = []
    if not newVar:
        for c in csp.get_all_nary_cons(1):
            v = c.get_unasgn_vars()[0]
            if v.cur_domain_size() == 0:
                return False, vals
            if v.cur_domain_size() == 1:
                if not c.check_var_val(v, v.cur_domain()[0]):
                    return False, vals
                
    else:
        for c in csp.get_cons_with_var(newVar):
            if c.get_n_unasgn() == 1:
                v = c.get_unasgn_vars()[0]
                if v.cur_domain_size() == 0:
                    return False, vals
                if v.cur_domain_size() == 1:
                    if not c.check_var_val(v, v.cur_domain()[0]):
                        return False, vals
                for val in v.cur_domain():
                    if not c.check_var_val(v, val):
                        # print("setting", newVar, "pruning", val, "from", v)
                        v.prune_value(val)
                        vals.append((v, val))
                # print("setting", newVar, "looking", v, "cur", v.cur_domain())
                # if not c.check_tuple(v.cur_domain()):
                #     print("setting", newVar, "pruning", newVar.get_assigned_value(), "from", v)
                #     v.prune_value(newVar.get_assigned_value())
                #     vals.append((v, newVar.get_assigned_value()))  
                    # continue
                # v = c.get_unasgn_vars()[0]
                # if v.cur_domain_size() == 0:
                #     return False, []
                
                # if not c.check_var_val(newVar, newVar.get_assigned_value()):
                #     # continue
                # if v.in_cur_domain(newVar.get_assigned_value()):
                #     if v.cur_domain_size() == 1:
                #         return False, []
                #     print("setting", newVar, "pruning", newVar.get_assigned_value(), "from", v)
                #     v.prune_value(newVar.get_assigned_value())
                #     vals.append((v, newVar.get_assigned_value()))  

                   
    return True, vals


def prop_GAC(csp, newVar=None):
    '''Do GAC propagation. If newVar is None we do initial GAC enforce
       processing all constraints. Otherwise we do GAC enforce with
       constraints containing newVar on GAC Queue'''
    #IMPLEMENT

    # print(csp.get_all_cons()[0].get_scope())
    vals = []
    # csp.print_all()
    if not newVar:
        # print("here")
        queue = csp.get_all_cons()
        resolved =[]
        for c in queue:
            # print(c)
            # print("bing", c.get_unasgn_vars())
            for v in c.get_scope():
                # print(v.cur_domain())
                for val in v.cur_domain():
                    if not c.check_var_val(v, val):
                        # print("setting", v, "pruning", val, "from", c)
                        v.prune_value(val)
                        vals.append((v, val))
                        # resolved.append(c)
                        # break
                    # print("checking", v, val, c.check_var_val(v, val))
        # for c in csp.get_all_cons():
        #     print(c.get_unasgn_vars())
    else: 
        for c in csp.get_cons_with_var(newVar):
            for v in c.get_scope():
                # print(v.cur_domain())
                for val in v.cur_domain():
                    if not c.check_var_val(v, val):
                        # print("setting", v, "pruning", val, "from", c)
                        v.prune_value(val)
                        vals.append((v, val))
                        # resolved.append(c)
                        # break
                    # print("checking", v, val, c.check_var_val(v, val))

    return True, vals