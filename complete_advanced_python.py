'''chapter-2 BASICS OF PYTHON PROGRAMMING'''

'''to display hello, world and good bye in three different lines'''
'''print("Hello")
print("World")
print("Good Bye")'''
'''print("hello", end="")
print("world", end="")
print("good bye", end="")'''
'''length=20
breadth=30
area=length*breadth
print("area of rectangle is:",area)'''
'''str1=input("Enter string 1:")
str2=input("Enter string 2:")
print("string1=",str1)
print("string2=",str2)'''
'''x=input("Please enter the number:")
print("Entered number is:",x)
print(type(x))
num1=input("please enter the number:")
print("num1=",num1)
print(type(num1))
print("converting type of num1 to int")
num1=int(num1)
print(num1)
print(type(num1))'''
'''num1=int(input("please enter the number:"))
print("num1=",num1)
print(type(num1))'''
'''length=int(input("Enter the length of the rectangle:"))
breadth=int(input("Enter the breadth of the rectangle:"))
area=length*breadth
print("length=",length)
print("breadth=",breadth)
print("Area of the rectangle is:",area)'''
'''num1=int(input("Enter integer type number:"))
num2-float(input("Enter floating type number:"))
print("number1=",num1)
print("number2=",num2)
sum=num1+num2
print("sum=",sum)'''
'''name=input("Enter the name")
age=eval(input("Enter age:"))
gender=input("Enter gender:")
height=eval(input("Enter the height:"))
print("name=",name)
print("age=",age)
print("gender=",gender)
print("height=",height)'''
'''radius=int(input("Please enter the radius of the circle:"))
print("radius=",radius)
pi=3.1428
area=pi*radius*radius
print("area of the circle is:",area)'''
'''radius=int(input("Enter the radius:"))
print("radius pf the circle=",radius)
pi=3.1428
area=pi*radius*radius
print("area of the circle is:",format(area,'.2f'))'''
'''import math
base=int(input("Enter the base of a right-angled triangle:"))
height=int(input("Enter the height of a right-angled triangle:"))
print("base=",base)
print("height=",height)
hypotenuse=math.sqrt(base*base+height*height)
print("hypotenuese=",hypotenuse)'''
'''char1-'b'
char2='B'
print("letter\tASCII Value")
print(char1,'\t',ord(char1))
print(char2,'\t',ord((char2)))
print("difference between ASCII value of two letters is:")
print(ord(char1),'-',ord(char2),'=',end="")
print(ord(char1)-ord(char2))'''


'''CHAPTER_3-OPERATORS AND EXPRESSIONS'''



'''sp=eval(input("Enter the selling price:"))
cp=eval(input("Enter the cost price:"))
print("selling price=",sp)
print("cost price=",cp)
profit=sp-cp
print("profit earned by selling=",profit)'''
'''num=eval(input("Enter the number:"))
print("Number=",num)
square=num*num
cube=num*num*num
print("square of a number=",num,'is',square)
print("cube of a number=",num,'is',cube)'''
'''p=eval(input("Enter the principle amount in RS="))
r=eval(input("Enter the rate of interest="))
t=eval(input("Enter the number of years="))
print("principle=",p)
print("rate of interest=",r)
print("number of years=",t)
SI=(p*r*t)/100
print("simple interest=",SI)'''
'''celcius=eval(input("Enter the temperature in celcius:"))
print("celcius=",celcius)
fahrenheit=(9/5)*celcius+32
print("fahrenheit=",fahrenheit)'''
'''w1=eval(input("Enter  the weight of the object in grams:"))
print("weight of the object=",w1,'grams')
w2=w1//1000
w3=w1%1000
print("weight of the object=",w2,'kg and ',w3,'g')'''
'''num=eval(input("Enter the number:"))
print("Entered number is:",num)
r1=num%10
q1=num//10
r2=q1%10
q2=q1//10
r3=q2%10
q3=q2//10
r4=q3%10
print("reverse of ",num,"is:",r1,r2,r3,r4)'''
'''print("point1")
x1=eval(input("Enter x1 coordinate:"))
y1=eval(input("Enter y1 coordinate:"))
print("point2")
x2=eval(input("Enter x2 coordinate:"))
y2=eval(input("Enter y2 coordinate:"))
l1=(x2-x1)**2+(y2-y1)**2
distance=l1**0.5
print("distance between two points is as follows")
print('(',x1,y1,')','(',x2,y2,')=',distance)'''
'''print('x \t y \t x**y')
print("10 \t 2 \t ",10**2)
print("10 \t 3 \t ",10**3)
print("10 \t 4 \t ",10**4)
print("10 \t 5 \t ",10**5)'''
'''length=eval(input("Enter the length of the rectangle:"))
breadth=eval(input("Enter the breadth of the rectangle:"))
print("---------")
print("length=",length)
print("breadth=",breadth)
print("------------")
print("area=",length*breadth)
print("perimeter=",2*(length+breadth))'''
'''p=4
q=2
z=(2+8*p)/2-((p+q)(p-q))/2+4*((p+q)/2)
print(2+8*p)/2-((p+q)(p-q))/2+4*((p+q)/2)
print("where p=",p,"and q=",q)
print("answer of above expresssion=",z)'''
'''num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print(num1,"&",num2,"=",num1&num2)'''
'''num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print(num1,"^",num2,"=",num1^num2)'''
'''n=input("Enter Number:")
s=int(input("Enter number of bits to be shift right:"))
print(n,">>",s,"=",n>>s)'''
'''n=int(input("Enter number:"))
s=int(input("Enter number of bits to be shift left"))
print(n,"<<",s,"=",n<<s)'''
'''radius=eval(input("Enter the radius of the circle:"))
print("radius=",radius)
area=3.14
radius**=2
area*=radius
print("radius of circle is =",area)'''
'''cp=float(input("Enter the cost of the product:"))
CGST=float(input("Enter tax % imposed by centre i.e. CGST:"))
SGST=float(input("Enter tax % imposed by state i.e. SGST:"))
total=0
amount_CGST=((CGST/100)*cp)
amount_SGST=((SGST/100)*cp)
total=cp+amount_CGST+amount_SGST
print("total cost of product:Rs",total)'''
'''p,q,r=eval(input("Enter three numbers:"))
print("p=",p,"q=",q,"r=",r)
print("(p>q>r) is",p>q>r)
print("(p<q<r) is",p<q<r)
print("(p<q) and (q<r) is",(p<q) and (q<r))
print("(p<q) or (q<r) is", (p<q) or (q<r))'''
'''num1=eval(input("Enter first number:"))
num2=eval(input("Enter second number:"))
if num1==num2:
    print("both the numbers entered are equal")'''
