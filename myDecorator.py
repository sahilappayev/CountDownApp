import time


def countDown(arg):
    def wrapperFunc():
        startT = arg()
        for i in range(startT):
            print(f""" >>> {startT} <<< """)
            startT -= 1
            time.sleep(1)
        print("Time up!")

    return wrapperFunc
