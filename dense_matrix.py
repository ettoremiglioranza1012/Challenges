import unittest
# CLASS DenseMatrix
class DenseMatrix():
    
    '''__Constructor__'''
    
    def __init__(self, *args):

        if len(args) == 1: # List of list
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
            # Filling matrix
            for row_index, col_index, value in triplets:
                self._cells[row_index+1][col_index+1] = value 
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
        output = []
        # RETURN one-line string representing a Python expression which would recreate the matrix
        mat = self._cells
        for i, row in enumerate(mat):
            if i == 0: 
                if len(mat) == 1:
                    output.append('[ ' + f'{row} ]')
                else:
                    output.append('[ ' + f'{row}')
            elif i == (len(mat) - 1):
                output.append(f'{row} ]')
            else:
                output.append(f'{row}')
        return ', '.join(output)

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
                if n_row >= len(mat):
                    raise IndexError('Row index out of range')
            # checking col index
            if n_col < 0:
                # handling neg. index case
                if n_col < -len(mat[0]):
                    raise IndexError('Column index out of range')
                else:
                    n_col += len(mat[0])
            else:
                if n_col >= len(mat[0]):
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

# Class Test_matrix
Mat = DenseMatrix
#Mat = SparseMatrix
class MatrixTest(unittest.TestCase):

    def test_empty(self):
        with self.assertRaises(ValueError):
            Mat([])
    
    def test_init_list(self):
        lst = [[1,2,3],
               [4,5,6]]
        mat = Mat(lst)
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                self.assertEqual(mat[i,j], lst[i][j])

        self.assertEqual(lst, [[1,2,3],
                               [4,5,6]])

        with self.assertRaises(ValueError):
            Mat([[]])   

    def test_init_triplets(self):        
        mat = Mat(10,20, [(8,12,4), (7,9,6)])

        for i in range(10):
            for j in range(20):
                if (i,j) != (8,12) and (i,j) != (7,9):
                    self.assertEqual(mat[i,j], 0)
        self.assertEqual(mat[8,12], 4)
        self.assertEqual(mat[7,9], 6)
        
        with self.assertRaises(ValueError):
            Mat(0,0,[])
        with self.assertRaises(ValueError):
            Mat(-4,2,[(2,4,7)])
        with self.assertRaises(ValueError):
            Mat(3,-4,[(2,4,7)])
        with self.assertRaises(ValueError):
            Mat(5,10,[(7,1,50)])   
        
        with self.assertRaises(ValueError):
            Mat(5,10,[(5,1,60)])   
        
        with self.assertRaises(ValueError):
            Mat(6,15,[(4,16,70)])
        
        with self.assertRaises(ValueError):
            Mat(6,15,[(4,15,70)])

        with self.assertRaises(ValueError):
            Mat(6,15,[(7,19,80)])

        with self.assertRaises(ValueError):
            Mat(6,15,[(4,3,80), (4,20,10)])

        with self.assertRaises(ValueError):
            Mat(6,15,[(4,3,80), (20,1,10)])

    def test_str(self):
        # notice different implemenetations will have different str
        mat = Mat([[2,5,3],
                   [6,2,7],
                   [4,2,5]])
        s = str(mat)        
        self.assertTrue(type(mat).__name__ in s)
    
    def test_repr(self):
        # notice different implemenetations will have different str
        triplets = [(1,2,3), (2,0,9)]
        mat = Mat(triplets)
        self.assertTrue(str(type(mat).__name__) in repr(mat))

    def test_shape_12(self):        
        mat = Mat([[6,5,3], 
                   [2,8,3]]) 
        self.assertEqual(mat.shape(), (2,3))

    def test_shape_3019(self):        
        mat = Mat(30,19,[(2,5,3)]) 
        self.assertEqual(mat.shape(), (30,19))    

    def test_get_item(self):
        mat = Mat([ [9,5,0],
                    [6,0,4] ]) 
        self.assertEqual(mat[0,0], 9)
        self.assertEqual(mat[1,2], 4)        
        self.assertEqual(mat[-1,0], 6)
        self.assertEqual(mat[-2,1], 5)        
        self.assertEqual(mat[0,-1], 0)

        with self.assertRaises(TypeError):
            mat[1.6,2]
        with self.assertRaises(TypeError):
            mat[0,1.9]
        with self.assertRaises(TypeError):
            mat[0.2,1.2]
        with self.assertRaises(TypeError):
            mat[1,2,3]


    def test_isclose(self):
        mat1 = Mat([(7,5,24), (2,9,13), (1,4,18)]) 
        mat2 = Mat([(7,5,24.1), (2,9,13.1), (1,4,18.1)]) 
        self.assertTrue(mat1.isclose(mat2, 0.2))
        self.assertFalse(mat1.isclose(mat2, 0.05))

    def test_eq(self):
        mat1 = Mat([(7,5,24), (2,9,13), (1,4,18)]) 
        mat2 = Mat([(7,5,24), (2,9,13), (1,4,18)]) 
        mat3 = Mat([(7,5,24), (2,9,13)]) 
        self.assertEqual(mat1, mat1)
        self.assertEqual(mat1, mat2)
        self.assertNotEqual(mat1, mat3)

    def test_add(self):
        import numpy as np
        mat1 = [[7,0,24], [0,0,13], [1,4,18]]
        mat2 = [[7,5,0], [2,9,0], [1,4,18]]
        res = (np.array(mat1) + np.array(mat2)).tolist()
        self.assertEqual(Mat(mat1) + Mat(mat2), Mat(res) )                
    

    def test_mat_by_vec_mul(self):
        import numpy as np
        mat = [[1,0,3],
               [4,5,0]]
        vec = [[1],
               [0],
               [3]]
        res = np.array(mat).dot(np.array(vec)).tolist()        
        self.assertEqual(Mat(mat) * Mat(vec), Mat(res))

    def test_vec_by_mat_mul(self):
        import numpy as np
        vec = [[1,2,0]]
        mat = [ [0, 6, 8, 0],
                [0, 0, 0, 5],
                [9, 0, 7, 0] ]        
        
        res = np.array(vec).dot(np.array(mat)).tolist()
        self.assertEqual(Mat(vec) * Mat(mat), Mat(res))
# Main
def main():

    unittest.main()

if __name__ == '__main__':
    main()