'''from math import pi
radius=eval(input("Enter radius of circle:"))
if radius>0:
    area=radius*radius*pi
    print("Area of circle is =",format(area,".2f"))
    circumference=2*pi*radius
    print("circumference of circle is =",format(circumference,".2f"))'''
'''num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num1>num2:
    print(num1,"is greater than",num2)
else:
    print(num2,"is greater than",num1)'''
'''sales=float(input("Enter total sales of the month:"))
if sales>=100000:
    basic=4000
    HRA=20*(basic/100)
    da=110*(basic/100)
    incentive=sales*(10/100)
    bonus=1000
    conveyance=500
else:
    basic=4000
    HRA=10*(basic/100)
    da=110*(basic/100)
    incentive=sales*(4/100)
    bonus=500
    conveyance=500
salary=basic+HRA+da+incentive+bonus+conveyance
print("salary of the employee")
print("basic=",basic)
print("total sales=",sales)
print("HRA=",HRA)
print("da=",da)
print("incentive=",incentive)
print("bonus=",bonus)
print("conveyance=",conveyance)
print("gross salary=",salary)'''
'''num=int(input("Enter the number:"))
print("Entered number is:",num)
if (num%5==0 and num%10==0):
    print(num,"is divisible by both 5 and 10")
if (num%5==0 or num%10==0):
    print(num,"is divisible by 5 or 10")
else:
    print(num,"is not divisible either by 5 or 10")'''
'''num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
num3=int(input("Enter the nnumber:"))
if num1>num2:
    if num2>num3:
        print(num1,"is greater than",num2,"and",num3)
else:
        print(num1,"is less than",num2,"and",num2)
print("end of nested if")'''
'''subject1=float(input("Enter the marks of data structures:"))
subject2=float(input("Enter the marks of python"))
subject3=float(input("Enter the marks of java"))
subject4=float(input("Enter the marks of c programming"))
subject5=float(input("Enter the marks of HTML"))
sum=subject1+subject2+subject3+subject4+subject5
per=sum/5
print("total marks obtained",sum,"out of 500")
print("percentage=",per)
if per>=90:
    print("distinction")
elif per>=80 and per<90:
    print("first class")
elif per>=70 and per<80:
    print("second class")
elif per>=60 and per<70:
    print("third class")
elif per>=60:
    print("pass")
else:
    print("fail")'''
'''day=int(input("Enter the day of the week:"))
if day==1:
    print("it's monday")
elif day==2:
    print("it's tuesday")
elif day==3:
    print("it's wednesday")
elif day==4:
    print("it's thursday")
elif day==5:
    print("it's friday")
elif day==6:
    print("it's saturday")
elif day==7:
    print("it's sunday")
else:
    print("sorry!! week contains only 7 days")'''
'''num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
print("1) addition")
print("2) subtraction")
print("3) multiplication")
print("4) division")
choice=int(input("please enter the choice:"))
if choice==1:
    print("addition of",num1,"and",num2,"is:",num1+num2)
elif choice==2:
    print("subtraction of",num1,"and",num2,"is:",num1-num2)
elif choice==3:
    print("multiplication of",num1,"and",num2,"is",num1*num2)
elif choice==4:
    print("division of",num1,"and",num2,"is",num1/num2)
else:
    print("sorry!!! invalid choice")'''
'''num1=int(input("Enter two numbers:"))
num2=int(input("Enter two numbers:"))
if num1<num2:
    min=num1
    print("min=",num1)
else:
    min=num2
    print("min=",num2)'''
'''num1=int(input("enter two numbers:"))
num2=int(input("enter two numbers:"))
min=print("min=",num1) if num1<num2 else print("min=",num2)'''
'''print("program will print nuber of days in a given month")
flag=1
month=int(input("enter the month for 1 to 12:"))
if month==2:
    year=int(input("Enter year:"))
    if (year%3==0) and (not(year%100==0)) or (year%400==0):
        num_days=29
    else:
        num_days=28
elif month in (1,3,5,7,8,10,12):
    num_days=31
elif month in (4,6,9,11):
    num_days=30
else:
    print("please enter valid month")
    flag=0
if flag==1:
    print("there are",num_days,"days in",month,"month")'''


'''chapter_5-LOOP CONTROL STATEMENTS'''





'''count=0
while count<=5:
    print("count=",count)
    count=count+1'''
