#coding:utf-8
import threading

class myThread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        self.result = apply(self.func, self.args)

    def getResult(self):
        return self.result

#循环创建并发线程
def loop_create_func(func, loop_args):
    treads = []
    for i in range (0, len(loop_args)):
        t = myThread(func, loop_args[i])
        treads.append(t)
    return treads

def loop_threads_start(treads):
    for i in range(0, len(treads)):
        treads[i].start()

def loop_threads_join(treads):
    for i in range(0, len(treads)):
        treads[i].join()

'''
def test_func(a, b):
    if a > b:
        print '第一位数必须小于第二位数'
    else:
        for i in range(a, b):
            print i


loop_args = [(3000, 4000), (1000,2000),(9000,10000)]

treads = loop_create_func(test_func, loop_args)
loop_threads_start(treads)
loop_threads_join(treads)
'''
