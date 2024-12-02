FILE_NAME = 'data/day01.txt'

with open (FILE_NAME) as f:
    lines = f.readlines()

left_list, right_list = list(), list()

for line in lines:

    temp_list = line.split(' ' * 3)
    
    left_list.append(int(temp_list[0]))
    right_list.append(int(temp_list[1]))

#print('Left list:\n', left_list)
#print('Right list\n', right_list)

# Part 1

total_distance = 0

for item_L, item_R in zip(sorted(left_list), sorted(right_list)):

    total_distance += abs(item_L - item_R)
    
print('Total distance between two lists: ', total_distance)

# Part 2

from collections import Counter
count = Counter(right_list)

similarity_score = 0

for item in left_list:
    if item in count.keys():
        similarity_score += item * count [item]
        
print('similarity_score: ', similarity_score)

# as an alternative solution with NumPy

from numpy import loadtxt, sort, isin

list_L, list_R = sort(loadtxt(FILE_NAME, int).T)

print(sum(abs(list_L-list_R)))

print(sum(isin(list_R, list_L)* list_R))