'''count=0
sum=0
while count<=10:
    sum=sum+count
    count=count+1
print("sum of first 10 numbers=",sum)'''
'''num=int(input("please enter the number:"))
x=num
sum=0
rem=0
while num>0:
    rem=num%10
    num=num//10
    sum=sum+rem
print("sum of the digits of an entered number",x,"is =",sum)'''
'''num=int(input("please enter the number:"))
x=num
rev=0
while num>0:
    rem=num%10
    num=num//10
    rev=rev*10+rem
print("reverse of a entered number",x,"is=",rev)'''
'''count=1
sum=0
while count<=20:
    if count%5==0:
        sum=sum+count
    count=count+1
print("the sum of numbers from 1 to 20 divisible by 5 is:",sum)'''
'''num=int(input("Enter the number:"))
fact=1
ans=1
while fact<=num:
    ans=ans*fact
    fact=fact+1
print("factorial of",num,"is:",ans)'''
'''for i in range(1,6):
    print(i)
print("End of the program")'''
'''print("The capital letters A to Z are as follows:")
for i in range(65,91,1):
    print(chr(i),end="")'''
'''print("numbers from 1 to 10 in reverse order:")
for i in range(10,0,-1):
    print(i,end="")
print("\n end of program")'''
'''for i in range(1,6):
    square=i*i
    print("square of",i,"is:",square)
print("end of program")'''
'''sum=0
print("even numbers from 0 to 10 are as follows")
for i in range(0,11,1):
    if i%2==0:
        print(i)
        sum=sum+i
print("sum of even numbers from 0 to 10 is=",sum)'''
'''sum=0
print("numbers from 1 to 20 which are not divisible by 2,3,or 5")
for i in range(1,20):
    if i%2==0 or i%3==0 or i%5==0:
        print("")
    else:
        print(i)
        sum=sum+i
print("sum of even numbers from 1 to 20 is=",sum)'''
'''num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
num4=int(input("Enter the fourth number:"))
sum=num1+num2+num3+num4
print("the sum of entered 5 nummbers is =",sum)
for i in range(sum):
    if i==num1 or i==num2 or i==num3 or i==num4:
        large=i
print("largest number=",large)
print("end of proogram")'''
'''num=int(input("please enter the number:"))
triangular_num=0
for i in range(num,0,-1):
    triangular_num=triangular_num+i
print("triangular number of",num,"is =",triangular_num)'''
'''first_number=int(input("please enter first number:"))
second_number=int(input("please enter first number:"))
limit=int(input("number of fibonacci numbers to be print:"))
print(first_number,end="")
print(second_number,end="")
for i in range(limit+1):
    sum=first_number+second_number
    first_number=second_number
    second_number=sum
    print(sum,end="")'''
'''for i in range(1,4,1):
    for j in range(1,4,1):
        print("i=",i,"j=",j,"i+j=",i+j)
print("end of program")'''
'''print("Multiplication table from 1 to 5")
for i in range(1,11,1):
    for j in range(1,6,1):
        print(format(i*j,"4d"),end="")
    print()
print("end of program")'''
'''print("star pattern display")
num=7
x=num
for i in range(1,6,1):
    num=num-1
    for j in range(1,num,1):
        print("*",end="")
    x=num-1
    print()
print("end of program")'''
'''print("star pattern display")
num=1
x=num
for i in range(1,6,1):
    num=num+1
    for j in range(1,num,1):
        print("*",end="")
        x=num+1
    print()
print("end of program")'''
'''print("number pattern display")
num=1
x=num
for i in range(1,6,1):
    num=num+1
    for j in range(1,num,1):
        print(j,end="")
        x=num+1
    print()
print("end of program")'''
'''print("number pattern display")
num=1
x=num
for i in range(1,5,1):
    num=num+1
    for j in range(1,num,1):
        print(j,end="")
        x=num+1
    print()
num=5
x=num
for i in range(1,5,1):
    num=num-1
    for j in range(1,num,1):
        print(j,end="")
        x=num-1
    print()'''
'''print("the numbers from 1 to 10 are as follows:")
for i in range(1,100,1):
    if (i==11):
        break
    else:
        print(i,end="")'''
'''num=int(input("Enter the number:"))
x=num
for i in range(2,num):
    if num%i==0:
        flag=0
        break
    else:
        flag=1
if (flag==1):
    print(num,"is prime")
else:
    print(num,"is not prime")'''
'''for i in range(1,11,1):
    if i==5:
        continue
    print(i,end="")'''
'''str1=str(input("please enter the string:"))
print("entered string is:",str1)
print("after removing spaces, the string becomes:")
for i in str1:
    if i==" ":
        continue
    print(i,end="")'''
'''x=0
print("{}\t{}\t{}\t{}".format("D2","D1","T","X"))
print("----------------------")
for i in range(0,5):
    x=i
    T=(x*x)+x+41
    if(i==0):
        print("\t\t{}\t{}".format(T,i))
    elif (i>0 and i<2):
        a=((x-1)*(x-1)+(x-1)+41)
        print("\t{}\t{}\t{}".format(T-(a),T,i))
    else:
        a=((x-1)*(x-1)+(x-1)+41)
        b=((x-2)*(x-2)+(x-2)+41)
        c=(T-a)-(a-b)
        print("{}\t{}\t{}\t{}".format(c,(T-a),T,i))'''


