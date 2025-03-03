from skimage import io
import re

def decode(s):
  l=re.findall(r'.{16}',s)
  s=''
  for i in l:
    s=s+chr(int(i,2))
  return s

def display():
  path="qqq.png"
  img=io.imread(path)
  width,height,c=img.shape
  num=''
  index=0
  for i in range(width):
    for j in range(height):
      num=num+str(img[i,j,0]&1)
      index+=1
      if index ==16:
        break
    if index ==16:
      break
    num=int(num,2)+1
    total=num*16
    binMsg=''
    index=0
    for i in range(width):
      for j in range(height):
        binMsg=binMsg+str(img[i,j,0]&1)
        index+=1
        if index>total:
          break
      if index>total:
        break
    message=decode(binMsg[16:])
    print(message)
    
if __name__='__main__':
  display()
