from flask import render_template,request
import os
from PIL import Image
from utility import utils 

UPLOAD_FOLDER='static/upload'

def error():
    return render_template('error.html')

def base():
    return render_template('base.html')

def index():
    return render_template('index.html')

def faceapp():
    return render_template('faceapp.html')

def delete(path):
    filelist = [f for f in os.listdir(path) if f.endswith(".jpg")]
    for f in filelist:
        os.remove(os.path.join(path,f))

def space_free():
    delete("static/upload/")
    delete("static/predict/")

def getwidth(path):
    img=Image.open(path)
    size = img.size # width and height
    aspect = size[0]/size[1] # width/height
    w = 300 * aspect
    return int(w)

def gender():
    if request.method=='POST':
        space_free()
        f= request.files['image']
        filename=f.filename
        path=os.path.join(UPLOAD_FOLDER,filename)
        f.save(path)
        # preprocessing
        w=getwidth(path)
        # prediction (pass to pipeline model)
        text=utils.pipeline_model(path,filename,color='bgr')
        return render_template('gender.html',fileupload=True,img_name=filename,w=w,text=text)    
    return render_template('gender.html',fileupload=False,img_name="appicon.jpeg",w=300,text=None)