'''CHAPTER-6-FUNCTIONS'''


      
'''def Display():
    print("Welcome to python programming")
Display()'''
'''def print_msg():
    str1=input("please enter your name:")
    print("Dear",str1,"Welcome to python programming")
print_msg()'''
'''sum=0
for i in range(1,26):
    sum=sum+i
print("sum of integers from 1 to 25 is:",sum)
sum=0
for i in range(50,76):
    sum=sum+i
print("aum of integers from 50 to 76 is:",sum)
sum=0
for i in range(90,101):
    sum=sum+i
print("sum of integers from 90 to 100 is:",sum)'''
'''def sum(x,y):
    s=0
    for i in range(x,y+1):
        s=s+i
    print("sum of integers from ",x," to ",y," is",s)
sum(1,25)
sum(50,75)
sum(90,100)'''
'''def printMax(num1,num2):
    print("num1=",num1)
    print("num2=",num2)
    if num1>num2:
        print("The number",num1,"is greater than",num2)
    elif num2>num1:
        print("The number",num2,"is greater than",num1)
    else:
        print("both numbers",num1,"and",num2,"are equal")
printMax(10,20)'''
'''def calc_factorial(num):
    fact=1
    print("entered number is:",num)
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of number",num,"is=",fact)
number=int(input("enter the number:"))
calc_factorial(number)'''
'''def display(Name,age):
    print("Name=",Name,"age=",age)
display("John",25)
display("sachin",40)'''
'''def Display(Name,age):
    print("Name=",Name,"age=",age)
Display(age=25,Name="john")'''
'''def greet(name,msg="welcome to python!!"):
    print("Hello",name,msg)
greet("sachin")'''
'''def area_circle(pi=3.14,radius=1):
    area=pi*radius*radius
    print("radius=",radius)
    print("The area of circle=",area)
area_circle()
area_circle(radius=5)'''
'''def disp_values(a,b=10,c=20):
    print("a=",a,"b=",b,"c=",c)
disp_values(15)
disp_values(50,b=30)
disp_values(c=80,a=25,b=35)'''
'''p=20
def Demo():
    q=10
    print("The value of local variable q:",q)
    print("The value of global variable p:",p)
Demo()'''
'''def Demo():
    print(S)
S="I Love Python"
Demo()'''
'''def Demo():
    S="I Love Programming"
    print(S)
S="I Love python"
Demo()
print(S)'''
'''a=20
def Display():
    a=30
    print("The value a in function:",a)
Display()
print("The value of an outside function:",a)'''
'''a=20
def Display():
    global a
    a=30
    print("The value of a in function:",a)
Display()
print("The value of an outside functtion:",a)'''
'''def minimum(a,b):
    if a<b:
        return a
    elif b<a:
        return b
    else:
        return "Both the numbers are equal"
print(minimum(100,85))'''
'''import math
def calc_Distance(x1,y1,x2,y2):
    print("x1=",x1)
    print("x2=",x2)
    print("y1=",y1)
    print("y2=",y2)
    dx=x2-x1
    dx=math.pow(dx,2)
    dy=y2-x1
    dy=math.pow(dy,2)
    z=math.pow((dx+dy),0.5)
    return z
print("Distance=",(format(calc_Distance(4,4,2,2),".2f")))'''
'''def quad_D(a,b,c):
    d=b*b-4*a*c
    print("a=",a)
    print("a=",b)
    print("a=",c)
    print("D=",d)
    if d>0:
        return "The Equation has two Real Roots"
    elif d<0:
        return "The Equation has two complex Roots"
    else:
        return "The Equation haa one real root"
print(quad_D(1,2,5))'''
'''def area_of_circle(radius):
    if radius<0:
        print("Try Again,Radius of circle cannot be negative")
        return
    else:
        print("Radius=",radius)
    return 3.1459*radius*radius
print("Area of circle=",area_of_circle(2))'''
'''def cal_abs(x):
    if x<0:
        return -x
    elif x>0:
        return x
print(cal_abs(0))'''
'''def calc_arith_op(num1,num2):
    return num1+num2, num1-num2
print(" ",calc_arith_op(10,20))'''
'''def compute(num1):
    print("number=",num1)
    return num1*num1, num1*num1*num1
square,cube=compute(4)
print("Square=",square,"Cube=",cube)'''
'''def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(5))'''
'''def fib(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
print("The value of 8th fibonacci number = ",fib(8))'''
'''def Calculate_Compound_Interest(p,n,r):
    print("StartBalance\t","\tInterest\t","Ending Balance")
    total=0
    x=r/100
    tot=0
    for i in range(1,n+1):
        z_new=p*(1+x)**i-p
        z_old=p*(1+x)**(i-1)-p
        tot=tot+(z_new-z_old)
        if (i==1):
            print("{0:.2f}\t".format(p),end="")
            print("\t{0:.2f}\t".format(z_new-z_old),end="")
            print("\t\t{0:.2f}\t".format(z_new+p))
        else:
            print("{0:2f}\t".format(p+z_old),end="")
            print("\t{0:.2f}\t".format(z_new-z_old),end="")
            print("\t\t{0:.2f}\t".format(z_new+p))
    print("Total Interest Deposited:Rs{0:.2f}".format(tot))
p=int(input("Enter the principal amounr:"))
r=int(input("Enter the rate of Interest:"))
n=int(input("Enter the number of year:"))
Calculate_Compound_Interest(p,n,r)'''





'''CHAPTER-7 STRINGS'''








'''S="India"
for ch in S:
    print(ch,end="")'''
'''S="ILOVEPYTHONPROGRAMMING"
for ch in range(0,len(S),2):
    print(S[ch],end="")'''
'''S="India"
index=0
while index<len(S):
    print(S[index],end="")
    index=index+1'''
'''word1="USA North America"
word2="USA South America"
print("word1=",word1)
print("word2=",word2)
print("The words that appear in word1 also appear in word2")
for letter in word1:
    if letter in word2:
        print(letter,end="")'''
