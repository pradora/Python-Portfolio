#ToniP
#INF103
#employeDriver

from employeeClass import *
def main():

    #user input
    eName= input('Please input your name: ')
    eNum = input('Please input your ID number: ')
    eDept = input('Please input your Department: ')
    eJob = input('Please input your Job Title: ')

    #####Employee info
    #Creat instance of employee
    iEmployee = Employee(eName,eNum,eDept,eJob)

    ####Display employee info
    print("Employee Name: ", iEmployee.getName())
    print("ID Number: ", iEmployee.getIdnum())
    print("Employee Department: ", iEmployee.getDept())
    print("Employee Title: ", iEmployee.getTitle())

    
main()
