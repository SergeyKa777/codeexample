import os
import sys
import uuid
from PIL import Image, ImageEnhance, ImageFilter
import difflib
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #Путь до модуля Tesseract
os.chdir(r"e:\\xx\\") ## Путь до папки где лежат скрины !!!
lister = os.listdir(os.getcwd())
print(lister)
i = 0
for kk in lister:
    i += 1
    os.rename(kk, str(i) + str(uuid.uuid4().hex) + ".jpg")
lister = os.listdir(os.getcwd())
i=0
for kk in lister:
    i += 1
    os.rename(kk, str(i) + ".jpg")
def sortByLength(inputStr):
    return len(inputStr)
lister = os.listdir(os.getcwd())
lister=sorted(lister,key=sortByLength)
textdiff=[]
i=0
count=len(lister)
for kk in lister:
    img=Image.open(os.getcwd()+ "\\" + str(lister[i]))
    textdiff.insert(i, pytesseract.image_to_string(img, lang='rus+eng'))
    print(textdiff[i])
    i += 1
    count -= 1
    print(">>>>"+str(count)+"<<<<")
i=0
count=len(lister)
for gg in textdiff:
    aa=gg
    ii=0
    for pp in textdiff:
        bb=pp
        seq = difflib.SequenceMatcher(a=aa, b=bb)
        if seq.ratio()>0.6: #Коэффициент соответствия экземпляров ! 1=100% 0.5=50%
            print("Дубликат" + str(ii+1))
        ii+=1
    print("------------------------")
    i+=1
    count -= 1
    print("> " + str(count) + " <")
