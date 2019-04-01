import arithmetic_operators, comparison_operators, assignment_operators, bitwise_operators, logical_operators, membership_operators, identity_operators

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

    print('\n###  Assignment Operators ###')
    print('get_dog_name', assignment_operators.get_dog_name('Jonathan'))
    print('get_dog_age', assignment_operators.get_dog_age(3))
    print('get_dog_toy_count', assignment_operators.get_dog_toy_count(4))
    print('get_dog_friends_count', assignment_operators.get_dog_friends_count(10))
    print('get_dog_treats_count', assignment_operators.get_dog_treats_count(24))
    print('get_dog_sibling_count', assignment_operators.get_dog_sibling_count(2))
    print('get_dog_son_count', assignment_operators.get_dog_son_count(10))

    print('\n###  Bitwise Operators ###')
    print('binary_and', bitwise_operators.binary_and(60, 13))
    print('binary_or', bitwise_operators.binary_or(60, 13))
    print('binary_xor', bitwise_operators.binary_xor(60, 13))
    print('binary_once_comp', bitwise_operators.binary_once_comp(60))
    print('binary_left_shift', bitwise_operators.binary_left_shift(60, 2))
    print('binary_right_shift', bitwise_operators.binary_right_shift(60, 2))

    print('\n###  Logical Operators ###')
    print('both_true', logical_operators.both_true(1 == 1, 2 > 1))
    print('any_true', logical_operators.any_true(1 != 1, 2 > 1))
    print('reverse_state', logical_operators.reverse_state(True))

    print('\n###  Membership Operators ###')
    print('is_inside', membership_operators.is_inside('c', ['b', 'c', 'a']))
    print('is_not_inside', membership_operators.is_not_inside('z', ['b', 'c', 'a']))

    print('\n###  Identity Operators ###')

    a = []
    b = a
    c = list(a)

    print('same', identity_operators.same(a, c))
    print('not_same', identity_operators.not_same(a, c))