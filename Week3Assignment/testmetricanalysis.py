import numpy as np


np_array = np.random.randint(5, 51, size=(5, 50))
print(np_array)

#Statistical Analysis
test_cycle=1
for i in np_array:
    print(f"Average Test execution time for cycle {test_cycle}: {i.mean()}")
    test_cycle+=1

print(f"Testcase with the maximum execution time: {np_array.max()}")

test_cycle=1
for i in np_array:
    print(f"Standard deviation of execution times for cycle {test_cycle}: {i.std()}")
    test_cycle+=1

#Slicing Operations
print(f"First 10 Execution time from Cycle1: {np_array[0][:10]}")
print(f"Last 5 Execution time from Cycle5: {np_array[4][-5:]}")
print(f"Every alternate Execution time from Cycle3: {np_array[2][::2]}")

#Arithmetic Operations
print(f"Element wise addition between Cycle1 and Cycle2: {np_array[0] + np_array[1]}")
print(f"Element wise subtraction between Cycle1 and Cycle2: {np_array[0] - np_array[1]}")
print(f"Element wise multiplication between Cycle4 and Cycle5: {np_array[3] * np_array[4]}")
print(f"Element wise division between Cycle4 and Cycle5: {np_array[3] / np_array[4]}")

#Power Functions
print(f"Square of all execution times: {np.power(np_array, 2)}")
print(f"Cube of all execution times: {np.power(np_array, 3)}")
print(f"Square root transformation: {np.sqrt(np_array)}")
print(f"Logarithmic transformation: {np.log(np_array+1)}")

#Copy Operations
shallow_copy = np_array.view()
print("#####################################################")
print(f"Shallow copy of the dataset: {shallow_copy}")
shallow_copy[0] = shallow_copy[0] + shallow_copy[1]
print(f"Shallow copy of the dataset after modification: {shallow_copy}")
print(f"Original copy of the dataset which has the same modification of shallow copy: {np_array}")
print("#####################################################")

np_array_new = np.random.randint(5, 51, size=(5, 50))
print(f"New dataset to test deep copy: {np_array_new}")
deep_copy = np_array_new.copy()
print("#####################################################")
print(f"Deep copy of the dataset: {deep_copy}")
deep_copy[0] = deep_copy[0] + deep_copy[1]
print(f"Deep copy of the dataset after modification: {deep_copy}")
print(f"Original copy of the dataset with no modification of deep copy: {np_array_new}")
print("#####################################################")


#Filtering with conditions
print(f"All test cases in Cycle2 that takes more than 30 seconds: {np_array_new[1][np_array_new[1] > 30]}")
print(f"All test cases in all Cycles that takes more than 25 seconds: {np_array_new[np_array_new > 25]}")

