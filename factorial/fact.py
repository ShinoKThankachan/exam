def fact():
    x=int(input("enter a number:"))
    factorial=1
    for i in range(1,x+1):
        factorial*=i
    print(factorial)
fact()
        
