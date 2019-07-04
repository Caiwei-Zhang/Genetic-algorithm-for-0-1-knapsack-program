# Genetic-algorithm-for-0-1-knapsack-program

Using simple genetic algorithm to approximatively solve 0-1 knapsack program




ga_knapsack.py: define the genetic algorithm.

simulate.py: define a function to do numeric simulation. Parameters are shown as following:

     def simulate(n, popsize, gen, pc, pm, c, w, W):  

         """     

         :param n:  length of chromosome(the number of items)

         :param popsize: size of population(the number of chromosomes in population)

         :param gen: the times of iterations

         :param pc: the probability of crossover

         :param pm: the probability of mutation      

         :param c: the value of each item

         :param w: the quality of each item

         :param W: max quality that the knapsack could hold

         :return: optimal solution，opyimal items group，the kth iteration when optimal solution appear，runtime.

         """ 
     
Run simulate.py to get the simulation result. You can also change the quantity of parameters.
