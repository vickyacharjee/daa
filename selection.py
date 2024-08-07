import random
import timeit

# Input Array elements
def input_array(array, n):
    for i in range(n):
        ele = random.randrange(1, 50)
        array.append(ele)

# Selection Sort
def selection_sort(array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        array[ind], array[min_index] = array[min_index], array[ind]

# Main Block
def main():
    N = []
    CPU = []
    trail = int(input("Enter no. of trials: "))
    
    for t in range(trail):
        array = []
        print(f"-----> TRIAL NO: {t + 1}")
        n = int(input("Enter number of elements: "))
        input_array(array, n)
        
        start = timeit.default_timer()
        selection_sort(array, n)
        elapsed_time = timeit.default_timer() - start
        
        print("Sorted Array:")
        print(array)
        
        N.append(n)
        CPU.append(round(elapsed_time * 1000000, 2))
    
    print("N CPU")
    for i in range(trail):
        print(N[i], CPU[i])

if __name__ == "__main__":
    main()
