class Mutation:
    
    @classmethod
    def horizontal(cls, data):    
        found = False
        j = 0
        while j < len(data):
            end = 4
            while end <= len(data[j]):                    
                init = end - 4        
                if len(set(data[j][init : end])) == 1:
                    found = True
                    break
                end+=1    
            j += 1
        return found

    @classmethod
    def vertical(cls, data):
        found = False    
        j = 0    
        while j < len(data[0]):
            init = 4
            while init <= len(data):
                if len(set([data[init - 4][j], data[init - 3][j], data[init - 2][j], data[init - 1][j]])) == 1:
                    found = True
                    break               
                init += 1
            j+=1
        return found
