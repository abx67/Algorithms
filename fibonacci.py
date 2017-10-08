def fibonacci(n):
    if n==0:
        return False
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
        return (fibonacci(n-1)+fibonacci(n-2))