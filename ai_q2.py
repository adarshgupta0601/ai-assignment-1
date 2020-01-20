print("Is every human a good grader")

#creating a truth table

x=[1,1,0,0]
y=[1,0,1,0]
z=[]
j=0
for i in x:
    if i==1:
        i=0
        z.append(i and y[j])
    elif i==0:
        i=1
        z.append(i and y[j])
    j+=1
    for i in z:
        if i==0:
            print("no")
            break
        elif i==1:
            pass
