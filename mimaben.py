import subprocess
import itertools as its

def build_one(file,number,i,char,j):
  r1=its.product(number,repeat=i)
  r2=its.product(char,repeat=j)
  r1=list(r1)
  r2=list(r2)
  for ii in r1:
    for jj in r2:
      l=ii+jj
      temp=''
      for k in l:
        temp+=k
      file.write(temp+'\n')
def build_pws(file,number,i,char,j):
  for ii in range(i+1):
    for jj in range(j+1):
      build_one(file,number,ii,char,jj)

command='del pass.txt'
subprocess.call(command,shell=True)

number=['0','1','2','3','4','5','6','7','8','9']
char=['a','b','c','d']

file=open("pass.txt","a")
build_pws(file,char,0,number,6)
file.close()
print('密码本生成成功')
