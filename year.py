year=int(input("Enter year:-  "))
if(year%4==0 and year%400==0 or year%100!=0):
    print('Year is a leap year')
else:
    print('Year is not a leap year')