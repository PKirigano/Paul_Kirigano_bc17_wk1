def prime_num_listing(n):
    alist=[]
    if n < 0:
        raise ValueError
    elif n == 0 and n==1:
        return []
    elif type(n)==str:
        raise ValueError
    else:
        for num in range(2, n):
            for i in range(2,num):
                if (num%i)!=0:
                    alist.append(num)