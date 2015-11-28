"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler010
"""

TEST_MTX = ['99 44 55 66 38 15 00 40 00 75 04 05 07 78 52 12 66 55 44 33',
            '99 77 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 99 00',
            '99 49 88 73 55 79 14 29 93 71 40 67 53 88 30 03 49 88 36 11',
            '99 70 95 99 04 60 11 42 69 24 68 56 01 32 56 71 77 02 36 22',
            '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80',
            '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50',
            '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70',
            '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21',
            '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72',
            '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95',
            '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92',
            '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57',
            '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58',
            '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40',
            '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66',
            '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69',
            '22 42 16 55 38 25 39 11 24 94 72 18 08 46 29 32 22 62 76 01',
            '33 69 66 41 72 30 23 88 34 62 99 69 82 67 59 85 74 33 36 12',
            '44 77 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 22 15',
            '22 88 00 11 83 51 54 69 16 92 33 48 61 43 52 01 60 12 07 33']


def horiz_max(row):
    best_prod = 0
    for col_no in range(len(row) - 3):
        prod = row[col_no] * row[col_no + 1] * row[col_no + 2] * row[col_no + 3]
        best_prod = max(prod, best_prod)
    return best_prod


def vert_max(row1, row2, row3, row4):
    best_prod = 0
    for col_no in range(len(row1)):
        prod = row1[col_no] * row2[col_no] * row3[col_no] * row4[col_no]
        best_prod = max(prod, best_prod)
    return best_prod


def diag_max(row1, row2, row3, row4):
    best_prod = 0
    for col_no in range(len(row1) - 3):
        prod = row1[col_no] * row2[col_no + 1] * \
               row3[col_no + 2] * row4[col_no + 3]
        best_prod = max(best_prod, prod)
    return best_prod


def anti_diag_max(row1, row2, row3, row4):
    best_prod = 0
    for col_no in range(3, len(row1)):
        prod = row1[col_no] * row2[col_no - 1] * \
               row3[col_no - 2] * row4[col_no - 3]
        best_prod = max(best_prod, prod)
    return best_prod


def find_max_product(mtx):
    """
    finds the maximum product of four adjacent numbers in a matrix in
    the same direction
    :param mtx: matrix represented as list of lists
    :return: integer of maximum product
    """
    max_prod = 0
    for row_num in range(20):
        vert = 0
        diag = 0
        anti_diag = 0
        horiz = horiz_max(mtx[row_num])
        if row_num < len(mtx) - 3:
            vert = vert_max(mtx[row_num], mtx[row_num + 1],
                            mtx[row_num + 2], mtx[row_num + 3])
            diag = diag_max(mtx[row_num], mtx[row_num + 1],
                            mtx[row_num + 2], mtx[row_num + 3])
            anti_diag = anti_diag_max(mtx[row_num], mtx[row_num + 1],
                                       mtx[row_num + 2], mtx[row_num + 3])
        max_prod = max(max_prod, horiz, vert, diag, anti_diag)
    return max_prod


def test():
    test_mtx = []
    for row in TEST_MTX:
        test_mtx.append([int(itm) for itm in row.split()])
    print(find_max_product(test_mtx))
    if find_max_product(test_mtx) == 96059601:
        print ('correct')


def run_battery():
    euler_mtx = []
    for idx in range(20):
        euler_mtx.append([int(itm) for itm in input().split()])
    print(find_max_product(euler_mtx))


run_battery()
# test()
