from urllib import request

bidu_url = 'http://chart.finance.yahoo.com/table.csv?s=BIDU&a=10&b=5&c=2016&d=11&e=5&f=2016&g=d&ignore=.csv'  #url过长，把它放在一个变量里
def download_data(csv_url):
    response = request.urlopen(csv_url) #打开url
    csv = response.read() #读取URL中的内容
    csv_str = str(csv)  #将其中的内容转化为str
    lines = csv_str.split('\\n')  #分行
    name_url = r'BIDU.csv'  #命名文件，放在一个变量里
    fx = open(name_url, 'w')  #将变量写在另一个文件里
    for line in lines:
        fx.write(line + '\n') #划分行
    fx.close()

download_data(bidu_url) #执行函数
