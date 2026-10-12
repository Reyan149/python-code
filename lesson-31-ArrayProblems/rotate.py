def left_rotate_shift(shift_amount):

    numbers = [1, 2, 3, 4, 5]

    length_of_list = len(numbers)
    
    shift_amount = shift_amount % length_of_list

    rotated_numbers = numbers[shift_amount:] + numbers[:shift_amount]

    return rotated_numbers

print('Left rotated by 2 : ', left_rotate_shift(2))