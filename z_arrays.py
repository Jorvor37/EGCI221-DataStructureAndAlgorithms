new_list = [1,2,3]
result = new_list[0]        #constant time operation

if 1 in new_list: print(True)

for n in new_list:
    if n == 1:
        print(True)

        break

#insert in python have inseart patern: 4,8,16,...
# O(k)
numbers = []
numbers.extend([4,5,6])
print(numbers)

#delete