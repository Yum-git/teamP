import time


def hello():    
    import datetime
    t1 = time.time()
    nTime = datetime.datetime.now()
    print("名前を入力してください")
    str = input()
    if(nTime.hour<12):
        print("おはようございます "+str)
    elif(nTime.hour>12 and nTime.hour <18):
        print("こんにちは "+str)
    else :
        print("こんばんわ "+str)
        
    pass
    
def wait():
    pass
    
def goodbye():
    pass

hello()