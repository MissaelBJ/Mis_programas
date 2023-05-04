import time

"""for i in range(10):
    print(i)
    time.sleep(1)""" #Duermo el programa por un segundo

"""while True:
    print("Ya pasó un segundo")"""

"""print(time.time())
time.sleep(2)
print(time.time())"""

t1 = time.time()
t2 = time.time()

while True:
    if (t2-t1)<1:
        t2=time.time()
    else:
        t1=time.time()
        print("Ya pasó un segundo")



