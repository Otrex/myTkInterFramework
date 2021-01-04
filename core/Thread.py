import threading 
import ctypes 
import time 
   
class thread_with_exception(threading.Thread): 
    def __init__(self, target=None, cb=None, args=[], cb_args=[]): 
        threading.Thread.__init__(self) 
        assert target != None, "Incorrect parameter for target. Function is required" 
        self.fnc = target
        self._args = args
        self._args2 = cb_args
        self.cb = cb
              
    def run(self): 
        try:
            self.fnc(*self._args)
        finally:
            if self.cb != None:
                self.cb(*self._args2)
            pass
           
    def get_id(self): 
        # returns id of the respective thread 
        if hasattr(self, '_thread_id'): 
            return self._thread_id 
        for id, thread in threading._active.items(): 
            if thread is self: 
                return id
   
    def raise_exception(self): 
        thread_id = self.get_id() 
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 
              ctypes.py_object(SystemExit)) 
        if res > 1: 
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0) 
            print('Exception raise failure') 
       

class pThread(thread_with_exception):
    def stop(self):
        self.raise_exception()
        self.join()

    @staticmethod
    def time(target = None, cb=None, cb_args=[], time_count = 0, args = []):
        def cover():
            time.sleep(time_count)
            target(*args)
        t = pThread(target=cover, cb=cb, cb_args=cb_args)
        t.start()
        return t
        
        

if __name__ == '__main__':
    def fnc():
        while True:
            print('happy', end='')

    pThread.time(fnc, time_count=5)

    # t1 = thread_with_exception(target=fnc) 
    # t1.start() 
    # time.sleep(1) 
    # t1.raise_exception() 
    # t1.join() 