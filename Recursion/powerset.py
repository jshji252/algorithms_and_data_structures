def power_set(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [ [my_list[0]] + rest for rest in without_first ]
    # return combination of the two
    return with_first + without_first
  
universities = ['A', 'B', 'C', 'D']
power_set_of_universities = power_set(universities)
print(power_set_of_universities)