def food(cost):
    tip=cost+1.5
    cost=cost+tip
    fperson=cost/num
    return fperson
def movie(m):
    return m/num
num=int(input("enter no.of friends:"))
ftotal=int(input("enter total cost of food:"))
mtotal=int(input("enter total cost of movieS:"))

x=food(ftotal)
y=movie(mtotal) 
print("the  total value ",x+y) 
    