import datetime, time

#code designed to run the algorithm from question 2 in End of Year 10 Computer Science test
while True:
    hour = datetime.datetime.now().hour
    if (hour>=3) and (hour<12):
        print('Good morning')
    elif (hour>=13) and (hour<=19):
        print('Good afternoon')
    else:
        print('Good evening')
    time.sleep(60)