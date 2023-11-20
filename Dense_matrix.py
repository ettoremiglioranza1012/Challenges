class DenseMatrix():
    
    def __init__(self, *args):
        # self is now a DenseMatrix instance, meanwhile 
        # *args is a tuple with len == number of args.
        
        if len(args) == 1: # List of list
            # in this case we got args as a tuple of len == 1, and in 
            # position args[0] we find the input list of list. 
            # We put the input(list of list) into row variable. 
            ll = args[0]
            # checking for wrong data
            if not ll:
                raise ValueError('The list is empty')
            for sublist in ll: 
                if not sublist:
                    raise ValueError('Data missing in sublist')
            # the deep_copied_lits becames callable by the ._cells method
            self._cells = self.mat_deepcopy(ll)
        elif len(args) == 3: # Triplets
            n_row, n_col, triplets = args
            # setting a condition for the input value
            if n_row < 1 or n_col < 1:
                raise ValueError('Provided data must allow the creation of a matrix with at least one row and one column')
            # creating a matrix with 0 in every cell
            self._cells = [[0]*n_col for _ in range(n_row)]
            # then fill each position present in the triplets,
            # with the corresponding value
            for row_index, col_index, value in triplets:
                self._cells[row_index][col_index] = value 
            # in the end we got a matrix with 0 values in the blind spot,
            # and with the value in the triplets
        else:
            raise ValueError('Invalid argouments provided to build the matrix')

    def mat_deepcopy(self, ll):
        # Perform a deep copy of the input list of list 
        return [row[:] for row in ll]

    def get_cells(self):
        # the get_cells method calls the ._cells method and return the result
        return self._cells
    
    def shape(self):
        mat = self._cells
        return len(mat), len(mat[0])
    
    def __str__(self):
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
        mat = self._cells
        print(mat)

    def __getitem__(self, key):
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


def main():
    # we got Notes to explain what's going on
    
    # List of list:
    ## input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ## input = [[1]]
    ## input = []
    ## input = [[]]
    ## dense_matrix = DenseMatrix(input)

    # So after this we got our dense matrix,
    # which is a DenseMatrix instance called ._cells,
    # in which is stored a deep copy of the original input matrix.
    # Lastly, the constructor end up in the output dense_matrix

    ## cells = dense_matrix.get_cells()

    # The method .get_cells return the object related to the 
    # DenseMatrix Instance self._cells, which is the deep copy of the 
    # original input matrix

    ## dense_matrix.__str__()
    ## dense_matrix.__repr__()

    # Triplets:
    n = 3
    m = 4
    triplets = [(0,1,6),(0,2,8),(1,3,5),(2,0,9),(2,2,7)]
    dense_matrix = DenseMatrix(n,m,triplets)
    
    dense_matrix.__str__()
    print('')
    dense_matrix.__repr__()
    print('')
    print(dense_matrix.shape())
    print('')
    print(dense_matrix.__getitem__([2,-1]))
    print('')

if __name__ == '__main__':
    main()