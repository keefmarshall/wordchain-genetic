# adapting a genetic algorithm from https://devmates.co/solutions/minumum_genetic_mutation
# to solve the wordchains problem

from solution import Solution

def loadFile(filename):
    f = open(filename, 'r')
    x = f.read().splitlines()
    f.close()
    return x


dictionary = loadFile("50kwords.txt")
inputs = loadFile("wordpairs.txt")
sol = Solution()
for input in inputs:
    (start, end) = input.split(" ")
    (count, chain) = sol.minMutation(start, end, dictionary)
    chain.append(end)
    print(count + 1, ",".join(chain))
