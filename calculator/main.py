while(True):
    uc=int(input('''
             1.Addition
             2.Substraction
             3.Multiplication
             4.division
             5.exit
             Enter your choice:'''))

    if uc==1:
        from add import ad
        c=ad()
        print(c)
    elif uc==2:
        from sub import subs
        c=subs()
        print(c)
    elif uc==3:
        from mul import multi
        c=multi()
        print(c)
    elif uc==4:
        from div import divi
        c=divi()
        print(c)
    elif uc==5:
        break
    else:
        print("invalid choice")
        