"""
程序：遗传算法解决0-1背包问题
说明：
1.采用经典的二进制编码，选择算子为轮盘赌选择，交叉算子为两点交叉，变异算子为单点变异
2.可调的参数为：
gen：最大生成代数；  pc：交叉概率；  pm：变异概率；
popsize：种群大小； n：染色体长度，即物品数量；
 w：物品重量； c：物品价值； W：背包承重.
"""

import numpy as np
from time import time


# 初始化种群
def generate_population(popsize, n):
    population = []
    for i in range(popsize):
        pop = ''
        for j in range(n):
            pop = pop+str(np.random.randint(0, 2))
        population.append(pop)    
    return population


# 判断是否符合约束
def decode(x, n, w, c, W):
    s = []  # 储存被选择物体的下标集合
    weight = 0
    v = 0
    for i in range(n):
        if (x[i] == '1'):
            if weight + w[i] <= W:
                weight = weight + w[i]
                v = v + c[i]
                s.append(i)
            else:
                break
    return v, s

def getfitness(population, n, w, c, W):
    value = []
    ss = []
    for i in range(len(population)):
        [v, s] = decode(population[i], n, w, c, W)
        value.append(v)
        ss.append(s)
    return value, ss


# 选择——轮盘赌方法
def select(population, value, popsize):
    fitness_sum = []
    value_sum = sum(value)
    fitness = [i/value_sum for i in value]
    for i in range(len(population)):
        if i == 0:
            fitness_sum.append(fitness[i])
        else:
            fitness_sum.append(fitness_sum[i-1]+fitness[i])
    population_new = []
    for j in range(popsize):
        r = np.random.uniform(0, 1)
        for i in range(len(fitness_sum)):
            if i == 0:
                if r >= 0 and r <= fitness_sum[i]:
                    population_new.append(population[i])
            else:
                if r >= fitness_sum[i-1] and r <= fitness_sum[i]:
                    population_new.append(population[i])
    return population_new


# 两点交叉
def crossover(population_new, pc, ncross):
    a = int(len(population_new)/2)
    parents_one = population_new[:a]
    parents_two = population_new[a:]
    np.random.shuffle(parents_one)
    np.random.shuffle(parents_two)
    offspring = []
    for i in range(a):
        r = np.random.uniform(0, 1)
        if r <= pc:
            point1 = np.random.randint(0, (len(parents_one[i])-1))
            point2 = np.random.randint(point1, len(parents_one[i]))
            off_one = parents_one[i][:point1]+parents_two[i][point1:point2]+parents_one[i][point2:]
            off_two = parents_two[i][:point1]+parents_one[i][point1:point2]+parents_two[i][point2:]
            ncross = ncross+1
        else:
            off_one = parents_one[i]
            off_two = parents_two[i]
        offspring.append(off_one)
        offspring.append(off_two)
    return offspring


# 单点变异
def mutation(offspring, pm, nmut):
    for i in range(len(offspring)):
        for j in range(len(offspring[i])):
            r = np.random.uniform(0, 1)
            if r <= pm:
                if j == 0:
                    if offspring[i][j] == '1':
                        offspring[i] = '0'+offspring[i][1:]
                    else:
                        offspring[i] = '1'+offspring[i][1:]
                else:
                    if offspring[i][j] == '1':
                        offspring[i] = offspring[i][:(j-1)]+'0'+offspring[i][j:]
                    else:
                        offspring[i] = offspring[i][:(j-1)]+'1'+offspring[i][j:]
                nmut = nmut+1
    return offspring





