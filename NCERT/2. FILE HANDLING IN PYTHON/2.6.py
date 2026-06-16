#2.6
import pickle
listvalues=[1,"Geetika",'F',26]
fileobject=open("mybinary.dat","wb")
pickle.dump(listvalues,fileobject)
fileobject.close()