OPMAT = [
        [[1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]],

        [[0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0]],

        [[0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]],

        [[0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]]]

class mat2d:
    matrix = list()
    def __init__(self, a, b, c, d):
        self.matrix = [[a, b], [c, d]]
    def __str__(self):
        mat_str = ''
        a = self.matrix
        mat_str += str(a[0][0]) + ' -- ' + str(a[0][1]) + '\n'
        mat_str += '|    |\n'
        mat_str += str(a[1][0]) + ' -- ' + str(a[1][1])
        return mat_str
    def listify(self):
        a = [0,0,0,0]
        b = self.matrix
        a[0] = b[0][0]
        a[1] = b[0][1]
        a[2] = b[1][0]
        a[3] = b[1][1]
        return a

def inner(v1, v2):
    sum_ = 0
    if(len(v1) != len(v2)):
        return False
    for i in range(len(v1)):
        sum_ += v1[i] * v2[i]
    return sum_

def make_trans(mat):
    trans = list()
    mat_list = mat.listify()
    for i in range(4):
        temp_trans = list()
        for j in range(4):
            temp_trans.append(inner(OPMAT[i][j], mat_list))
        trans.append(temp_trans)
    return trans

def op1(mat1, mat2):
    mat1_list = mat1.listify()
    mat2_list = mat2.listify()
    mat1_trans = make_trans(mat1)
    result = list()
    for i in range(4):
        result.append(inner(mat1_trans[i], mat2_list))
    return result

a = mat2d(1, 2, 3, 4)
print(a)
print(a.listify())
print(make_trans(a))
t = op1(a, a)
print(mat2d(t[0], t[1], t[2], t[3]))
