<<<<<<< HEAD
def health_calculator(age, apple_ate, cigar_smoked):
    answer = (100 - age) + (apple_ate * 3.5) - (cigar_smoked * 2)
    print(answer)

kyle_date = [25, 1, 0]

health_calculator(kyle_date[0], kyle_date[1], kyle_date[2])
health_calculator(*kyle_date)
=======
def health_calculator(age, apple_ate, cigar_smoked):                #定义函数，包括3个参数
    answer = (100 - age) + (apple_ate * 3.5) - (cigar_smoked * 2)   #为变量answer设定赋值公式
    print(answer)                                           

kyle_date = [25, 1, 0]                                              #定义一个数组
health_calculator(kyle_date[0], kyle_date[1], kyle_date[2])         #以此输入数组的3个值
health_calculator(*kyle_date)                                       #直接导入整个数组
>>>>>>> master
