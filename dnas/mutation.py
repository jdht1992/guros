class Mutation:
    
    @classmethod
    def validate_genetic_difference(cls, data):
        found = False    
        row = 0
        while row < len(data[0]):
            column = 0
            while column < len(data):             

                if len(data[0]) - column > 3:
                    if len(set([data[row][column], data[row][column + 1], data[row][column + 2], data[row][column + 3]])) == 1:
                        return True
                    if row < len(data[0]) - 3:
                        if len(set([data[row][column], data[row + 1][column + 1], data[row + 2][column + 2], data[row + 3][column + 3]])) == 1 or \
                        len(set([data[row][column], data[row + 1][column], data[row + 2][column], data[row +3][column]])) == 1:
                            return True

                if column >= 3:
                    if len(set([data[row][column], data[row - 1][column], data[row - 2][column], data[row - 3][column]])) == 1:
                        return True

                    if row < len(data[0]) - 3:
                        if len(set([data[row][column], data[row + 1][column - 1], data[row + 2][column - 2], data[row + 3][column - 3]])) == 1:                   
                            return True
                
                column += 1
            row+=1
        return found
