import os
import shutil
from os import *

from Version import Version
def clean_add(path):
    for file1 in os.listdir(path):
        new_path=os.path.join(path,file1)
        if os.path.isfile(new_path):
            os.remove(new_path)

def create_wit(path):
    # path="C:\\Users\\user1\\Desktop\\python\\.wit"
    # path=os.path.join(path,".wit")
    if os.path.exists(path):
        raise Exception(".wit folder already exist")
    else:
        os.makedirs(path)
        ph=os.path.join(path,"allFiles")
        os.makedirs(ph)
        ph = os.path.join(path, "add")
        os.makedirs(ph)
        ph = os.path.join(path, "versions")
        os.makedirs(ph)

def add(path,file1):
    ph=path+"\\add\\"+file1
    if os.path.exists(ph):
        os.remove(ph)
    open(ph,os.O_CREAT)
    shutil.copyfile(os.path.join(path,"allFiles",file1),ph)
def commit(path,message):
    print (path)
    addToCommit(path,createCommit(path,message))
    clean_add(os.path.join(path,"add"))
def createCommit(path,message):
    ph=path+"\\versions\\"
    ver=Version(message)
    ph=os.path.join(ph,str(ver.id))
    if not os.path.exists(ph):
        os.makedirs(ph)
        f=open(os.path.join(ph,"info.txt"),os.O_CREAT|os.O_RDWR)
        # open(os.path.join(ph,"info.txt"),os.O_WRONLY)
        str1="id:%d  \n date:%s/%s/%s \n message:%s"%(int(ver.id),ver.date.day,ver.date.month, ver.date.year,str(ver.message))
        os.write(f,str1.encode())
        os.close(f)
    print (ph+" \n"+path)
    return ph
def addToCommit(path,path_commit):
    path_add=os.path.join(path,"add")
    for f in os.listdir(path_add):
        open(os.path.join(path_commit,f),os.O_CREAT)
        shutil.copyfile(os.path.join(path_add ,f),os.path.join(path_commit ,f))

def returnToCommit(path,path_folder):
    path_all_files=os.path.join(path,"allFiles")
    path_add = os.path.join(path, "add")
    for f in os.listdir(path_folder):
        ph1=os.path.join(path_all_files,f)
        ph2 = os.path.join(path_add, f)
        if os.path.exists(ph1):
            os.remove(ph1)
        if f!="info.txt":
            open(ph1, os.O_CREAT)
            shutil.copyfile(os.path.join(path_folder, f), ph1)
        if os.path.exists(ph2):
            os.remove(ph2)
            if f != "info.txt":
                open(ph2, os.O_CREAT)
                shutil.copyfile(os.path.join(path_folder, f), ph2)














