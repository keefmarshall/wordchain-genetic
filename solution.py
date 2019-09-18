# adapted a genetic algorithm from https://devmates.co/solutions/minumum_genetic_mutation
# to handle english words instead of gene sequences


class Solution:
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if len(start) < 1 or len(end) < 1 or len(bank) < 1 or not end in bank:
            return -1
        
        queue = []
        queue.append((start,0,[]))
        bankSet = set(bank)
        chain = {}
        while queue:
            current_mutation, current_level, from_list = queue.pop(0)
            if current_mutation == end:
                return (current_level, from_list)
            
            new_from = from_list.copy()
            new_from.append(current_mutation)

            for index in range(len(current_mutation)):
                for char in 'abcdefghijklmnopqrstuvwxyz': # was 'ACGT'
                    mutation = current_mutation[:index] + char + current_mutation[index+1:]
                    if mutation in bankSet:
                        bankSet.remove(mutation)
                        queue.append((mutation,current_level+1,new_from))
        
        return -1
        