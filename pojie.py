import time
import win32com.client

password=[]
with open("pass.txt","r") as dic:
  data=dic.readlines()
  for line in data:
    a=line.strip('\n')
    password.append(a)
wps=win32com.clinet.Dispatch('word.Application')
wps.Visible=1

jj=0
start_time=time.time()

for i in password:
  if i == "":
    continue
  else:
    try:
      wps.Documents.Open(r'E:\Reserch\xuexi\test.pptx',0,0,None,i)
      print(f'\rsuccess-{i}')
      break
    except:
      now_time=time.time()
      jj+=1
      dt=int(now_time-start_time)
      dt_h=dt//3600
      dt_m=(dt%3600)//60
      dt_s=dt%60
      ps=jj*100/len(password)
      st_h=st//3600
      st_m=(st%3600)//60
      st_s=st%60
      if jj %1==0:
        print(f"\r已完成{round(ps,3)}%，已花费时间{dt_h}h{dt_m}m{dt_s}s，预估剩余时间{st_h}h{st_m}m{st_s}s------{i}",end="")
      continue
      
