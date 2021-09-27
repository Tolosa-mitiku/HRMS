from datetime import date
from PIL import Image
import math as m
'''
#number 2
dic={
    'male': 'Mr.',
    'female':'Miss.'
}
name=input('enter ur first name')
gender=input('inout ur gender')
print(dic[gender],name)

#number 3
num1=int(input('num1'))
num2=int(input('num2'))
num3=int(input('num3'))
if ((num1==num2 and num2!=num3) or (num1==num3 and num2!=num3) or (num2==num3 and num1!=num3)):
    print(num3+num2+num1)

#number 4
list=[]
n=int(input('enter number'))
while n!=0:
    list.append(n)
    n = int(input('enter number'))
ls1=[]
ls2=[]
for i in list:
    if i>50:
        ls1.append(i)
    else:
        ls2.append(i)
print(ls1)
print(ls2)


#number 5
list=[]
n=int(input('enter number'))
while n!=0:
    list.append(n)
    n = int(input('enter number'))
for i in list:
    print(i,'#'*i)

#number 6
image=Image.open('elena.jpg')
pix_val=list(image.getdata())
print(pix_val)

#number 7
m=int(input('how many numbers do u have'))
k=[]
for i in range(m):
    k.append(int(input('enter the numbers')))
minu=min(k)
p=minu
count=0
t=1
while minu>0:
    for i in range(0,len(k)):
        if k[i]%minu==0:
            count+=1
    if count==len(k):
        print('the gcd is' ,minu)
        break
    else:
        minu=minu-1
        count=0

#number 8
n1=eval((input('num1')))
n2=eval((input('num2')))
if type(n1)==float and type(n2)==float:
    print(n1+n2)

'''
#number 9
from PIL import Image
import math as m
img = Image.open("woni.jpg")

def distance(x1, y1, x2, y2):
    distance = m.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
    return distance
try:
    print('enter the x1,y1,x2,y2 coordinates where the x coordinates is in range of ',0,'-',img.size[0],'and y in range of',0,'-',img.size[1])
    x1=int(input('enter the x1 coordinate in the image '))
    y1=int(input('enter the y1 coordinate in the image'))
    x2=int(input('enter the x2 coordinate in the image'))
    y2=int(input('enter the y2 coordinate in the image'))
    if (x1 <= img.size[0] and x2 <= img.size[0]) and (y1<= img.size[1] and y2 <= img.size[1]):
        print(distance(x1, y1, x2, y2)/1.5,'meter')
    else:
        print('coordinnate value out of range!')
except Exception:
    print('invalid input')

