def rainwater(n):

    bars = [0,n,0,n,0]

    left_walls = bars[:3]
    tallest_left = max(left_walls)

    right_walls = bars[2:]
    tallest_right = max(right_walls)

    water_level = min(tallest_left, tallest_right)

    ground_height = bars[2]
    trapped_water = water_level - ground_height

    return trapped_water

print('Water Trapped: ', rainwater(5))