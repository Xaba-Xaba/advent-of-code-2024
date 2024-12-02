import numpy as np
import time

FILE_NAME = 'data/day02.txt'

with open (FILE_NAME) as f:
    lines = f.readlines()

# Part 1

def check_if_increasing(arr):
    
    diff = np.diff(arr)
    
    if np.all(diff > 0):
        if (max(diff)< 4) and (min(diff)>0):
            return True
        
    return False
        
        
def check_if_decreasing(arr):
    
    diff = np.diff(arr)
    
    if np.all(diff < 0):
        if (max(abs(diff))< 4) and (min(abs(diff))>0):
            return True

    return False

indicies_to_save = list()

for index, report in enumerate(lines):

    report = [int(char) for char in report.split()]   
    arr = np.array(report)
    
    # Check for increasing pattern
    if check_if_increasing(arr):
        indicies_to_save.append(index)
        continue
                      
    # Check for decreasing pattern
    if check_if_decreasing(arr):
        indicies_to_save.append(index)


print(f'{len(set(indicies_to_save))} reports are safe') 

# Part 2

def search_for_single_bad_level(arr):
    for i in range(len(arr)):
        new_arr = np.delete(arr, i)
        
        if check_if_increasing(new_arr):
            return True
        
        if check_if_decreasing(new_arr):
            return True
        
    return False

indicies_to_save = list()

for index, report in enumerate(lines):

    report = [int(char) for char in report.split()]   
    arr = np.array(report)
    
    #increasing
    if check_if_increasing(arr):
        indicies_to_save.append(index)
        continue
            
    #decreasing
    if check_if_decreasing(arr):
        indicies_to_save.append(index)
        continue
            
    # Search for any luck removing one level
    if search_for_single_bad_level(arr):
        indicies_to_save.append(index)

print(f'{len(set(indicies_to_save))} reports are safe')