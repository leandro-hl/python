def cuentaRegresiva2(n):
    if n == 0:
        print("0")
    else:
        print(n)
        cuentaRegresiva(n-1)
 
def cuentaRegresiva(n):
    print(n)
    cuentaRegresiva(n-1)
    
 
def cuentaRegresivaIterativa(n):
   for i in range(n,-1,-1):
       print(i)
       

cuentaRegresiva(3)