'''
#number 10
import multiprocessing
print(multiprocessing.cpu_count())

#number 12
import os 
rows,columns=os.popen('satty size','r')
read().split()
print('width=',columns,'height=',rows)

#number 13
import time
s = time.time()
def activity():
    sum = 0
    for i in range(10000000):
        sum += 1
    print(sum)

def activity2():
    sum = 0
    for i in range(100000):
        sum += 1
    print(sum)

def start_end(a):
    a
    e=time.time()
    print('excution time in second: ',e-s)
start_end(activity2())

#number 15
import math as m
def math_detail():
    print(help(math))
    
math_detail()

#number 16
size=6
ls=[None]*(size*2)
print(ls)

def index(n):
    f = 0
    for j in n:
        f=f+ord(j)
    place=f%size
    return place
def get_value(a):
    if ls[a]==None:
        ls.pop(a)
        return True
    else:
        return False
def checker(b):
    t=1
    while get_value(b)==False:
        b=(b + t**2)
        print('e')
        if b>=12:
            b=0
            t=0

        t+=1
    return b

def search_check(m,search_index,search):
    if ls[search_index]==search:
        return search_index
    else:
        m=m
        search_index=search_index+1
        if search_index==7:
            search_index=0
        if m!=8:
            return search_check(m+1,search_index,search)
        else:
            return "didn't found any matching result"
def append():
    global m
    m = 0
    for i in range(size):
        n=input('enter the data')
        place=index(n)
        print(place)
        b=checker(place)
        ls.insert(b,n)
        print(b)
        print(ls)
    print(ls)
    search = input('what name u want to search? /enter 0 to exit')
    while search!=0:
        search=input('what name u want to search? /enter 0 to exit')
        search_index=index(search)
        s=search_check(0,search_index,search)
        print(s)
append()

#number 18 add leading zeros
str1='122.22'
print("Original String: ",str1)
n=int(input('enter number of leading zeros to add'))
for i in range(n):
    str1 = str1+'0'
print(str1)

#number 20
n=input('enter the base of the number ')
m=input('enter the base to be converted to ')
k=input('enter the number')
def hexa(sum,m):
    nList=[]
    while sum >= 1:
        rem = sum % 16
        sum = sum // 16
        nList.append(int(rem))
    nList.reverse()
    i = 0
    while i < len(nList):
        if nList[i] == 10:
            nList[i] = 'A'
        elif nList[i] == 11:
            nList[i] = 'B'
        elif nList[i] == 12:
            nList[i] = 'C'
        elif nList[i] == 13:
            nList[i] = 'D'
        elif nList[i] == 14:
            nList[i] = 'E'
        elif nList[i] == 15:
            nList[i] = 'F'
        i+=1
    return nList

def convert(sum,m):
    if int(m)<10:
        result = []
        while sum >= 1:
            re = sum % int(m)
            sum = sum // int(m)
            result.append(int(re))
        result.reverse()
        return result
    elif int(m)==16:
        return hexa(sum,m)
    elif int(m)>10 and int(m)<16:
        str='this bases are not supported for now!'
        return str
    else:
        return sum
def div(n,m,k):
    p=[]
    sum=0
    j=0
    t=0
    for i in k:
        p.append(int(i))
    p.reverse()
    for i in p:
        sum=sum+ (i*(int(n)**j))
        j+=1
    answer=convert(sum,m)
    if type(answer)==list:
        while t < len(answer):
            print(answer[t], end="")
            t += 1
    else:
        print(answer)

def multi(n,m,k):
    nList = []
    p = []
    sum = 0
    j = 0
    for i in k:
        p.append(int(i))
    p.reverse()
    for i in p:
        sum = sum + (i * (int(n) ** j))
        j += 1
    while sum >= 1:
        re = sum % int(m)
        sum = sum // 2
        nList.append(int(re))
    nList.reverse()
    i = 0
    while i < len(nList):
        print(nList[i], end="")
        i += 1

def check(n,m,k):
    l=False
    for i in k:
        if int(i) > (int(n)-1):
            l=False
            print('invalid number with this format')
            break
        else:
            l = True
    if l==True:
        if int(m) > int(n):
            div(n,m,k)
        else:
            multi(n,m,k)
check(n,m,k)

#number 21
def max_min():
    print('enter 0 to stop')
    n = int(input('enter fisrst number'))
    mini=n
    max=n
    sum=0
    count=0
    while n!=0:
        if n>max:
            max=n
        if mini>n:
            mini=n
        elif n==0:
            break
        sum=sum+n
        count+=1
        n = int(input('enter next'))
    print('the maximum is: ',max,'the  minimum is :',mini)
max_min()

#number 22
n=int(input('enter how many numbers'))
o=[]
for i in range(n):
    h=int(input('enter the number'))
    o.append(h)
o.sort()
p=True
for j in range(len(o)-1):
    if o[j]==o[j+1]:
        print('not distinict numbers')
        p=True
        break
    else:
        p=False
if p==False:
    print('this are distinict numbers')


#number 24
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]

    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]

        for p in permutation(remLst):
            l.append([m] + p)
    return l

data = list(input('enter nubers without space'))
for p in permutation(data):
    print(" ".join(x for x in p))


#number 26
n=int(input('enter the total note'))
lis=[]
lss=['-100','-50','-10','-1']
n15_f=n//100
lis.append(n15_f)
n15_r=n%100
n50_f=n15_r//50
lis.append(n50_f)
n50_r=n15_r%50
n10_f=n50_r//10
lis.append(n10_f)
n1=n50_r%10
lis.append(n1)
for i in range(len(lis)):
    if lis[i]!=0:
        print(lis[i],lss[i])
    else:
        continue

#number 28
k=[]
import math as m
def distance(x1, y1, x2, y2):
    distance = m.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
    return distance
def istriangle(k):
    r1=distance(k[0],k[1],k[2],k[3])
    r2 = distance(k[0], k[1], k[4], k[5])
    r3 = distance(k[2], k[3], k[4], k[5])
    if r1+r1>=r3 and r2+r3>=r1 and r1+r3>=r2:
        print('these are possible coordinates for triangle')
    else:
        print('not possible')

print('enter x1,y1,x2,y2,x3,y3 coordinates respectively')
for i in range(6):
    j=eval(input('enter the coorinates '))
    k.append(j)
istriangle(k)

#number 29
l=[]
def checker(l):
    r1=(l[2]-l[0])/(l[6]-l[4])
    p1=(l[3]-l[1])/(l[7]-l[5])
    if r1==int(r1) and p1==int(p1) and r1==p1:
        print('they are parallel')
    else:
        print('not')
print('enter x1,y1,x2,y2,a1,b1,a2,b2 coordinates respectively')
for i in range(8):
    n=eval(input('enter the coordinate'))
    l.append(n)
checker(l)

   
#number 31
f=1
for row in range(10):
    if row < 5:
        print('*' * (row + 1), end='')
    elif row >= 5:
        print('*' * (row - (2 * f - 1)), end='')
        f += 1
    else:
        print(' ', end='')
    print()


#number 33
import math as m
t=int(input('enter the number'))
j=0
Z=True
while j <= int(m.log(t,2)):
    if pow(2,j) == t:
        print('it is power of 2')
        z=True
        break
    else:
        z=False
    j+=1
if z==False:
    print('not')

#number  35
ls=[1,2,3,4,7,5,6,9,3,4,55]
n=int(input('enter the summation to search for'))
m=[]
for i in ls:
    for j in ls:
        for k in ls:
            if (i!=j and j!=k and k!=i) and i+j+k==n:
                m.append(tuple([i,j,k]))

print(m)


#number 37
str1=input('enter string')
str2=input('enter 2nd string')
m=0
l1=set(str1)
l2=set(str2)
if len(str1)==len(str2):
    l1=set(str1)
    l2=set(str2)
    for i in l1:
        for j in l2:
            if j==i:
                m+=1
if m == len(l1):
    print('anagomous letter')
else:
    print('not')


#number 1 part two
from PIL import Image
n=input('enter name of image with extention that is in s')
img = Image.open("images.jfif")
i=img.size[0]-1
for y in range(img.size[1]):
    for x in range(int((img.size[0]+1)/2)):
        left_color = img.getpixel((x, y))
        right_color = img.getpixel((i, y))
        img.putpixel((i, y), left_color),img.putpixel((x, y), right_color)
        i=i-1
    i=img.size[0]-1

img.show()
'''
#number 2 special
import turtle as t
def square(y):
    if y==0:
        t.fillcolor('black')
    else:
        t.fillcolor('white')
    t.begin_fill()
    for j in range(4):

        t.forward(50)
        t.right(90)
    t.end_fill()
