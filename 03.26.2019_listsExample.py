#Steven Waring

def main():
    
    user = []
    count = 0
    while count < 20:
        user.append(int(input('Please enter a number: ')))
        count += 1

    print('Smallest number in the list: ',min(user),'Largest number in the list: ',max(user))
    print('Total numbers in list: ',len(user))
    print('Total: ',sum(user))
    print('Average: ',sum(user)/len(user))
main()
