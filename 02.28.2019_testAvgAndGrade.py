#ToniP
#INF103
#testAvgAndGrade

#determineGrade -- get 5 grades from user and return avg score

def determineGrade(score):
    if score >= 90 and score <= 100:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    elif score >= 0:
        return 'F'
    else:
        return 'Grade out of Bounds'
        
# determin avg of test score
def calcAve(t1,t2,t3,t4,t5):
    avg = (t1 + t2 + t3 + t4 + t5) / 5
    return avg

def main():
    
    #asks user for input
    t1 = float(input('Enter first test score: '))
    t2 = float(input('Enter second test score: '))
    t3 = float(input('Enter third test score: '))
    t4 = float(input('Enter fourth test score: '))
    t5 = float(input('Enter fifth test score: '))

    #call determine grade
    print('test 1 Grad: ', determineGrade(t1))
    print('test 2 Grad: ', determineGrade(t2))
    print('test 3 Grad: ', determineGrade(t3))
    print('test 4 Grad: ', determineGrade(t4))
    print('test 5 Grad: ', determineGrade(t5))

    #call calcAvg

    print('Average score is: ', calcAve(t1,t2,t3,t4,t5))
main()
