abc=[1,44,'kitab',25,"qelem"]
for i in abc:
  print(i)
a="Lale"
for i in a:
    print(i)
    
task2=[11,22,33,44,55]
for i in range(len(task2)):
    print(task2[i])
    
number=[1,3,5,7,10,12,14]
total=0
for num in number:
    if num %2==0:
        total+=num
    elif num %3==0:
        total -=num
    else:
        total+=1
print(total)#??

t=(1,2,3,4,5)
for x in t:
    if x %2==0:
        t=t+(x,)
print(len(t))
    
task2=["112","22","33","44"",55"]
newtask=[]
for i in task2:
    if "2" in i:
        newtask.append(i)
print(newtask)

task2=[1,2,3,4,5,6,7,8,9]
task3=[]
for x in task2:
    if x<5:
        task3.append(x)
print(task3)

i=1
while i<10:
    if i in range(2,11,3):
     break
    i+=2
    print(i)#3,5
     
i=1
while i<10:
    if i in range(1,11,3):
        i+=2
        continue
    print(i)
    i=i+2#3,5,9
    
i=1
while i<10:
    if i in range(1,11,3):
        i+=1
        continue
    print(i)
    i=i+2#2,5,8
    
i=1
while i<10:
    if i in range(10,0,-1):
        print(i)
        i=i+3#1,4,7
        
i=1
while i<10:
    if i in range(1,11,3):
        print(i)
    i=i+2#1,7

task3=["alma","armud","heyva"]
i=0
while i < len(task3):
    print("i=",i,task3[i])
    i=i+1
    
i=1
while i<10:
    if i in range(2,11,3):
     break
    print(i)
    i=i+2  #1,3
    