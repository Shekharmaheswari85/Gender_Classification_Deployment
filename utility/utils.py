import pickle
import cv2 as cv

#loading model
haar=cv.CascadeClassifier('./model/haarcascade_frontalface_default.xml')
#Pickle files
mean=pickle.load(open('./model/mean_preprocess.pickle','rb'))
model_svm=pickle.load(open('./model/model_svm.pickle','rb'))
model_pca=pickle.load(open('./model/pca_50.pickle','rb'))
# print("Model loaded successfully")

#settings
gender_pre=['Male','Female']
font=cv.FONT_HERSHEY_SIMPLEX

def pipeline_model(path,filename,color='rgb'):
    # step - 1: read image in cv
    img=cv.imread(path)
    # step - 2 : convert to gray scale
    if color=='bgr':
        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    else:
        gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    # step - 3: Crop the image using haar cascade classifier
    faces=haar.detectMultiScale(gray,1.5,3)
    for x,y,w,h in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) #drawing contour or rectangle
        roi=gray[y:y+h,x:x+w] # crop image
        # step - 4: normalization (0-1)
        roi=roi/255.0
        # step - 5: resize image (100,100)
        if roi.shape[1]>100:
            roi_resize=cv.resize(roi,(100,100),cv.INTER_AREA)
        else:
            roi_resize=cv.resize(roi,(100,100),cv.INTER_CUBIC)
        # step - 6: Falttening (1x10000)
        roi_reshape=roi_resize.reshape(1,10000) #1 , -1
        # step - 7: substract with mean
        roi_mean=roi_reshape-mean
        #step - 8: get eigen image
        eigen_image=model_pca.transform(roi_mean)
        #step - 9: pass to ml Model(svm)
        results=model_svm.predict_proba(eigen_image)[0]
        #step - 10: 
        predict= results.argmax() # 0 or 1
        score=results[predict]
        #step - 11:
        text = "%s : %0.2f"%(gender_pre[predict],score)
        # print(text)
        cv.putText(img,text,(x,y),font,1,(255,255,0),2)
    cv.imwrite('./static/predict/{}'.format(filename),img)
    return text
 