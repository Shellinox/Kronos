count=input("")
numberlist=[]
count=int(count)
for i in range(count):
    number=input("")
    numberlist.append(number)
for i in range(count):
    evenlist=[]
    oddlist=[]
    a=numberlist[i]
    for i in range(len(a)):
        if int(a[i])%2==0:
            evenlist.append(int(a[i]))
        else:
            oddlist.append(int(a[i]))
    # print(oddlist)
    # print(evenlist)
    totaleven=0
    for i in range(0,len(evenlist)):
        totaleven=totaleven+evenlist[i]
    # print(totaleven)
    totalodd=0
    for i in range(0,len(oddlist)):
        totalodd=totalodd+oddlist[i]
    # print(totalodd)
    if(totalodd%3==0 or totaleven%4==0):
        print("Yes")
    else:
        print("No")

        