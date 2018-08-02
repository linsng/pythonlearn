import os;

#创建目录
path = 'txtfile'
try:
    if not os.path.exists(path):
        os.mkdir(path)

except EnvironmentError as e:
    print('exception:', e)
finally:
    print('mkdir occur error')

#写入文件, 如果文件不存在会自动新建文件并写人
with open('txtfile/test.txt', 'w') as f:
    f.write('Hello Python')

#一次性读取
with open('txtfile/test.txt', 'r') as fileRead:
    print(fileRead.read())
