'''Калькулятор среднего арифметического значения

Описание: Этот модуль содержит функцию вычисления среднего значения списка
'''

def calculate_average(numbers):
    '''вычисляем среднее арифметическое'''
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
