

# Build a 3-dim array with the input list and length for 3 axis
def build_mat(x, y, z, L):
    if len(L) != x*y*z:
        return False
    result = list()
    for i in range(x):
        temp1 = list()
        for j in range(y):
            temp2 = list()
            for k in range(z):
                temp2.append(L[i * y * z + j * z + k])
            temp1.append(temp2)
        result.append(temp1)
    return result


# class for array of 3dim
class mat_3d:
    # for now lets just think of a cube
    i = 0
    j = 0
    k = 0
    mat = list()

    def __init__(self, a):
        self.i = len(a)
        self.j = len(a[0])
        self.k = len(a[0][0])
        self.mat = a
        if not self._check_mat():
            print("Error, exit")
            exit()

    def __str__(self):
        mat_str = ''
        for i in range(self.i):
            for j in range(self.j):
                for k in range(self.k):
                    mat_str += str(self.mat[i][j][k])
                    mat_str += ' '
                mat_str += '\n'
            mat_str += '\n'
        return mat_str

    def is_cube(self):
        return self.i == self.j and self.j == self.k

    def cube_len(self):
        if self.is_cube():
            return self.i
        else:
            return 0

    def _check_mat(self):
        if len(self.mat) != self.i:
            print(1)
            return False
        for i in self.mat:
            if len(i) != self.j:
                print(2)
                return False
            for j in i:
                if len(j) != self.k:
                    print(3)
                    return False
        return True

    def element(self, a, b, c):
        if a > self.i or b > self.j or c > self.k:
            return False
        return self.mat[a][b][c]


# Multiplication of Tensor
# D = AxBxC
def op1(mat1, mat2, mat3):
    # Mijk = SUM mat1_ijl mat2_ilk mat3_ljk
    if mat1.cube_len() == mat2.cube_len() == mat3.cube_len():
        length = mat1.cube_len()
        result = list()
        for i in range(length):
            temp1 = list()
            for j in range(length):
                temp2 = list()
                for k in range(length):
                    # append the sum of M_ijk = SUM of mat1_trans
                    sum_ = 0
                    for l in range(length):
                        sum_ += mat1.element(i, j, l) * mat2.element(i, l, k) * mat3.element(l, j, k)
                    temp2.append(sum_)
                temp1.append(temp2)
            result.append(temp1)
        return mat_3d(result)
    else:
        print("error")
        return False


# Returns a simple cube string
def simplecube(mat):
    a = mat.mat
    mat_str = ''
    mat_str += '  ' + str(a[0][0][0]) + ' -- ' + str(a[0][0][1]) + '\n'
    mat_str += str(a[0][1][0]) + ' -- ' + str(a[0][1][1]) + ' |\n'
    mat_str += '| ' + str(a[1][0][0]) + ' -| ' + str(a[1][0][1]) + '\n'
    mat_str += str(a[1][1][0]) + ' -- ' + str(a[1][1][1])
    return mat_str


# returns 3 cube string
def treecubes(mat1, mat2, mat3):
    a = mat1.mat
    b = mat2.mat
    c = mat3.mat
    mat_str = ''
    mat_str += '  ' + str(a[0][0][0]) + ' -- ' + str(a[0][0][1]) + '      '
    mat_str += str(b[0][0][0]) + ' -- ' + str(b[0][0][1]) + '      '
    mat_str += str(c[0][0][0]) + ' -- ' + str(c[0][0][1]) + '    ' +  '\n'

    mat_str += str(a[0][1][0]) + ' -- ' + str(a[0][1][1]) + ' |' + '    '
    mat_str += str(b[0][1][0]) + ' -- ' + str(b[0][1][1]) + ' |' + '    '
    mat_str += str(c[0][1][0]) + ' -- ' + str(c[0][1][1]) + ' |' + '    ' +  '\n'

    mat_str += '| ' + str(a[1][0][0]) + ' -| ' + str(a[1][0][1]) + '    '
    mat_str += '| ' + str(b[1][0][0]) + ' -| ' + str(b[1][0][1]) + '    '
    mat_str += '| ' + str(c[1][0][0]) + ' -| ' + str(c[1][0][1]) + '    ' +  '\n'

    mat_str += str(a[1][1][0]) + ' -- ' + str(a[1][1][1]) + '      '
    mat_str += str(b[1][1][0]) + ' -- ' + str(b[1][1][1]) + '      '
    mat_str += str(c[1][1][0]) + ' -- ' + str(c[1][1][1]) + '    ' +  '\n'

    return mat_str


A_ = build_mat(2, 2, 2, [1, 0, 1, 0, 0, 1, 0, 1])
B_ = build_mat(2, 2, 2, [1, 1, 0, 0, 0, 0, 1, 1])
C_ = build_mat(2, 2, 2, [1, 0, 1, 0, 0, 1, 0, 1])

print(A_)
print(B_)
print(C_)

A = mat_3d(A_)
B = mat_3d(B_)
C = mat_3d(C_)

print(treecubes(A, B, C))

print(simplecube(op1(A, B, C)))
