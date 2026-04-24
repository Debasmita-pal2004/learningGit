def fibonacci(a,b,n):
    if n==0:
        return
    c=a+b
    print(c)
    fibonacci(b,c,n-1)
n=5
a=0
b=1
print(a)
print(b)
fibonacci(a,b,n-2)