'''TOP_10_Company="TCS,INFOSYS,GOOGLE,MICROSOFT,YAHOO"
Company=TOP_10_Company.split(",")
print(Company)
for c in Company:
    print(end="")
    print(c)'''
'''def countB(word):
    print(word)
    count=0
    for b in word:
        if (b=="b"):
            count=count+1
    return count
print("Number of 'b'=",countB("abbbabbaaa"))'''
'''def count_Letter(word,letter):
    print("Word=",word)
    print("Letter to count=",letter)
    print("Number of occurrences of '",letter,"' is=",end="")
    count=0
    for i in word:
        if (i== letter):
            count=count+1
    return count
x=count_Letter("INDIA",'I')
print(x)'''
'''def modify_Case(word):
    print("Original String=",word)
    print("After Swapping String=",end="")
    return word.swapcase()
print(modify_Case("hi Python is interesting, isn't it?"))'''
'''def getChar(word,pos):
    print("Word=",word)
    print("Character at Position",pos,"=",end="")
    counter=0
    for i in word:
        counter=counter+1
        if (counter==pos):
            return i
print(getChar("Addicted to Python",3))'''
'''def Eliminate_Letter(word,Letter):
    print("String=",word)
    print("String=",end="")
    newstr=''
    newstr=word.replace(Letter,"")
    return newstr
x=Eliminate_Letter("PYTHON PROGRAMMING",'P')
print(x)'''
'''def countVowels(word):
    print("Word=",word)
    word=word.lower()
    return {v:word.count(v) for v in 'aeiou'}
print(countVowels("I Love Python Programming"))'''
'''def UpperCaseVowels(word):
    new=''
    print("string=",word)
    print("After Capitializing Vowels")
    print("String=",end="")
    for i in word:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            new=new+i.upper()
        else:
            new=new+i
    return new
x=UpperCaseVowels("aehsdfiou")
print(x)'''
'''def removeVowels(word):
    new=''
    print("String=",word)
    print("String After Removing Vowels=",end="")
    for i in word:
        if(i!='a' and i!='e' and i!='i' and i!='o' and i!='u'):
            new=new+i
    return new
x=removeVowels("abceiodeuf")
print(x)'''
'''def isReverse(word1,word2):
    print("First word=",word1)
    print("Second word=",word2)
    if(word1==word2[::-1]):
        return True
    else:
        return False
x=isReverse("Hello",'olleH')
print(x)'''
'''def mirrorText(word1, word2):
    print("String1=",word1)
    print("String2=",word2)
    print("Mirror String=",end="")
    return word1+word2+word2+word1
x=mirrorText("PYTHON",'STRONG')
print(x)'''
'''def dec_bin(x):
    k=[]
    n=x
    while(n>0):
        a=int(float(n%2))
        k.append(a)
        n=(n-a)/2
        k.append(0)
        string=""
        for j in k[::-1]:
            string=string+str(j)
        if len(string)>4:
            print(string[1:],end="")
        elif len(string)>3:
            print(string,end="")
        elif len(string)>2:
            print("0"+string,end='')
        else:
            print("00"+string,end='')
def hex_to_bin(h):
    print("",end='')
    for ch in range(len(h)):
        ch=h[ch]
        if 'A'<=ch<='F':
            dn+10+(ord(ch)-ord('A'))
            dec_bin(dn)
        else:
            dn=(ord(ch)-ord('0'))
            dec_bin(dn)
n=input("Please Enter Hexadecimal Number:")
print("Equivalent Binary Number is as follows:")
hex_to_bin(n)'''



'''CHAPTER-8-LISTS'''





