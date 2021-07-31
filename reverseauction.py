from collections import OrderedDict
dict1=dict()
dictt1=dict()
x=OrderedDict()
dict2=dict()
dictt2=dict()
y=OrderedDict()
grp=[]
need=[]
arr=[]
bid=[]
lst=[]
n,m=map(int,input().split())
for _ in range(n):
  Rtime, request,status,wk=map(str,input().split())
  dictt1[int(Rtime)]=[int(request),wk]
  if int(status)==1:
    dict1[int(Rtime)]=[int(request),int(status),wk]
for i in sorted(dict1.keys())[::-1]:
  x[i]=dict1[i]
#print('There are',len(dict1),'charging EVs which are participating in the trading.')
#print()
#print()
#print('The information for each charging EV will be in form of "Xtime:[request,status,pu]"')
#print()
#print()
#print('The charging EVs participating are:')
l=0
#for k,v in dict1.items():
  #if l%3==0:
    #print('\n')
  #print(k,v,sep=':',end=' ')
  #l+=1
print('The charging EVs with status value 1 are authorized')
print ('And they only will participate in the trading.')
print()
#print()
print('The information of charging EVs after sorting their trading time:')
h=0
for k,v in x.items():
  if l%2==0:
    print('\n')
  print(k,v,sep=':',end=' ')
  l+=1
print()
print()
for k in x.keys():
  grp.append(k)
for _ in range(m):
  Btime, capacity,iprice,lprice,status,wk=map(str,input().split())
  dictt2[int(iprice)]=[int(Btime),int(capacity),lprice,wk]
  if int(status)==1:
    dict2[int(iprice)]=[int(Btime),int(capacity),lprice,int(status),wk]
for i in sorted(dict2.keys()):
  y[i]=dict2[i]
#print('There are',len(dict2),'discharging EVs which are participating in the trading.')  
#print()
#print('The information for each discharging EV will be in form of')
#print('"fprice:[ytime,capacity,lprice,status,pu]"')
#print()
#print('The discharging EVs participating are:')
#for k,v in dict2.items():
  #if h%2==0:
    #print('\n')
  #print(k,v,sep=':',end=' ')
  #h+=1
print('The discharging EV with status value 1 are authorized')
print('And they only will participate in the trading.')
print()
print('The information of discharging EVs after sorting their initial prices:')
for k,v in y.items():
  if h%2==0:
    print('\n')
  print(k,v,sep=':',end=' ')
  h+=1
print() 
for k in y.keys():
  arr.append(k)
#print(arr)
#print(x[grp[0]][0])
#print(len(x))
i=0
ptime=2
Ttime=5
count=1
while len(x)!=0:
  while x[grp[0]][0]!=0:
    if len(arr)==0:
      break
    pay=min(arr)
    #print('arr=',arr)
    #print('keys=',y.keys())
    ptime=ptime+y[pay][0]
    Ttime=Ttime*(1.0005)+y[pay][0]
    #print(y,pay)
    bid=y[pay]
    need=x[grp[0]]
    i+=1
    #print('  ','The matched charging EV bid in', l,'th round:')
    #print('  ',grp[0],':',need)
    #print('  ','The matched discharging EV bid in', l,'th round:')
    #print('  ',pay,':',bid)
    #print()
    M=min(need[0],bid[1])
    deal=pay*M
    y[pay][1]=y[pay][1]-M
    x[grp[0]][0]=x[grp[0]][0]-M
    #print ('M',M,' ','deal',deal,' ','updated capacity',y[pay][1],' ','upadated request',x[grp[0]][0])       
    if need[0]==0:
      l+=1
    if y[pay][1]==0:
      l+=1
      arr.remove(pay)
      del y[pay]
      #print('arr before updated is:',arr)
      for i in range(len(arr)):
        r=((arr[i]-pay)/pay)
        #print(r)
        #print(arr[i]-r)
        if (arr[i]-r)!=(arr[i]):
          if (arr[i]-r) in lst:
            keyx+=1
          else:
            keyx=(arr[i]-r)
          y[keyx]=y[arr[i]]
          lst.append(int(arr[i]-r))
          del y[arr[i]]
          sorted(y.keys())
        arr[i]=arr[i]-r
       # print(arr[i])
      #print('arr after updated is:',arr)
      #print(y)
  del x[grp[0]]
  grp.remove(grp[0])
  #print(grp,x)
print()
#print('  ','All charging EVs requests are satisfied and trading is completed.')
#print('And time taken in this proposed scheme is:',ptime,'mins')
#traditional scheme time calculation.
#print()
#print('But time taken if we use traditional scheme is:',Ttime)
