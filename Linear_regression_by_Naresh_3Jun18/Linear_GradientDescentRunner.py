from numpy import *
def costFunction(theta0,theta1,data):
   
    totalError=0
    for i in range(0, len(data)):
         y=data[i,1]
         x=data[i,0]
         totalError+=(y-(theta1*x+theta0))**2
    return totalError/float(len(data))
    
def gradientDescent(theta0,theta1,data,learningRate):
    derivativetheta0=0
    derivativetheta1=0
    for i in range(0,len(data)):
        y=data[i,1]
        x=data[i,0]
        derivativetheta0+=-(2*(y-(theta1*x+theta0)))/len(data)
        derivativetheta1+=-2*x*(y-(theta1*x+theta0))/len(data)
    theta0=theta0-(learningRate*derivativetheta0)
    theta1=theta1-(learningRate*derivativetheta1)
    return[theta0,theta1]

def gradientDescentConverger(theta0,theta1,data,leraningrate,iterations):
   
    for i in range(0,iterations):
     [theta0, theta1]=gradientDescent(theta0,theta1,data,leraningrate)
     print(costFunction(theta0,theta1,data),"Iterations","theta0",theta0,"theta1",theta1)
    
    return[theta0,theta1]
    
        
def run():
    data=genfromtxt("Lineardata.csv", delimiter=",")
    learningRate=0.0001
    theta0=20
    theta1=40
    iterations=5000
    costFunction(theta0,theta1,data)
    [theta0, theta1]=gradientDescentConverger(theta0,theta1,data,learningRate,iterations)
   
if __name__ == '__main__':
    run()