'''List1=[1,2,3,4,5]
print("Contents of List1")
print(List1)
List1=[x for x in List1 if x%2==0]
print("Even elements from the List1")
print(List1)'''
'''print("List A=",end="")
A=[x**2 for x in range(11)]
print(A)
B=[x**3 for x in range(11)]
print(B)
print("Only Even Numbers from List A=",end="")
C=[x for x in A if x%2==0]
print(C)'''
'''print("All the elements with celcius value:")
print("Celcius=",end="")
Celcius=[10,20,31.3,40,39.2]
print(Celcius)
print("Celcius to Fahrenheit Conversion")
print("Fahrenheit=",end="")
Fahrenheit=[((float(9)/5)*x+32) for x in Celcius]
print(Fahrenheit)'''
'''print("List with Mixed Elements")
L1=[1,'x',4,5.6,'z',9,'a',0,4]
print(L1)
print("List With only Integer Elements:")
L2=[e for e in L1 if type(e)==int]
print(L2)'''
'''def Print_List(Lst):
    for num in Lst:
        print(num,end=" ")
Lst=[10,20,30,40,100]
Print_List(Lst)'''
'''def Calculate_Avg(Lst):
    print("Lst=",Lst)
    print("Sum=",sum(Lst))
    avg=sum(Lst)/len(Lst)
    print("Average=",avg)
Lst=[10,20,30,40,3]
Calculate_Avg(Lst)'''
'''def Split_List(Lst,n):
    list1=Lst[:n]
    list2=Lst[n:]
    print("First List with 'n,' elements")
    print(list1)
    print("Second List with ',len(Lst)-n,' elements")
    print(list2)
Lst=[100,22,32,43,51,64]
print("List before splitting")
print(Lst)
Split_List(Lst,4)'''
'''def Reverse_List(Lst):
    print("List Before Reversing=",Lst)
    Lst.reverse()
    return Lst
Lst=[10,20,30,40,3]
print("List after Reversing=",Reverse_List(Lst))'''
'''def list_of_multiples(k):
    my_list=[]
    for i in range(1,6):
        res=k*i
        my_list.append(res)
    return my_list
print(list_of_multiples(3))'''
'''def list_of_even_numbers(start,end):
    output_list=[]
    for number in range(start,end):
        if number%2==0:
            output_list.append(number)
    return output_list
print(list_of_even_numbers(10,20))'''
'''def is_Lst_Palindrome(Lst):
    r=Lst[::-1]
    for i in range(0,(len(Lst)+1)//2):
        if r[i]!=Lst[i]:
            return False
        return True
Lst=[1,2,3,2,1]
x=is_Lst_Palindrome(Lst)
print(Lst,"(is palindrome):",x)
Lst1=[1,2,3,4]
x=is_Lst_Palindrome(Lst1)
print(Lst1,"(is palindrome):",x)'''
'''def check_duplicate(Lst):
    dup_Lst=[]
    for i in Lst:
        if i not in dup_Lst:
            dup_Lst.append(i)
        else:
            return True
    return False
Lst=[4,6,2,1,6,7,4]
print(Lst)
x=check_duplicate(Lst)
print(x)
Lst1=[1,2,3,12,4]
print(Lst1)
x=check_duplicate(Lst1)
print(x)'''
'''lst=[]
for i in range(0,4):
    x=int(input("Enter element to add to the list"))
    lst.append(x)
print("Elements of List are as follows:")
print(lst)
def maximum(lst):
    myMax=lst[0]
    for num in lst:
        if myMax<num:
            myMax=num
    return myMax
def minimum(lst):
    myMin=lst[0]
    for num in lst:
        if myMin>num:
            myMin=num
    return myMin
y=maximum(lst)
print("Maximum element  from the list=",y)
y=minimum(lst)
print("Minimum Element from the list=",y)'''
'''def Assign_grade(Lst):
    for Marks in Lst:
        if Marks>=90:
            print("student",Lst.index(Marks)+1,'Marks=',Marks,' grade A')
        elif Marks>=80 and Marks<90:
            print("Student",Lst.index(Marks)+1,'Marks=',Marks,'grade B')
        elif Marks>65 and Marks<80:
            print("Student",Lst.index(Marks)+1,'Marks=',Marks,'grade C')
        elif Marks>=40 and Marks<=65:
            print("Student",Lst.index(Marks)+1,'Marks=',Marks,'grade D')
        else:
            print("Student",Lst.index(Marks)+1,'Marks=',Marks, 'grade F')
Lst=[78,90,34,56,89]
print("Marks of 5 students=",Lst)
Assign_grade(Lst)'''
'''def check_duplicate(Lst):
    dup_Lst=[]
    for i in Lst:
        if i not in dup_Lst:
            dup_Lst.append(i)
        else:
            return True
    return False
Lst=[4,6,2,1,6,7,4]
print(Lst)
x=check_duplicate(Lst)
print(x)
Lst1=[1,2,3,12,4]
print(Lst1)
x=check_duplicate(Lst1)
print(x)'''
'''def print_reverse(Lst):
    print("List Before Reversing")
    print(Lst)
    lst=[]
    count=1
    for i in range(0,len(Lst)):
        lst.append(Lst[len(Lst)-count])
        count+=1
    lst=str(lst)
    lst="".join(lst)
    return lst
Lst=[12,23,4,5,1,9]
x=print_reverse(Lst)
print("List After Reversing")
print(x)'''
'''def list_of_odd_numbers(start,end):
    output_list=[]
    for number in range(start,end+1):
        if number%2==1:
            output_list.append(number)
            output_list.sort()
            output_list.reverse()
    return output_list
print(list_of_odd_numbers(10,20))'''
'''List1=[3,17,9,2,4,8,97,43,39]
print("List1=",List1)
lst=[]
print("Prime Numbers from the list are as follows")
for a in List1:
    prime=True
    for i in range(2,a):
        if (a%i==0):
            prime=False
            break
    if prime:
        lst.append(a)
print(lst)'''





'''CHAPTER-9-LIST PROCESSING:SEARCHING AND SORTING'''






'''def Linear_Search(My_List,key):
    for i in range(len(My_List)):
        if (My_List[i]==key):
            return i
            break
    return -1
My_List=[12,23,45,67,89]
print("Contents of List are as follows:")
print(My_List)
key=int(input("Enter the number to be searched:"))
L1=Linear_Search(My_List,key)
if(L1!=-1):
    print(key,"is found at position",L1+1)
else:
    print(key,"is not present in the list")'''
'''def Binary_Search(MyList,key):
    low=0
    high=len(MyList)-1
    while low<=high:
        mid=(low+high)//2
        if MyList[mid]==key:
            return mid
        elif key>MyList[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1
MyList=[10,20,30,34,56,78,899,90]
print(MyList)
key=eval(input("Enter the number to search:"))
x=Binary_Search(MyList,key)
if(x==-1):
    print(key,"is not present in the list")
else:
    print("The Element ",key," is found at position",x+1)'''
