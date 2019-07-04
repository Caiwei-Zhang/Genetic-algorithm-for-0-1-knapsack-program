import numpy as np
import time
import matplotlib.pyplot as plt
from ga_knapsack import *


def simulate(n, popsize, gen, pc, pm, c, w, W):
    """
    :param n:  染色体长度，即物品数量
    :param popsize: 种群大小，即种群中的染色体数量
    :param gen: 最大代数，迭代次数
    :param pc: 交叉概率
    :param pm: 变异概率
    :param c: 输入数据——物品价值
    :param w: 输入数据——物品重量
    :param W: 背包承重
    :return: 最优解，最优组合，最优解出现代数，运行时间
    """
    # 初始化-------------------------------------------------------------------------
    # 初始化种群（编码）
    np.random.seed(10)
    population = generate_population(popsize, n)

    # 适应度评价（解码）
    value, s = getfitness(population, n, w, c, W)

    # 初始化交叉个数
    ncross = 0

    # 初始化变异个数
    nmut = 0

    # 储存每代种群的最优值及其对应的个体
    t = []
    best_ind = []
    last = []  # 储存最后一代个体的适应度值
    realvalue = []  # 储存最后一代解码后的值
    totaltime = 0
    t1 = time()

    # 循环---------------------------------------------------------------------------
    for i in range(gen):
        print("迭代次数：")
        print(i)
        # 交叉
        offspring_c = crossover(population, pc, ncross)

        # 变异
        # offspring_m = mutation1(offspring, pm, nmut)
        offspring_m = mutation(offspring_c, pm, nmut)
        mixpopulation = population + offspring_m
        # 适应度函数计算
        value, s = getfitness(mixpopulation, n, w, c, W)

        # 轮盘赌选择
        population = select(mixpopulation, value, popsize)
        # 储存当代的最优解
        result = []
        if i == gen - 1:
            value1, s1 = getfitness(population, n, w, c, W)
            realvalue = s1
            result = value1
            last = value1

        else:
            value1, s1 = getfitness(population, n, w, c, W)
            result = value1

        maxre = max(result)
        h = result.index(max(result))
        # 将每代的最优解加入结果种群
        t.append(maxre)
        best_ind.append(population[h])
        t2 = time()
        totaltime = t2 - t1

# 输出结果-------------------------------------------------------------------------------------
    best_value = max(t)
    hh = t.index(max(t))
    f2, s2 = decode(best_ind[hh], n, w, c, W)

    print("最优组合为：")
    print(s2)
    print("最优解为：")
    print(best_value)
    print("最优解出现的代数：")
    print(hh)
    print("运行时间：")
    print(totaltime)
    # 画出收敛曲线
    plt.plot(t)
    plt.title('The curve of the optimal function value of each generation with the number of iterations',
              color='#123456')
    plt.xlabel('the number of iterations')
    plt.ylabel('the optimal function value of each generation')
    plt.savefig("n100.jpg")
    plt.show()


# simulate(n, popsize, gen, pc, pm, c, w, W, ncross, nmut)
gen = 1500  #  最大生成代数
pc = 0.25  # 交叉概率  建议在0.5~0.95之间
pm = 0.02  # 变异概率  建议在0.01~0.05之间
popsize = 50  # 种群大小 取10,20,50,100

n = 100# 物品数, 即染色体长度n 取20,50,100

np.random.seed(10)
w = np.random.randint(0, 20, n)
c = np.random.randint(0, 40, n)
print('物品重量为：')
print(w)
print('物品价值为：')
print(c)

W = 40

simulate(n, popsize, gen, pc, pm, c, w, W)
