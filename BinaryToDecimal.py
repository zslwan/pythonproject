#coding:utf8
#将二进制转化为十进制数字
B = input('输入一个二进制数字：')
B = str(B)
#B = '1101'
I = 0
while B!='':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]
print I
