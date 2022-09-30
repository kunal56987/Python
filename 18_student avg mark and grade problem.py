# wap to enter the mark of a student in 6 subject then calculate the total mark,avg. mark and grade 
# avg>=90            ------------> O grade 
# avg>80 and avg<=89 ------------> E grade 
# avg>70 and avg<=79 ------------> A grade 
# avg>60 and avg<=69 ------------> B grade 
# avg>50 and avg<=59 ------------> C grade 
# avg>40 and avg<=49 ------------> D grade 
# other wise fail - Better luck next time

eng=int(input('Enter your marks in English:'))
hin=int(input('Enter your marks in Hindi:'))
math=int(input('Enter your marks in maths:'))
sci=int(input('Enter your marks in science:'))
s_sci=int(input('Enter your marks in social science:'))
it=int(input('Enter your marks in Coumputer:'))
total_mark=eng+hin+math+sci+s_sci+it
print('Total marks:',total_mark)
avg_mark=total_mark/6
print('Avrage mark:',avg_mark)
if avg_mark>=90:
    print('Congratulation you got O Grade')
elif avg_mark>80 and avg_mark<=89:
    print('Congratulation you got E Grade')
elif avg_mark>70 and avg_mark<=79:
    print('Congratulation you got A Grade')
elif avg_mark>60 and avg_mark<=69:
    print('Congratulation you got B Grade')
elif avg_mark>50 and avg_mark<=59:
    print('Congratulation you got C Grade')
elif avg_mark>40 and avg_mark<=49:
    print('Congratulation you got D Grade')
else:
    print('FAIL! "BETTER LUCK NEXT TIME"')