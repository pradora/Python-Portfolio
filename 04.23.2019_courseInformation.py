#ToniP
#INF103
#courseInformation

def main():
    #create dictionary CourseNumber Dictionary
    courseRoom = {'CS101':'3004','CS102':'4501','CS103':'6755','NT110':'1244','CM241':'1411'}
    couseInstructor ={'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
    courseTime = {'CS101':'8:00 a.m.','CS102':'9:00 a.m.','CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 p.m.'}

    #ask user for course number
    cNum = input('Enter course Number: ').upper().strip()

    if cNum in courseRoom:
        print('Course room number', courseRoom[cNum],'\n', 'Course instructor: ', couseInstructor[cNum],'\n', 'Course Time: ',courseTime[cNum])

    else:
        print('Please re-enter course number')
        main()

    

main()
