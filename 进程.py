#!/usr/bin/env python3
#antuor:Alan
#
# import multiprocessing
# import time
# def worker(interval):
#     n = 5
#     while n>0:
#         print('The tie is {0}'.format(time.ctime()))
#         time.sleep(interval)
#         n-=1
# if __name__ == "__main__":
#     p = multiprocessing.Process(target = worker,args =(3,))
#     p.start()
#     print("p.pid:",p.pid)
#     print("p.name:",p.name)
#     print("p.is_alive:",p.is_alive())



# import multiprocessing
# import time
# def worker_1(interval):
#     print("worker_1")
#     time.sleep(interval)
#     print('end worker_1')
# def worker_2(interval):
#     time.sleep(interval)
#     print("end worker_2")
# def worker_3(interval):
#     time.sleep(interval)
#     print("end worker_3")
#
# if __name__ =="__main__":
#     p1 = multiprocessing.Process(target= worker_1,args=(2,))
#     p2 = multiprocessing.Process(target= worker_2,args=(3,))
#     p3 = multiprocessing.Process(target= worker_3,args=(4,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     print("the number of CPU is :",str(multiprocessing.cpu_count()))
#     for p in multiprocessing.active_children():
#         print("child p.name:{0} tp.id{1}".format(p.name,str(p.pid)))
#     print('end')


import multiprocessing
import time

class ClockProcess(multiprocessing.Process):
    def __init__(self,interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        n =5
        while n>0:
            print('the time is {0}'.format(time.ctime()))
            time.sleep(self.interval)
            n-=1

if __name__ == "__main__":
    p=ClockProcess(3)
    p.start()
