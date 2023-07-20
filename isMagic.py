def isMagic(res):
    sum=0
    while res>0:
        sum+=res%10
        res //=10
    if sum>9:
        return isMagic(sum)
    else:
        if sum==1:
            return 1
        else:
            return 0
number=int(input())
print(isMagic(number))