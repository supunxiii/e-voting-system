import time
print('Hi!')
time.sleep(2)
print("First, we need to verify your age")
time.sleep(1)
if int(input('Please enter your age:\n'))>=18:
    print("Congratulations! You're eligible to vote Biden-Harris!")
    time.sleep(2)
    print("Please cast your vote now.")
    time.sleep(2)
    print("Thank you for using our e-voting system.")
    time.sleep(1)
    print("Hope to see you in the next year!")
else:
    time.sleep(2)
    print("Sorry. You're not eligible, please try again in the next year. Thank You.")

