# 'hello, {name}!'と出力してください 。
def hello(name):
    print('hello, {0}!'.format(name))


# sentence の文字数を出力してください
def length(sentence):
    print(len(sentence))


# sentence の2文字目から5文字目まで(5文字目は含まない)を出力してください
def slicing2to5(sentence):
    print(sentence[2:5])

# number の符号を出力してください。ただし、0は'0'と出力してください
def number_sign(number):
    if number > 0: return 1
    else: return 0
# number が素数なら'ok',そうでないなら'ng'と出力してください
def prime_number(number):
    def is_prime(x):
        if x < 2:
            return'ng'
        elif x == 2:
            return True
        elif x % 2 == 0 or x % number(x) == 0:
            return'ng'
        else:
            return'ok'


# 1からnumberまでの合計を出力してください
def sum_from_1_to(number):
    def sum_list(l):
        sum = 0
        for x in l:
            sum += x
        return sum


# numberの階乗(factorial)を出力してください
def factorial(number):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
# リストdataの各要素(整数)を3乗した結果をリスト型として返してください
def cubic_list(data):



# 底辺x,高さyの直角三角形(right angled triangle)の残り1つの辺の長さを返してください
def calc_hypotenuse(x, y):
    print(x, y)


# 底辺x,斜辺vの直角三角形の残り1つの辺の長さを返してください
def calc_subtense(x, v):
    print(x, v)


# 三辺の長さがそれぞれx,y,zの三角形の面積を返してください
def calc_area_triangle(x, y, z):
    print(x, y, z)


# 引数a,b,cを小数点以下2桁表示で空白切りで表示してください
def point_two_digits(a, b, c):
    print(a, b, c)


# リストdataの内容を小さい順でソートした結果を返してください
def list_sort(data):
    print(data)


# 文字列の並びを逆にしたものを返してください
def reverse_string(sentence):
    print(sentence)


# dateから2016年4月1日までの日数を返してください
def days_from_date(point):
    print(point)
