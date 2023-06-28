def find_combinations(arr, target):
    complements = {}
    first_combination = []
    
    # Step 1: Find pairs that sum up to the target value
    for num in arr:
        complement = target - num
        if complement in complements:
            first_combination.append([num, complement])
        complements[num] = complement
    
    # Step 4: Sort the first combination in ascending order
    first_combination.sort()
    
    # Step 5: Merge the first combination into a single array
    merged_array = [num for pair in first_combination for num in pair]
    
    # Step 6: Double the target value
    target *= 2
    
    # Step 7: Find pairs that sum up to the doubled target value
    second_combination = []
    for num in merged_array:
        complement = target - num
        if complement in complements:
            second_combination.append([num, complement])
    
    # Step 9: Sort the second combination in ascending order
    second_combination.sort()
    
    return first_combination, second_combination