'''def Bubble_Sort(MyList):
    for i in range(len(MyList)-1,0,-1):
        for j in range(i):
            if MyList[j]>MyList[j+1]:
                MyList[j],MyList[j+1]=MyList[j+1],MyList[j]
MyList=[30,50,45,1,6,3,20,90,78]
Bubble_Sort(MyList)
print("Elements of List After Sorting:",end="")
print(MyList)'''
'''def Selection_Sort(MyList):
    for i in range(len(MyList)-1):
        k=i
        for j in range(i+1,len(MyList)):
            if(MyList[j]<MyList[k]):
                k=j
        if(k!=i):
            MyList[i],MyList[k]=MyList[k],MyList[i]
MyList=[12,34,2,7,45,90,89,9,1]
print("Elements before sorting")
print(MyList)
Selection_Sort(MyList)
print("Elemeents After Sorting")
print(MyList)'''
'''def insertion_Sort(MyList):
    for i in range(1,len(MyList)):
        CurrentElement=MyList[i]
        k=i-1
        while k>=0 and MyList[k]>CurrentElement:
            MyList[k+1]=MyList[k]
            k=k-1
            MyList[k+1]=CurrentElement
MyList=[12,23,5,2,21,1,4]
print("Elements before sorting")
print(MyList)
insertion_Sort(MyList)
print("Elements after sorting")
print(MyList)'''
'''def quickSort(MyList):
    print("Elements of list are as follows")
    print(MyList)
    n = len(MyList)
    Rec_Quick_Sort(MyList, 0, n - 1)

def Rec_Quick_Sort(MyList, first, last):
    if first < last:
        pos = Partition(MyList, first, last)
        Rec_Quick_Sort(MyList, first, pos - 1)
        Rec_Quick_Sort(MyList, pos + 1, last)

def Partition(MyList, first, last):
    pivot = MyList[first]
    i = first + 1
    j = last
    while True:
        while i <= j and MyList[i] <= pivot:
            i += 1
        while i <= j and MyList[j] > pivot:
            j -= 1
        if i <= j:
            MyList[i], MyList[j] = MyList[j], MyList[i]
        else:
            break
    MyList[first], MyList[j] = MyList[j], MyList[first]
    return j

MyList = [50, 30, 10, 90, 80, 20, 40, 60]
quickSort(MyList)
print("Elements of List after Sorting Using Quick Sort")
print(MyList)'''
'''def mergeSort(MyList):
    if len(MyList)>1:
        mid=len(MyList)//2
        leftList=MyList[:mid]
        rightList=MyList[mid:]
        mergeSort(leftList)
        mergeSort(rightList)
        i=0
        j=0
        k=0
        while i<len(leftList) and j<len(rightList):
            if leftList[i]<rightList[j]:
                MyList[k]=leftList[i]
                i=i+1
            else:
                MyList[k]=rightList[j]
                j=j+1
            k=k+1
        while i<len(leftList):
            MyList[k]=leftList[i]
            i=i+1
            k=k+1
        while j<len(rightList):
            MyList[k]=rightList[j]
            j=j+1
            k=k+1
MyList=[54,26,93,17,77,31,44,55,20]
print("List before sorting",MyList)
mergeSort(MyList)
print("List after Sorting",MyList,end="")'''
'''def calc(n):
    c=0
    while n>0:
        n=n//10
        c=c+1
    return c
def Bubble_Sort(MyList):
    for i in range(len(MyList) -1,0,-1):
        for j in range(i):
            if calc(MyList[j])>calc(MyList[j+1]):
                    MyList[j],MyList[j+1]=MyList[j+1],MyList[j]
MyList=[23,10,4566,344,123,121]
print("List before sorting based on length of each element:")
print(MyList)
Bubble_Sort(MyList)
print("List after sorting bassed on length of each element:")
print(MyList)'''






'''CHAPTER-10-TUPLES SETS AND DICTIONARIES'''







'''T=[(1,"AMIT"),(2,"DIVYA"),(3,"Sameer")]
for no, name in T:
    print(no,name)'''
'''L1=['Black','White','Gray']
L2=[255,0,100]
for Color,Code in zip(L1,L2):
    print((Color,Code))'''
'''def print_all(Country,Capital):
    print(Country)
    print(Capital)'''
'''X=[("APPLE",50000),("DELL",30000)]
Laptop,Prize=zip(*X)
print(Laptop)
print(Prize)'''
'''def oddTuples(aTup):
    rTup=()
    index=0
    while index<len(aTup):
        rTup+=(aTup[index],)
        index+=2
    return rTup
t=(1,3,2,4,6,5)
print(oddTuples(t))'''
'''Grades={"Tammana":"A","Pranav":"B","Sumit":"C"}
for key in Grades:
    print(key,":",str(Grades[key]))'''
'''Grades={"Tamana":"A","Pranav":"B","Summit":"C"}
for key in Grades.keys():
    print(key,'',Grades.get(key,0))'''
'''players={"Virat Kohli":{"ODI":7212,"Test":3245},
         "Sachin Tendulkar":{"ODI":18426,"Test":15921}}
for player_Name,player_Details in players.items():
    print("",player_Name)
    print("",player_Details)
for player_Name, player_Details in players.items():
    print("player:",player_Name)
    print("Run Scored in ODI :\t",player_Details["ODI"])'''
'''Players={"Virat Kohli":{"ODI":7212,"Test":3245},
         "Sachin Tendulkar":{"ODI":18426,"Test":15921}}
for Player_Name, Player_Details in Players.items():
    print(" ",Player_Name)
    for key in Player_Details:
        print(key,':',str(Player_Details[key]))'''
