import arithmetic_operators
import comparison_operators
import assignment_operators

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
    print('dog_name', assignment_operators.dog_name)
    print('dog_age', assignment_operators.dog_age)
    print('dog_toy_count', assignment_operators.dog_toy_count)
    print('dog_friends_count', assignment_operators.dog_friends_count)
    print('dog_treats_count', assignment_operators.dog_treats_count)
    print('dog_sibling_count', assignment_operators.dog_sibling_count)
    print('dog_son_count', assignment_operators.dog_son_count)
