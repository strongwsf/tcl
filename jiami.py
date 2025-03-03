from skimage import io
import matplotlib.pyplot as plt

input_secret_text_path="mimi.txt"
def encode(s):
    value=""
    for c in s:
        o=ord(c)
        t=bin(o)
        t=t.replace('0b','')
        t=''.join([i for i in ['0']*(16-len(t))])+t
        value=value+t
    return value

def get_text_from_file():
    file=open(input_secret_text_path,mode='r',encoding='gbk')
    text=file.read()
    file.close()
    return text

def hide():
    img=io.imread("section.png")
    width,height,c=img.shape
    print("此图片可以隐藏：",width*height//16,"个字符")
    message=get_text_from_file()
    length=len(message)
    binlength=bin(length).replace('0b','')
    binlength=''.join(['0']*(16-len(binlength)))+binlength
    binMsg=encode(message)
    binMsg=binlength+binMsg
    total=len(binMsg)
    index=0
    for i in range(width):
        for j in range(height):
            img[i,j,0]=img[i,j,0]&254
            img[i,j,0]=img[i,j,0]+int(binMsg[index])
            index+=1
            if index >=total:
                break
        if index >=total:
            break
    fname="qqq.png"
    io.imsave(fname,img)
    print("图片已保存为"+fname)
    mod_img=io.imread(fname)

if __name__=='__main__':
    hide()
