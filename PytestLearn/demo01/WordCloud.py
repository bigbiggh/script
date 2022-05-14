a = ['a','b','c','d']
b = [1,2,3,4]
c = ['aa','bb','cc','dd']

name = 'demo.txt'
with open(name,'a') as n:
    n.write(a+'\n')
    