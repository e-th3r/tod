
def mtx1(a, b, c):
    '''
    Задайте одномерный массив аг1 размерности, состоящий из {a} случайных целых чисел в пределах от {b} до {c}. Получите массив индексов, отсортированных по убыванию элементов массива. Выведите на печать массив ar1 с отсортированными элементами. Решить задачу средствами numpy и/или pandas. Не использовать циклы и конструкции стандартного Python там, где можно использовать возможности данных библиотек.
    Args: a,b,c
    '''
    import numpy as np


    ar1 = np.random.randint(a, b, c)


    sorted_indices = np.argsort(-ar1)


    sorted_ar1 = ar1[sorted_indices]


    print("Исходный массив:", ar1)
    print("Индексы по убыванию:", sorted_indices)
    print("Отсортированный массив:", sorted_ar1)

def mtx2(a,b,c,d):
    '''Создать матрицу {a} на {b} из случайных целых (используя модуль 'numpy.random) чисел из диапозона от {c} до {d} и найти в ней строку (ее индекс и вывести саму, строку), в которой сумма значений минимальна.'''
    matrix = np.random.randint(c, d, size=(a, b))


    row_sums = np.sum(matrix, axis=1)


    min_row_index = np.argmin(row_sums)

    min_row = matrix[min_row_index]


    print("Матрица 8x10:")
    print(matrix)
    print("Индекс:",min_row_index)
    print("Сама строка", min_row)