def chess():
    x=50
    y=0
    t.penup()
    t.goto(-200,300)
    t.pendown()
    s=0
    for j in range(8):
        for i in range(8):
            if s%2==0:
                y = 0
            else:
                y=1
            square(y)
            t.forward(50)
            s += 1
        t.penup()
        t.goto(-200,300-x)
        t.pendown()
        x+=50
        s+=1
    t.done()
chess()
#number 3 special
"""
from imutils.video import VideoStream

import argparse
import datetime
import imutils
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())

if args.get("video", None) is None:
    vs = VideoStream(src=0).start()
    time.sleep(2.0)
else:
    vs = cv2.VideoCapture(args["video"])

firstFrame = None

while True:
    frame = vs.read()
    frame = frame if args.get("video", None) is None else frame[1]
    text = "unavailable"
    if frame is None:
        break

    frame = imutils.resize(frame, width=900)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if firstFrame is None:
        firstFrame = gray
        continue

    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv2.contourArea(c) < args["min_area"]:
            continue

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0, 255), 1)
        text = "Available"

    cv2.putText(frame, "Object status: {}".format(text), (10, 20),
    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
    (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 255), 1)

    cv2.imshow("Motion Detection", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

vs.stop() if args.get("video", None) is None else vs.release()
cv2.destroyAllWindows()

'''

#number 4 special
import cv2
import numpy as np
p1=input('enter the name or absolute location of the 1st image ')
p2=input('enter the name or absolute location of the 2nd image with same size as the first ')

img1=cv2.imread(p1)
img2=cv2.imread(p2)
try:
    add= img1+img2
    cv2.imshow('add',add)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except Exception:
    print('Error: the images should be of same size of pixels!!')    

'''
