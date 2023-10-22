



def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[1+j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
my_list = [1,2,5,7,9,0,3,10,11,50,29,100,654,787,34]
print(f'список чисел не отсротированных: {my_list}')
print(f'список чисел отсоритированных:',bubble_sort(my_list))
def binarySearch(my_list1, N):
    first = 0
    last = len(my_list1) - 1
    resultOk = False

    while first <= last and not resultOk:
        middle = (first + last) // 2
        val = my_list[middle]
        if val == N:
            resultOk = True
        if val > N:
            last = middle - 1
        else:
            first = middle + 1
    return resultOk


my_list1 = [1,2,5,7,9,0,3,10,11,50,29,100,654,787,34]
el_find = 29
result = binarySearch(my_list1,el_find)

if result:
    print(f'число найден: {el_find} вот список: {my_list1}')
else:
    print(f'число не найден: {el_find} вот список:{my_list1}')

