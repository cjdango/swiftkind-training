import arithmetic_operators
import comparison_operators

if __name__ == '__main__':
    print('###  Arithmetic Operators ###')
    print('add(1, 2) =', arithmetic_operators.add(1, 2))
    print('sub(3, 2) =', arithmetic_operators.sub(3, 2))
    print('mult(3, 3) =', arithmetic_operators.mult(3, 3))
    print('div(15, 3) =', arithmetic_operators.div(15, 3))
    print('get_remainder(15, 4) =', arithmetic_operators.get_remainder(15, 4))
    print('pow(4, 4) =', arithmetic_operators.pow(4, 4))
    print('floor_div(9, 2) =', arithmetic_operators.floor_div(9, 2))

    print('\n###  Comparison Operators ###')
    print('is_equal(3, 3) =', comparison_operators.is_equal(3, 3))
    print('not_equal(3, 1) =', comparison_operators.not_equal(3, 1))
    print('left_greater(3, 1) =', comparison_operators.left_greater(3, 1))
    print('left_lesser(1, 5) =', comparison_operators.left_lesser(1, 5))
    print('left_greater_equal(3, 6) =', comparison_operators.left_greater_equal(3, 6))
    print('left_greater_equal(6, 6) =', comparison_operators.left_greater_equal(6, 6))
    print('left_lesser_equal(3, 6) =', comparison_operators.left_lesser_equal(3, 6))
    print('left_lesser_equal(6, 6) =', comparison_operators.left_lesser_equal(6, 6))