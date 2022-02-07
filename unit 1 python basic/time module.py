import time

def myfun(fn,*arg,rep=1,**kwargs):
    start = time.perf_counter()
    for i in range (rep):
        fn(*arg,**kwargs)
        
    end = time.perf_counter()
    avgtime = (end-start) / rep
    fn (avgtime)

myfun(print,1,2,3,end ='***\n',rep = 5)