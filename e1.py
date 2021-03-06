import tkinter as tkr
from tkinter import *
from tkinter import filedialog
from scipy.io import loadmat
from tkinter import messagebox as mb
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

from PIL import ImageTk,Image

top = tkr.Tk()
top.geometry("800x800")
top.title('Hyperspectral Image Classifier')
a=''
options=["SVM Model","MLP Model"]

global img

#loading the dataset
def ldmatfile():
    
    f1= filedialog.askopenfile(parent=top,mode='r',title='Choose a file', filetypes =[('mat files','*.mat')])
    a=f1.name
    global df1,df
    df=loadmat(a)
    df1=df['indian_pines_corrected']
    
    df1=np.reshape(df1,(df1.shape[0]*df1.shape[1],df1.shape[2]))

    lab=tkr.Label(top,text='Dataset Loaded Successfully')
    lab.pack()
 
#loading Ground truth,reshaping and removing extra class 
def ldgtfile():
    f2= filedialog.askopenfile(parent=top,mode='r',title='choose a file',filetypes =[('mat files','*.mat')])
    a=f2.name
    global gt1,gt,gt2
    gt=loadmat(a)
    gt1=gt['indian_pines_gt']
    gt2=gt1
    gt1=np.reshape(gt1,(gt1.shape[0]*gt1.shape[1],1))
    ind=np.array([])
    global new_df,new_gt
    for i in range(21025):
        if gt1[i][0]==0:
            ind=np.append(ind,i)
    new_gt=np.delete(gt1,ind)
    new_df=np.delete(df1,ind,axis=0)
    new_gt=new_gt[:,None]

    
    lab=tkr.Label(top,text='Ground Truth Loaded Successfully')
    lab.pack()





    

#displaying ground truth    
def shwgt():
    
    
     top1=Toplevel()
     canvas = Canvas(top1, width = 500, height = 500)      
     canvas.pack()      
     img =ImageTk.PhotoImage(Image.open('300px-Indian_pines_gt.png'))      
     canvas.create_image(20,20, anchor=NW, image=img) 


     top1.mainloop()
  

    
    
    
    
    
#performs svm or mlp based on the choice made    
def ok():
     
     if variable.get()=="SVM Model":
         
         
         
         B6 = tkr.Button(top,text='Training',command=svmtraining)
         B7 = tkr.Button(top,text='Testing',command=svmtesting)
         B8 = tkr.Button(top,text='Show Accuracy',command=svmacc)
         B3 = tkr.Button(top,text='Divide into training and test datasets',command=svmdivntrn)
         B5 = tkr.Button(top,text="Perform PCA",command=svmPca)
         B3.pack(pady=20)
         B5.pack(pady=20)
         B6.pack(pady=20)
         B7.pack(pady=20)
         B8.pack(pady=20)
        
     elif variable.get()=="MLP Model":
        
        
        M7 = tkr.Button(top,text='Divide into training and test datasets',command=mlpdivntrn)
       
        M1=tkr.Button(top,text='Perform Onehotencoding and Standardisation',command=onehotenc)
        M2=tkr.Button(top,text='Perform Training',command=mlptraining)
        M3=tkr.Button(top,text='Perform Testing',command=mlptesting)
        M4=tkr.Button(top,text='Accuracy',command=mlpacc)
        M5=tkr.Button(top,text='Reseruction',command=mlpresurect)
        M6=tkr.Button(top,text='Plotting',command=mlpplot)
        M8 = tkr.Button(top,text="Perform PCA",command=mlpPca)
        M1.pack(pady=10)
        M7.pack(pady=10)
        M8.pack(pady=10)
        M2.pack(pady=10)
        M3.pack(pady=10)
        M4.pack(pady=10)
        M5.pack(pady=10)
        M6.pack(pady=10)
        
#splitting the dataset to train and test sets        
def svmdivntrn():
    
   
    global x_train,x_test,y_train,y_test
    x_train, x_test, y_train, y_test = train_test_split(new_df, new_gt, test_size=0.50, random_state=20)
    scaler = StandardScaler()
    scaler.fit(x_train)

    x_train=scaler.transform(x_train)

    x_test=scaler.transform(x_test)
    lab=tkr.Label(top,text='Dataset Successfully Split')
    lab.pack() 
      
def svmPca():   
    
    from sklearn.decomposition import PCA
    from sklearn import decomposition
    
    
    
    pca=decomposition.PCA()
    pca.n_components=100
    svmdivntrn.x_train=pca.fit_transform(x_train)
    svmdivntrn.x_test=pca.transform(x_test)
    lab=tkr.Label(top,text='PCA performed on Dataset')
    lab.pack()   
    
   

    
def svmtraining():
    
    from sklearn import svm
    global clf
    clf =svm.LinearSVC()
    clf.fit(x_train, y_train)
    lab=tkr.Label(top,text='Trained Successfully')
    lab.pack()
    
