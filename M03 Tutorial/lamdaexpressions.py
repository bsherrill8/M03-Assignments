#lambdaexpressions.py
#Brian Sherrill
#9/12/2022


#square

my_list = [5,4,3]

print(list(map(lambda i: i**2, my_list)))

#list sorting

a = [(0,2), (4,3), (9,9), (10,-1)]

a.sort(key = lambda i: i[1])
print(a)