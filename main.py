import math

# Определить массив значений шага от 0,5 до 0,6 с шагом 0,01
arr_step = [i*0.01 for i in range(int(0.5/0.01), int(0.6/0.01))]

# Инициализировать пустой список для хранения результатов вычислений функции
arr_result_Built_in_functions = []

# Выполнить итерацию по каждому значению шага в массиве
for x in arr_step:
    # Вычислить значение функции с использованием встроенных математических функций
    # Функция: sqrt((1+x)*exp(2x+1))*sin(0.3x + 0.7)
    arr_result_Built_in_functions.append(math.sqrt((1+x)*math.exp(2*x+1))*math.sin(0.3*x + 0.7))
    ## Вычислите значения функции с помощью встроенных функций




def my_heron(x: float, k: int) -> float:
    """
    Эта функция аппроксимирует значение квадратного корня из x с помощью
    алгоритма Герона.

    :param x: значение, из которого ищется квадратный корень
    :param k: количество шагов алгоритма (количество итераций)
    :return: значение квадратного корня из x
    """
    if k != 0:
        w = my_heron(x, k - 1)
        return (1 / 2) * (w + x / w)
    else:
        return math.ceil(math.sqrt(x))




def my_exp(x: float, e: float) -> float:
    """
    Эта функция аппроксимирует значение e^(2x+1) с использованием ряда Тейлора.
    Точность аппроксимации определяется параметром e.
    """
    n = 0
    f = 0
    t = 2 * x + 1
    # Вычислите количество членов в ряду Тейлора
    while (1 + x) * (math.pow(t, n)) / math.factorial(n) > (e / 0.15):
        n += 1
    # Вычислите значение e ^(2x+1), используя ряд Тейлора
    for i in range(n, -1, -1):
        f += math.pow(t, i) / math.factorial(i)
    return f



def my_cos(x: float, e: float) -> float:
    """
    Эта функция аппроксимирует значение cos(0,3*x + 0,7) с использованием ряда Тейлора.
    Точность аппроксимации определяется параметром e.
    """
    # Вычислите количество членов в ряду Тейлора
    p = 0
    f = 0
    y = math.pi/2-(0.3*x+0.7)
    while (abs(math.pow(y, 2 * p) / math.factorial(2 * p))) > (e / 31.2):
        p += 1
    # Вычислите значение cos(0,3*x + 0,7), используя ряд Тейлора
    for i in range(p, -1, -1):
        f += math.pow(-1, i) * math.pow(y, 2 * i) / math.factorial(2 * i)
    return f




def my_sqrt(x: float, e: float) -> float:
    """
    Аппроксимирует квадратный корень из x, используя модифицированный метод Херона.
    Точность аппроксимации определяется параметром e.

    :param x: Число, из которого нужно извлечь квадратный корень.
    :param e: Желаемая точность аппроксимации.
    :return: приблизительный квадратный корень из x.
    """
    k = 1
    # Вычислите значение косинуса с заданной точностью
    c = my_cos(x, e)
    # Повторяйте до тех пор, пока изменение аппроксимации не достигнет желаемой точности
    while abs(c) * abs(my_heron(x, k) - my_heron(x, k-1)) > (e/3):
        k += 1
    # Окончательное приближение с использованием метода Герона
    f = my_heron(x, k)
    return f


# Запросить у пользователя уровень точности
print("Write degree of exp (The level of accuracy):  ")
# Получить ввод пользователя и преобразовать его в целое число
n = int(input())

# Вычислить значение экспоненты на основе ввода пользователя
e = pow(10, n)

# Использовать выражение-генератор для вычисления результата пользовательской функции
# для каждого значения в arr_step, используя вычисленное значение экспоненты
my_func_result = [
    # Вычислить квадратный корень из ((1+x) * exp(x, e)) с точностью e,
    # затем умножить на косинус (x, e)
    my_sqrt((1+x)*my_exp(x, e), e)*my_cos(x, e)
    for x in arr_step
]

# Перебрать результаты и вывести их вместе с результатами встроенной функции
for i in range(len(arr_step)):
    # Вывести результат встроенной функции и пользовательской функции
    print(f"{arr_result_Built_in_functions[i]}  {my_func_result[i]}")

## 17







