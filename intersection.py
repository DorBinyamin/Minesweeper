"""
Student: dor binyamin
ID: 209460302
Assignment no. 6
Program:intersection.py
"""
import random
from math import *

def difference(f,g):#Returns the difference between functions
       h=lambda x:f(x)-g(x)
       return h
  
       
       
def diff(f):#returns the numeric derivative of f
    h=0.000001
    return(lambda x:(f(x+h)-f(x))/h)

def NR(f,a,b,eps,n):
#Applies the Newton Rapson method to find a zero point of Function. 
    count=1 
    x=random.uniform(a,b)
    while(abs(diff(f)(x))<eps or x<0):#run until (positiv (diff(f)(x)))>epsilon and x positive
        x=random.uniform(a,b)
    while(count<=n):#run antil count>n
        count+=1
        x=x-(f(x)/diff(f)(x))
        if abs(f(x))<eps :
            return "%.4f"%x
        if n==count:
           return None
    
    
def main():
#The program prints into a file txt.functions_output the two functions, the values of a and b 
#and the intersection point (x,y) in the range of x between a and b if there is no intersection point 
#Cutting the program prints to a file no intersection
        file=open("input_functions.txt")
        filew=open("output_function.txt","w")
        f=file.read()
        file.close()
        func=f.split()
        for j in range(0,len(func),4):
            f1=lambda x:eval(func[j])
            f2=lambda x:eval(func[j+1])
            a=float(func[j+2])
            b=float(func[j+3])
            filew.write(func[j]+"\n"+func[j+1]+"\n"+func[j+2]+" "+func[j+3]+"\n")
            dif=difference(f1, f2)
            try:
                x=NR(dif,a,b,10**(-10),100)
                y="%.4f" %f1(float(x))
                filew.write(f"intersection: ({x}, {y}) \n\n")
            except Exception :
                filew.write("no intersection"+"\n\n")
                continue
if __name__=="__main__":
    main()
        
        
        
    