import cv2
import pytesseract
import re
import numpy as np
import streamlit as st
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr(file):
    img=np.frombuffer(file.read(),np.uint8)
    img=cv2.imdecode(img.cv2.INREAD_COLOR)
    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    (thresh,binary)=cv2.threshold(grey,225,255,cv2.THRESH_BINARY)
    data=pytesseract.image_to_string(binary)

def check(resume,keywords):
    text=ocr(resume)
    text=text.lower()
    l=[]
    for i in keywords:
        matches=re.findall(r'(?i)'+i,text)
        l.extend(matches)
    l=list(set(l))
    st.write(l)
    if len(l)>=3:
        return True
    else:
        return False
    
def app():
    st.title('Resume keyword check')
    resume=st.file_uploader('Upload Resume',type=['Jpeg','jpg','png'])
    keywords=st.text_input('Enter keywords')
    if st.button('Search'):
        keywords=[keyword.strip() for keyword in keywords.split(',')]
        if resume is not None:
            if check(resume,keywords):
                st.write('Resume qualified')
            else:
                st.write('The resume has no enough keywords')
        else:
            st.write('Please upload Resume') 
app()   