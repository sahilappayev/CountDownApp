from myDecorator import countDown


@countDown
def startApp():
    startTimeStr = input("Enter start time or enter q for quit:\n>>")
    if startTimeStr.strip().isnumeric():
        startTime = int(startTimeStr)
    elif startTimeStr == 'q':
        print("Program stopped!")
        exit()
    else:
        print("Wrong input!")
    return startTime
