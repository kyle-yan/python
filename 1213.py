# 提取标签并进行排序
from operator import attrgetter

class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + ' : ' + str(self.user_id)

users = [
    User('Bucky', 13),
    User('Sally', 23),
    User('Tuna', 61),
    User('Brian', 2),
    User('Joby', 88),
    User('Tom', 56)
]

for user in users:
    print(user)

print('--------')

for user in sorted(users, key=attrgetter('name')): # itemgetter用法类似
    print(user)

print('--------')

for user in sorted(users, key=attrgetter('user_id')):
    print(user)


# 计算词频
from collections import Counter

text = "Beijing could react with countermeasures in trade and regional issues, if Trump keeps challenging the time-tested one-China policy, which is the diplomatic cornerstone of relations between the world's two biggest economies, Chinese experts said."\
       "In a Fox News broadcast on Sunday, Trump said the United States does not necessarily have to stick to its long-standing position that Taiwan is part of \"one China\", challenging the consensus that the two countries have upheld for nearly four decades."

words = text.split()

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)

# 求最小值与zip的运用
stocks = {
    'GOOG': 434,
    'AAPL': 325,
    'FB': 54,
    'AMZN': 623,
    'F':32,
    'MSFT':549,
}

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)

# 求最大值
import heapq

grades = [100, 99, 94, 23, 56, 77, 13, 24]
print(heapq.nlargest(2, grades))

stocks = [
    {'ticker': 'AAPL', 'price': 201},
    {'ticker': 'GOOG', 'price': 21},
    {'ticker': 'FB', 'price': 251},
    {'ticker': 'AMZN', 'price': 520},
    {'ticker': 'YAHH', 'price': 23},
]

print(heapq.nlargest(2, stocks, key=lambda stock: stock['price']))

income = [10, 30, 75]

def double_money(dollars):
    return dollars * 2

new_income = list(map(double_money, income))
print(new_income)


# 二进制数的运算调整
from struct import *


# Store as bytes data
pack_data = pack('iif', 6, 19, 4.73)
print(pack_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))


# To get bytes data back to normal(b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@')
original_data = unpack('iif', pack_data)
print(original_data)
print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))


# lambda 不定义参数的函数
answer = lambda x: x * 7
print(answer(5))

# zip 将数据进行整合重组
first = ['Bucky', 'Tom', 'Taylor']
last = ['Roberts', 'Hanks', 'Swift']

names = zip(first, last)

for a,b in names:
    print(a, b)

# zip用于字典
stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'AAPL': 99.76
}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.keys(), stocks.values())))

# 去掉最高和最低的
def drop_first_last(grades):
    first, *middle, last = grades  # *middle代表中间的所有
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([66, 88, 33, 22, 56, 99])
drop_first_last([18, 22, 33, 44, 55, 66, 77, 88, 99])
