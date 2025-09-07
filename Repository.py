import os
from Files import *
class Repository:
    def __init__(self,path):
        self.path=os.path.join(path,".wit")
    def init(self):
        create_wit(self.path[:len(self.path)-5])
    def add(self, file1):
        if os.path.exists(os.path.join(self.path,"allFiles",file1)):
            add(self.path,file1)
        else:
            raise Exception( "the isn't such a file")

    def commit(self,message):
        commit(self.path,message)

    def log(self):
        print (self.path)
        path_version=os.path.join(self.path,"versions")
        li=os.listdir(path_version)
        for i in range(len(li)):
            f=os.open(os.path.join(path_version,li[i],"info.txt"),os.O_RDONLY)
            str1=os.read(f,os.path.getsize(os.path.join(path_version,li[i],"info.txt")))
            print (str1.decode())


    def status(self):
        if len(os.listdir(os.path.join(self.path,"add")))>0:
            print ("there are uncommitted changes")
        else:
            print ("there aren't any uncommitted changes")
    def checkout(self,commit_id):
        returnToCommit(self.path,os.path.join(self.path,"versions",commit_id))


