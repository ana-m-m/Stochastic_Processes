"""
KNAPSACK PROBLEM: 0/1
    una mochila que puede llevar un peso maximo y unas calorias máximas,
    tienes comida donde elegir para meter en la mmochila.
    método 0/1-> o coges elemento (1) o no coges (0)
    """
# item = (value, weight)
# w == total_bag_weight
# I == set of items, len n
# V == set of taken items, len n ex,(0, 1, 0...)
"""
    maximizar: sumatorio V[i]*I[i] value
    constricción: sumatorio  V[i]*I[i] weigth <= w
"""
# NOT EFFICIENT SOLUTION:
# 1. Enumerate all possible combinations of items -> power set
# 2. Remove combinations that exceed w
# 3. Choose the set with largest value

# this problem is exponential due to items

# GREEDY ALGORITHM: while knapsack not full, put best available item
class Food(object):

    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return self.name + ": <" + str(self.value) + ", " + str(self.calories) +">"

def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu

def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    # keyFunction => define what is the meaning of best (criteria of order)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= float(maxCost):
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return result, totalValue

def testgreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print("Total value of items taken =", val)
    for item in taken:
        print("   ", item)
def testgreedys(foods, maxUnits):
    print("use greedy by value to allocate", maxUnits, "calories")
    testgreedy(foods, maxUnits, Food.getValue)
    print("\n use greedy by cost to allocate", maxUnits, "calories")
    testgreedy(foods, maxUnits, lambda x: 1/Food.getCost(x)) # get less calories
    print("\n use greedy by density to allocate", maxUnits, "calories")
    testgreedy(foods, maxUnits, Food.density)
names = ["wine", "beer", "pizza", "burger", "fries", "cola", "apple", "donut", "cake"]
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testgreedys(foods, 750)

"""problemof greedy : of local maxima instead of golbal maxima"""