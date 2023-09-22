import copy

original = [1,2,3]
target = original
print(original, target)
original[0] = 100
print(original, target)

original = [1,2,3]
target = copy.deepcopy(original) #deepcopy로 값 고정
print(original, target)
original[0] = 100
print(original, target)