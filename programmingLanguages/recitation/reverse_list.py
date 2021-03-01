test_list = [1, 2, 3]

return_list = []

index = len(test_list) - 1
for item in test_list:
    return_list.append(test_list[index])
    index -= 1
print(return_list)

print(test_list[::-1])
test_list.reverse()
print(test_list)
