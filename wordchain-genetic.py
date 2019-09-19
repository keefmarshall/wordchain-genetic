# adapting a genetic algorithm from https://devmates.co/solutions/minumum_genetic_mutation
# to solve the wordchains problem

import itertools
import multiprocessing as mp
from solution import Solution

def loadFile(filename):
    f = open(filename, 'r')
    x = f.read().splitlines()
    f.close()
    return x

def groupBySize(list_to_group):
    sorted_by_size = sorted(list_to_group, key=len)
    grouped_result = {}
    for key, group in itertools.groupby(sorted_by_size, key=lambda x:len(x)):
        grouped_result[key] = list(group)
    return grouped_result

def getChainForPair(pair):
    (start, end) = pair.split(" ")
    (count, chain) = sol.minMutation(start, end, dict_by_size[len(start)])
    chain.append(end)
    return (count + 1, ",".join(chain))
    # print(count + 1, ",".join(chain))


dictionary = loadFile("50kwords.txt")
dict_by_size = groupBySize(dictionary)
sol = Solution()

pairs = loadFile("wordpairs.txt")

pool = mp.Pool(mp.cpu_count())
chains = pool.map(getChainForPair, [pair for pair in pairs])
pool.close()

[print(count, chain) for (count, chain) in chains]
# for pair in pairs:
#     print(getChainForPair(pair))
