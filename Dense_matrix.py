# CLASS DenseMatrix
class DenseMatrix():
    
    '''__Constructor__'''
    
    def __init__(self, *args):
        # 'self' refers to the instance of the class being created, meanwhile 
        # *args is a tuple with len == number of args.
        
        if len(args) == 1: # List of list
            # In this case we got args as a tuple of len == 1, and in 
            # position args[0] we find the input list of list. 
            # We put the input(list of list) into row variable. 
            ll = args[0]
            # Checking for wrong data
            if not ll:
                raise ValueError('The list is empty')
            for sublist in ll: 
                if not sublist:
                    raise ValueError('Data missing in sublist')
            # The deep_copied_lits becames the ._cells atribute 
            self._cells = self.mat_deepcopy(ll)
        elif len(args) == 3: # Triplets
            n_row, n_col, triplets = args
            # Setting a condition for the input value
            if n_row < 1 or n_col < 1:
                raise ValueError('Provided data must allow the creation of a matrix with at least one row and one column')
            # Creating a matrix with 0 in every cell
            self._cells = [[0]*n_col for _ in range(n_row)]
            # then fill each position present in the triplets,
            # with the corresponding value
            for row_index, col_index, value in triplets:
                self._cells[row_index][col_index] = value 
            # In the end we got a matrix with 0 values in the blind spot,
            # and with the value in the triplets
        else:
            raise ValueError('Invalid argouments provided to build the matrix')
    
    '''Methods'''
    
    def mat_deepcopy(self, ll):
        # Perform a deep copy of the input list of list hjlkl
        return [row[:] for row in ll]

    def get_cells(self):
        # The get_cells method calls the ._cells method and return the result
        return self._cells
    
    def shape(self):
        # Give shape of the matrix
        mat = self._cells
        return len(mat), len(mat[0])
    
    def nonzero(self):
        # Return a list of triplets (row index, column index, value) of non-zero cells,
        # in no particular order.
        nonzero_triplets = []
        mat = self._cells 
        for i, row  in enumerate(mat):
            row_ind = i + 1
            for k,col in enumerate(row):  
               col_ind = k+1
               if col != 0:
                   trip = (row_ind,col_ind,col)
                   nonzero_triplets.append(trip)  
        return nonzero_triplets

    @staticmethod
    def isclose_son(m1, m2, delta):
        # Staticmethod to return Bool value, cause I don't need 'self'
        for i, row in enumerate(m1):
            for k in range(len(row)): 
                if abs(m1[i][k] - m2[i][k]) > delta:
                    return False
        return True
    
    def isclose(self, other, delta):
        # RETURN True if each cell in this matrix is within a delta distance
        # from other Matrix. RETURN False if any cell couple differs more than delta
        if self.shape() == other.shape():
            mat_dma = self._cells
            mat_dmd = other._cells
            print(self.isclose_son(mat_dma, mat_dmd, delta))
        else:
            raise ValueError('Matrices have different dimension!')
    
    '''__SpecialMethods__'''
    
    def __str__(self):
        # RETURN a nice human-readable formatted string
        mat = self._cells
        for i, row in enumerate(mat):
            if i == 0:
                if len(mat) == 1:
                    print('DenseMatrix [ ' + f'{row} ]')
                else:
                    print('DenseMatrix [ ' + f'{row}')
            elif i == (len(mat)-1):
                print('              ' + f'{row} ]')
            else:
                print('              ' + f'{row}')
    
    def __repr__(self):
        # RETURN one-line string representing a Python expression which would recreate the matrix
        mat = self._cells
        print(mat)

    def __getitem__(self, key):
        # Overrides default bracket access behaviour.
        # Key is whatever the user passes within the brackets
        if isinstance (key, list):
            n_row, n_col = key
            mat = self.get_cells()
            if n_row == 0 or n_col == 0:
                    raise ValueError('Provided data must must match with a matrix with at least one row and one column')
            
            if n_row < 0:
                if n_row < -len(mat):
                    raise IndexError('Row index out of range')
                else:
                    n_row += len(mat)
            else:
                n_row -= 1
                if n_row >= len(mat):
                    raise IndexError('Row index out of range')
            
            if n_col < 0:
                if n_col < -len(mat[0]):
                    raise IndexError('Column index out of range')
                else:
                    n_col += len(mat[0])
            else:
                n_col -= 1
                if n_col >= len(mat[0]):
                    raise IndexError('Column index out of range')
            
            for i, row in enumerate(mat):
                for k in range(len(row)): 
                    if i == n_row and k == n_col:
                        return mat[i][k]
        else: 
            raise TypeError('Provided key must be a list')
# Main
def main():

    # dma:
    n = 3
    m = 4
    triplets = [(0,1,6),(0,2,8),(1,3,5),(2,0,9),(2,2,7)]
    dma = DenseMatrix(n,m,triplets)

    # dmd:
    input = [[0,5.9,8,0],[0,0,0.1,5],[9.15,-0.1,7,0.1]]
    ## input = [[0,5.9,8],[0,0, 0.1],[9.15,-0.1,7]]
    dmd = DenseMatrix(input)
    # delta:
    delta = 0.2
    
    # Tests:
    dma.isclose(dmd, delta)

if __name__ == '__main__':
    main()
