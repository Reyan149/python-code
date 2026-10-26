def find_target_window(window_size):
    data_array = [0] * window_size + [1] * window_size
    total_length = len(data_array)
    target_value = window_size

    print(f'--- Configuration ---')
    print(f'Array: {data_array}')
    print(f'Window Size: {window_size} | Target Sum: {target_value}\n')
    print(f'--- Step by Step Window Scan ---')

    for window_start_index in range(total_length - window_size + 1):
        window_sum = 0
        current_window_elements = []

        for element_index in range(window_start_index, window_start_index + window_size):
                current_value = data_array[element_index]
                window_sum += current_value
                current_window_elements.append(current_value)

        print(f'Index {window_start_index}: Subarray {current_window_elements} -> Sum = {window_sum} ')

        if window_sum == target_value: 
            print(f'Match found! Target sum {target_value} matched at starting index {window_start_index}.')
            return window_start_index

    print('No matching window found.')
    return -1

n = int(input('Enter n (try 5 or 6'))
result_index = find_target_window(n)
print(f'\nFinal Function Output: {result_index}')