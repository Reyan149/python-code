def get_max_consecutive_ones(binary_array):

    max_steak = 0
    current_steak = 0

    for number in binary_array:
        if number == 1:
            current_steak += 1
            if current_steak > max_steak:
                max_steak = current_steak
        else:
            current_steak = 0
    return max_steak


sample_binary = [1,0,1,1,1,1,0,1,1,0]
print(f'Max consecutive ones : {get_max_consecutive_ones(sample_binary)}')
