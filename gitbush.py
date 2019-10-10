import time
import sys

def hello():
    return time.time()
    
def wait():
    from time import sleep
    print("please wait a minute");
    sleep(60);
    print("thanks");
    pass
    
def goodbye():
    t2 = time.time()
    print('Goodbye everyone')
    print('経過時間:')
    print(str(t2 - t1) + '秒')
    sys.exit()

t1 = hello()



    
  
    
