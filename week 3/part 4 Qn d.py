
try:
    mark = int(input('Enter your exam mark: '))

    if mark < 0 or mark > 100:
        print('Invalid exam mark. Please enter a mark between 0 and 100.')
    elif mark >= 70:
        print('Exceptional result!')
    elif mark >= 40:
        print('Satisfactory result!')
    else:
        print('You have failed.')

except ValueError:
    print('Please enter a valid integer for the exam mark.')
