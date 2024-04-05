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
        # Perform a deep copy of the input list of list 
        return [row[:] for row in ll]

    def get_cells(self):
        # The get_cells method calls the ._cells method and return the result
        return self._cells
    
    def shape(self):
        # Give shape of the matrix
        mat = self._cells
        return (len(mat), len(mat[0]))
    
    def nonzero(self):
        # Return a list of triplets (row index, column index, value) of non-zero cells,
        # in no particular order.
        nonzero_triplets = []
        mat = self._cells 
        for i, row  in enumerate(mat):
            row_ind = i + 1
            for k,col in enumerate(row):  
               col_ind = k + 1
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
        output = []
        # list of string
        for i, row in enumerate(mat):
            if i == 0:
                # first row visualization
                if len(mat) == 1:
                    output.append('DenseMatrix [ ' + f'{row} ]')
                else:
                    output.append('DenseMatrix [ ' + f'{row}')
            elif i == (len(mat)-1):
                # middle rows visual.
                output.append('              ' + f'{row} ]')
            else:
                # end row visual.
                output.append('              ' + f'{row}')
        # joining strings in final visual.
        return '\n'.join(output)
    
    def __repr__(self):
        # RETURN one-line string representing a Python expression which would recreate the matrix
        mat = self._cells
        print(mat)

    def __getitem__(self, key):
        # Overrides default bracket access behaviour.
        # Key is whatever the user passes within the brackets
        if isinstance (key, tuple):
            n_row, n_col = key
            mat = self.get_cells()
            # checking row index
            if n_row < 0:
                # handling negative index case
                if n_row < -len(mat):
                    raise IndexError('Row index out of range')
                else:
                    n_row += len(mat)
            else:
                len_mat = n_row + 1
                if len_mat >= len(mat):
                    raise IndexError('Row index out of range')
            # checking col index
            if n_col < 0:
                # handling neg. index case
                if n_col < -len(mat[0]):
                    raise IndexError('Column index out of range')
                else:
                    n_col += len(mat[0])
            else:
                len_col = n_col + 1
                if len_col >= len(mat[0]):
                    raise IndexError('Column index out of range')

            for i, row in enumerate(mat):
                for k in range(len(row)):
                    if i == n_row and k == n_col:
                        print(mat[i][k])
                        return mat[i][k]
        else: 
            raise TypeError('Provided key must be a list')
    
    def __eq__(self, other):
        # Overrides an equality operator
        mat1 = self._cells
        if type(other) == DenseMatrix:
            mat2 = other._cells
            if self.shape() == other.shape():
                equal = True
                for i, row in enumerate(mat1):
                    for k in range(len(row)): 
                        if mat1[i][k] != mat2[i][k]:
                            # checking equality
                            equal = False
                            break
                    if equal == False:
                        break 
                if equal == True:
                    print(True)
                else:
                    print(False)
            else:
                print(False)
        else:
            print(False)
    
    def __add__(self, other):
        # overrides sum operator
        mat1 = self._cells
        if type(other) is DenseMatrix:
            if self.shape() == other.shape():
                mat2 = other._cells
                sum_mat = []
                for i, row in enumerate(mat1):
                    sum_mat.append([])
                    for k in range(len(row)): 
                        sum_mat[i].append(mat1[i][k] + mat2[i][k])
                return DenseMatrix(sum_mat)
            
        elif isinstance(other, list):
            n,m = self.shape()
            if n == len(other) or m == len(other[0]):
                sum_mat = []
                for i, row in enumerate(mat1):
                    sum_mat.append([])
                    for k in range(len(row)): 
                        sum_mat[i].append(mat1[i][k] + other[i][k])
                return DenseMatrix(sum_mat)
        else:
            raise ValueError('Not a DenseMatrix or any other matrix')

    def __mul__(self, other):
        # Overrides mul operator
        mat1 = self._cells
        if type(other) is DenseMatrix:
            _, m1 = self.shape()
            n2, m2 = other.shape()
            if m1 == n2:
                mat2 = other._cells
                mol_mat = []
                for row in mat1:
                    mol_mat_row = []
                    for j in range(m2):
                        cell_sum = 0
                        for k in range(len(row)):
                            cell_sum += row[k]*mat2[k][j] 
                        mol_mat_row.append(cell_sum)
                    mol_mat.append(mol_mat_row)
                return DenseMatrix(mol_mat)
            else:
                raise ValueError('First matrix\'s column not equal to second matrix\'s row')
            
        elif isinstance(other, list):
            _, m1 = self.shape()
            n2, m2 = len(other), len(other[0])
            if m1 == n2:
                mol_mat = []
                for row in mat1:
                    mol_mat_row = []
                    for j in range(m2):
                        cell_sum = 0
                        for k in range(len(row)):
                            cell_sum += row[k]*other[k][j] 
                        mol_mat_row.append(cell_sum)
                    mol_mat.append(mol_mat_row)
                return DenseMatrix(mol_mat)
            else:
                raise ValueError('First matrix\'s column not equal to second matrix\'s row')
        
        elif isinstance(other, int) or isinstance(other, float):
            _, m1 = self.shape()
            mol_mat = []
            for row in mat1:
                mol_mat_row = []
                for cell in row:
                    mol_mat_row.append(cell*other)
                mol_mat.append(mol_mat_row)
            return DenseMatrix(mol_mat)
        else:
            raise ValueError('Not a DenseMatrix or any other matrix or any scalar')


# Main
def main():

    dma = DenseMatrix([ [0,6,8,0],
                        [0,0,0,5],
                        [9,0,7,0] ])
    
    dmc = [ [1,2,3],
                        [6,7,8],
                        [10,11,12],
                        [9,0,7] ]
    
    print(dma * dmc)

if __name__ == '__main__':
    main()