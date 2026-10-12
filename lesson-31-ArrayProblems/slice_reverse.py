def reverse_in_groups(slice_length):

    numbers = [1,2,5,7,9,11]

    length_of_list = len(numbers)


    for start_index in range(0, length_of_list, slice_length):

       slice = numbers[start_index : start_index + slice_length]

       slice.reverse()

       numbers[start_index : start_index + slice_length] = slice
    return numbers

slice_length = int(input("Enter the slice length: "))
print("Reverse in groups:", reverse_in_groups(slice_length))



       