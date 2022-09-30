# A compny decided to give bouns to its employee on this diwali. A 5% bouns on salary is given to the male workers 
# and 10% bonus salary to femail workers. if the salary of the employee is less than 15000 then the employee gets 3%
# extra bonus on the salary. write a program to enter your salary and gender then calculate the bonus that has to given
# to the employee and display the salary that the employee will get.
sal=int(input('Enter your salary:'))
gender=input('Enter your Gender(M/F):')
if gender=='m' or gender=='M':
    bouns=0.05*sal
    if(sal<15000):
        bouns=bouns+0.03*sal
else:
    bouns=0.10*sal
    if(sal<15000):
        bouns=bouns+0.03*sal
sal+=bouns
print('Your diwali salery is:',sal) 