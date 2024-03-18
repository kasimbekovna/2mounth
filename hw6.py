def selection_sort(lst):
    n = len(lst)

    for i in range(n - 1):
        min_index = i

        for m in range(i + 1, n):
            if lst[m] < lst[min_index]:
                min_index = m


        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst

nums = [324, 423, 53, 6321, -1, 0, -34, 23456, 534]
print(selection_sort(nums))



def binary_search(A, Val):
    First = 0
    Last = N - 1
    ResultOk = False

    while First <= Last:
        Middle = (First + Last) // 2
        if A[Middle] == Val:
            ResultOk = True
            break
        elif A[Middle] < Val:
            First = Middle + 1
        else:
            Last = Middle - 1

    if ResultOk:
        return Middle
    else:
        return - 1


N = 5000
Val = 4999
nums = list(range(N))
result = binary_search(nums, Val)

if result != -1:
    print('Элемент найден в индексе', result)
elif result == -1:
    print("Элемент не найден!")
