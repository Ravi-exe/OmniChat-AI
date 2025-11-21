from contextlib import contextmanager
import time



@contextmanager
def auto_clear():
    print("start an app")
    time.sleep(10)
    yield "wait"
    print("now closing my app")
    time.sleep(10)
    print("closed")

    

# next(auto_clear())
# print(app)


# with auto_clear() as a:
#     print(a)




class myclass:

    def __init__(self):
        print(self)    

    def __enter__(self):
        print("started run")
        return 0

    def __exit__(self, *args):
        print("exit", args)
        return 1
    
    def __call__(self):
        print("creating an map from class")



with myclass() as m:
    print(m)