'''def Histogram(S):
    D=dict()
    for C in S:
        if C not in D:
            D[C]=1
        else:
            D[C]=D[C]+1
    return D
H=Histogram("AAPPLE")
print(H)'''
'''def Histogram(S):
    D=dict()
    for C in S:
        if C not in D:
            D[C]=1
        else:
            D[C]=D.get(C,0)+1
    return D
H=Histogram("AAPPLE")
print(H)'''
'''def Sq_of_numbers(n):
    d=dict()
    for i in range(1,n+1):
        if i not in d:
            d[i]=i*i
    return d
print("Squares of Number:")
Z=Sq_of_numbers(5)
print(Z)'''
'''def abc(L):
    D={}
    D["Pos"]=0
    D["Neg"]=0
    for x in L:
        if x>0:
            D["Pos"]+=1
        else:
            D["Neg"]+=1
    print(D)
L=[1,-2,-3,4]
abc(L)'''
'''def Convert_Oct_Bin(Number,Table):
    binary=''
    for digit in Number:
        binary=binary+Table[digit]
    return binary
octToBinaryTable={'0':'000','1':'001','2':'010',
                  '3':'011','4':'100','5':'101',
                  '6':'110','7':'111'}'''
'''def Eval_Poly(P,X):
    sum=0
    for Power in P:
        sum=sum+P[Power]*X**Power
    print("The Value of Polynomial after Evaluation:",sum)
P={0:-2,2:1,3:3}
Eval_Poly(P,2)'''
'''def orangecap(d):
    total={}
    for k in d.keys():
        for n in d[k].keys():
            if n in total.keys():
                total[n]=total[n]+d[k][n]
            else:
                total[n]=d[k][n]
    print("Total Run Scored by Each Player in 2 Tests:")
    print(total)
    print("Player with Highest Score")
    maxtotal=-1
    for n in total.keys():
        if total[n]>maxtotal:
            maxname=n
            maxtotal=total[n]
    return(maxname,maxtotal)
d=orangecap({"test1":{"Dhone":74,"Kohli":150}, "test2":{"Dhoni":29,"Pujara":42}})
print(d)'''






'''CHAPTER-11-FILE HANDLING'''







'''def main():
    obj1=open("WriteNumbers.txt","w")
    for x in range(1,21):
        x=str(x)
        obj1.write(x)
        obj1.write(" ")
    obj1.close()
main()'''
'''from random import randint
fp1=open("WriteNumRandom.txt","w")
for x in range(51):
    x=randint(500,1000)
    x=str(x)
    fp1.write(x+" ")
fp1.close()'''
'''fp=open("ReadDemo1.txt","r")
text=fp.read()
print(text)'''
'''fp1=open("numbers.txt","r")
num=fp1.read()
print(num)
print(type(num))'''
'''fp1=open("numbers.txt","r")
num=int(fp1.radline())
print(num)
sum=0
print("The",num,'numbers present in the file are as follows:')
for i in range(num):
    num1=int(fp1.readline())
    print(num1)
    sum=sum+num1
print("Sum of all the numbers (except first):")
print(sum)'''
'''fp1=open("Grades.txt","r")
n=int(fp1.readline())
print("Total Number of Students:",n)
for i in range(n):
    print("Student #",i+1,':',end=" ")
    allgrades=(fpl.readline().split())
    print(allgrades)
    sum=0
    for j in range(len(allgrades)):
        summ=sum+int(allgrades[j])
        per=float((sum/500)*100)
    print("Total=",sum,"\npercentage=",per)
    print("\n")'''
'''fpl=open("Grades.txt","r")
n=int(fpl.readline())
print("Total Number of Students:",n)
for i in range(n):
    print("Student #",i+1,':', end=" ")
    allgrades=(fpl.readline().split())
    print(allgrades)
    sum=0
    for j in range(len(allgrades)):
        sum=sum+int(allgrades[j])
        per=float((sum/500)*100)
    print("Total=",sum,'\npercentage=',per)
    print("\n)'''
'''def Find_Largest(fpl):
    fpl=open("Demo1.txt".'r')
    long=" "
    L=0
    count=0
    for line in fpl:
        count=count+1
        print("Line Number:",count)
        print(line)
        print("Number of Character=",len(line))
        print("----------------")
        if(len(line)>len(long)):
            long=line
            L=line
        print(L,"is the longest line with",len(long),"characters")
fp=open("Demo.txt","r")
Find_Largest(fp)'''
'''IP_File=open("Demo1.txt","r")
Out_File=open("Demo2.txt","w")
for line in IP_File:
    if line[0] not in "abcdefghijklmnopqrstuvwxyz":
        Out_File.write(line)
Out_File.close()'''
'''fp1=open("appendDemo.txt","a")
fp1.write("\nWow, Cant Believe.")
fp1.close()'''
'''fp1=open("weekdays.txt","w+")
fp1.write("Monday\n")
fp1.write("Tuesday\n")
fp1.write("Wednesday\n")
fp1.write("Thursday\n")
fp1.write("Friday\n")
fp1.seek(0)
fp1.seek(0,2)
fp1.write("Saturday\n")
fp1.write("Sunday\n")
fp1.seek(0)
t=fp1.read()
print(t)'''
fp1=open("Expenses.txt","w+")
fp1.write("Month1:100\n")
fp1.write("Month2:200\n")
fp1.write("Month3:079\n")
fp1.write("Month4:090\n")
fp1.write("Month5:098\n")
fp1.write("Month6:100\n")
print("Contents of File Expenses.txt are as follows:")
fp1.seek(0)
print(fp1.read())
fp1.seek()
text=fp1.readlines()
count=0
sum=0
for ch in txt:
    fpl.seek(7+count)
    exp=fpl.readline().strip("\n")
    sum=sum+int(exp)
    count+=12
print("Expenses of last six month:",sum)










      












         

                    
                    
                    
            
    











        





    
    

    

        
        

    