def svmtesting():
    
    prediction=clf.predict(x_test)
    lab=tkr.Label(top,text='Testing Successfull')
    lab.pack()
    
def svmacc():
  
    mb.showinfo('Accuracy', clf.score(x_test,y_test)*100)
    lab=tkr.Label(top,text='Accuracy Shown Successfully')
    lab.pack()
    
#onehotencoding on dataset before training with mlp model    
def onehotenc():
     from sklearn.preprocessing import StandardScaler
     from sklearn.preprocessing import OneHotEncoder
     global gt_onehot,dataset
     onehotencoder = OneHotEncoder() 
     y = onehotencoder.fit_transform(new_gt) 
     gt_onehot=y.toarray()

     scaler = StandardScaler()
     dataset = scaler.fit_transform(new_df)

 
     lab=tkr.Label(top,text='One hot encoding performed')
     lab.pack()
    
def mlpdivntrn():
    
   
    global x_train,x_test,y_train,y_test
    x_train, x_test, y_train, y_test = train_test_split(dataset, gt_onehot, test_size=0.15, random_state=1)
    
   
    lab=tkr.Label(top,text='Dataset Successfully Split')
    lab.pack()        
    
    
def mlpPca():   
    
    from sklearn.decomposition import PCA
    from sklearn import decomposition
    
    
    
    pca=PCA(0.5)
    
    mlpdivntrn.x_train=pca.fit_transform(x_train)
    mlpdivntrn.x_test=pca.transform(x_test)
    lab=tkr.Label(top,text='PCA performed on Dataset')
    lab.pack()
  
def mlptraining():
    global model
    model = MLPClassifier(hidden_layer_sizes=(150, 150),
                      activation='relu',
                      solver='adam',
                      alpha=0.0001,
                      batch_size='auto',
                      learning_rate='constant',
                      learning_rate_init=0.001,
                      max_iter=200,
                      shuffle=True,
                      random_state=1,
                      n_iter_no_change=50)
 

    model.fit(x_train, y_train)
    model.score(dataset,gt_onehot)
    lab=tkr.Label(top,text='Training Successfull')
    lab.pack()
    

def mlptesting():
    global predicted_onehot
    predicted_onehot=model.predict(dataset)
    lab=tkr.Label(top,text='Testing Successfull')
    lab.pack()
    
    
def mlpacc():
    global predicted
    from sklearn.metrics import accuracy_score
    print(accuracy_score(gt_onehot, predicted_onehot)*100)
    predicted = np.argmax(predicted_onehot, axis=1) 

    predicted=predicted[:,None]
    ldgtfile.new_gt=new_gt[:,None]
    
    mb.showinfo('Accuracy', accuracy_score(gt_onehot, predicted_onehot)*100)
    lab=tkr.Label(top,text=accuracy_score(gt_onehot, predicted_onehot)*100)
    lab.pack()
    


def mlpresurect():
    global predicted_reshape
    result1 = np.where(gt1!= 0)[0]
    resurret=np.zeros([df1.shape[0]])

    q=np.zeros([df1.shape[0]-dataset.shape[0],1])
    mlpacc.predicted=np.vstack((predicted,q))

    for i in range(dataset.shape[0]):
        resurret[result1[i]]=predicted[i]
    predicted_reshape=resurret.reshape(gt2.shape[0],gt2.shape[1])
    predicted_reshape=np.array(predicted_reshape)
    lab=tkr.Label(top,text='Resurection Successfull')
    lab.pack()
    


def mlpplot():
    import matplotlib
    import matplotlib.pyplot as plt
    from PIL import ImageTk,Image

    colors = 'black lime red blue magenta yellow green cyan white purple grey brown hotpink darkgreen orange aqua tan'.split()
    cmap = matplotlib.colors.ListedColormap(colors, name='colors', N=None)
    fig=plt.figure()
    plt.imshow(predicted_reshape, cmap=cmap)
    plt.show()
    top4=Toplevel()
    plt.savefig('g.png')
    canvas = Canvas(top4, width = 500, height = 500)
    canvas.pack()
    img= ImageTk.PhotoImage(Image.open('g.png'))
    canvas.create_image(20,20,anchor=NW, image=img)
    top4.mainloop()
    
    



                  
B1 = tkr.Button(top, text ="load mat file", command = ldmatfile)

B2 = tkr.Button(top,text="Load ground truth",command=ldgtfile)

B4 = tkr.Button(top,text='Show Ground Truth',command=shwgt)


#choosing between mlp or svm
variable = StringVar(top)


w = OptionMenu(top, variable, *options)



B1.pack(pady=10)
B2.pack(pady=20)
B4.pack(pady=20)



w.pack()


button = Button(top, text="OK", command=ok)
button.pack()



top.mainloop()
