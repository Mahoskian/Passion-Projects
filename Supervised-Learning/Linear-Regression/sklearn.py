"""
 Variables in order:
 CRIM     per capita crime rate by town
 ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
 INDUS    proportion of non-retail business acres per town
 CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
 NOX      nitric oxides concentration (parts per 10 million)
 RM       average number of rooms per dwelling
 AGE      proportion of owner-occupied units built prior to 1940
 DIS      weighted distances to five Boston employment centres
 RAD      index of accessibility to radial highways
 TAX      full-value property-tax rate per $10,000
 PTRATIO  pupil-teacher ratio by town
 B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
 LSTAT    % lower status of the population
 MEDV     Median value of owner-occupied homes in $1000's
"""
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

plt.rcParams["figure.figsize"] = [10, 5]
plt.rcParams["figure.autolayout"] = True
STR_X,STR_Y,STR_Z = "MEDV","LSTAT","ZN" #CHOOSE: CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,MEDV
Dimension = "3D" #CHOOSE: 2D or 3D
Boston_list = []
LinReg_DCT = {}
Slope_Int = []
CAT_LIST = ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B","LSTAT","MEDV"]

with open(r"C:\Users\soham\Documents\GitHub\Passion-Projects\Supervised-Learning\Linear-Regression\boston.txt") as fp:
    Temp_DCT = {}
    data_string = ""
    for i, line in enumerate(fp):
        if i%2==0:
            data_string+=line
        else:
            data_string+=line
            string_list = data_string.split()
            float_list = []
            for i in range(len(string_list)):
                float_list.append(float(string_list[i]))
            
            Temp_DCT["CRIM"] = float_list[0]
            Temp_DCT["ZN"] = float_list[1]
            Temp_DCT["INDUS"] = float_list[2]
            Temp_DCT["CHAS"] = float_list[3]
            Temp_DCT["NOX"] = float_list[4]
            Temp_DCT["RM"] = float_list[5]
            Temp_DCT["AGE"] = float_list[6]
            Temp_DCT["DIS"] = float_list[7]
            Temp_DCT["RAD"] = float_list[8]
            Temp_DCT["TAX"] = float_list[9]
            Temp_DCT["PTRATIO"] = float_list[10]
            Temp_DCT["B"] = float_list[11]
            Temp_DCT["LSTAT"] = float_list[12]
            Temp_DCT["MEDV"] = float_list[13]
                
            Boston_list.append(Temp_DCT)
                
            data_string=""
            Temp_DCT = {}
    fp.close()
def ARR_DCT(name):
    C_ARR = []
    for i in range(len(Boston_list)):
        C_ARR.append(Boston_list[i][name])
    return np.array(C_ARR).reshape(-1,1)
ARR_X,ARR_Y,ARR_Z,CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,MEDV = ARR_DCT(STR_X),ARR_DCT(STR_Y),ARR_DCT(STR_Z),ARR_DCT("CRIM"),ARR_DCT("ZN"),ARR_DCT("INDUS"),ARR_DCT("CHAS"),ARR_DCT("NOX"),ARR_DCT("RM"),ARR_DCT("AGE"),ARR_DCT("DIS"),ARR_DCT("RAD"),ARR_DCT("TAX"),ARR_DCT("PTRATIO"),ARR_DCT("B"),ARR_DCT("LSTAT"),ARR_DCT("MEDV")
def Lin_Reg(AuX, AuY):
    model = LinearRegression().fit(AuX,AuY)
    r_sq = model.score(AuX, AuY)
    #print('Coef of determination:', r_sq)
    #print('intercept:', model.intercept_[0])
    #print('slope:', model.coef_[0][0])
    #y_pred = model.predict(A_X)
    #print('Predicted response:', y_pred, sep='\n')
    return([r_sq, model.intercept_[0], model.coef_[0][0]])   
def min(arr):
    min = 1000.0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    min = math.floor(min)
    return min         
def max(arr):
    max = -100.0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    max = math.ceil(max)
    return max
for i in range(len(CAT_LIST)):
    TempDCT = {}
    r_list = []
    for j in range(len(CAT_LIST)):
        r_list = Lin_Reg(ARR_DCT(CAT_LIST[i]),ARR_DCT(CAT_LIST[j]))
        TempDCT[CAT_LIST[j]] = r_list
        LinReg_DCT[CAT_LIST[i]] = TempDCT
def MakeGraph(Type):
    if Type == "2D":
        fig, graph = plt.subplots()
        graph.scatter(x=ARR_X, y=ARR_Y, color='blue')
        graph.set_xlabel("X: "+STR_X, fontsize=20, rotation=0, color='red')
        graph.set_ylabel("Y: "+STR_Y, fontsize=20, rotation=90, color='red')
        graph.set(xlim=(min(ARR_X), max(ARR_X)), xticks=np.arange(min(ARR_X), max(ARR_X), (max(ARR_X)-min(ARR_X))/10), 
               ylim=(min(ARR_Y), max(ARR_Y)), yticks=np.arange(min(ARR_Y), max(ARR_Y), (max(ARR_Y)-min(ARR_Y))/10))
        
        Slope_Int = Lin_Reg(ARR_X,ARR_Y)
        x_int = np.linspace(min(ARR_X),max(ARR_X),100)
        y_int = (Slope_Int[2]*x_int)+Slope_Int[1]
        graph.plot(x_int,y_int)
        
        print("X-Y PLOT:")
        print("Coef of Determination = ", LinReg_DCT[STR_X][STR_Y][0])
        print("Y - Intercept = ", LinReg_DCT[STR_X][STR_Y][1])
        print("Slope = ", LinReg_DCT[STR_X][STR_Y][2])
    if Type == "3D":
        plt.style.use('_mpl-gallery')
        fig, graph = plt.subplots(subplot_kw={"projection": "3d"})
        graph.scatter(xs=ARR_X, ys=ARR_Y, zs=ARR_Z,s=1, color='blue')
        graph.set(xlim=(min(ARR_X), max(ARR_X)), xticks=np.arange(min(ARR_X), max(ARR_X), (max(ARR_X)-min(ARR_X))/10), 
          ylim=(min(ARR_Y), max(ARR_Y)), yticks=np.arange(min(ARR_Y), max(ARR_Y), (max(ARR_Y)-min(ARR_Y))/10),
          zlim=(min(ARR_Z), max(ARR_Z)), zticks=np.arange(min(ARR_Z), max(ARR_Z), (max(ARR_Z)-min(ARR_Z))/10))
        graph.set_xlabel("X: "+STR_X, fontsize=20, rotation=0, color='red')
        graph.set_ylabel("Y: "+STR_Y, fontsize=20, rotation=0, color='red')
        graph.set_zlabel("Z: "+STR_Z, fontsize=20, rotation=90, color='red')
        
        Slope_Int = Lin_Reg(ARR_X,ARR_Y)
        x_int = np.linspace(min(ARR_X),max(ARR_X),100)
        y_int = (Slope_Int[2]*x_int)+Slope_Int[1]
        z_int = np.linspace(0,0,100)
        graph.plot(x_int,y_int,z_int,color="red")
        print("X-Y PLOT:")
        print("Coef of Determination = ", LinReg_DCT[STR_X][STR_Y][0])
        print("Y - Intercept = ", LinReg_DCT[STR_X][STR_Y][1])
        print("Slope = ", LinReg_DCT[STR_X][STR_Y][2])
        Slope_Int = Lin_Reg(ARR_X,ARR_Z)
        x_int = np.linspace(min(ARR_X),max(ARR_X),100)
        y_int = np.linspace(0,0,100)
        z_int = (Slope_Int[2]*x_int)+Slope_Int[1]
        graph.plot(x_int,y_int,z_int,color="green")
        print("X-Z PLOT:")
        print("Coef of Determination = ", LinReg_DCT[STR_X][STR_Z][0])
        print("Y - Intercept = ", LinReg_DCT[STR_X][STR_Z][1])
        print("Slope = ", LinReg_DCT[STR_X][STR_Z][2])
        Slope_Int = Lin_Reg(ARR_Y,ARR_Z)
        x_int = np.linspace(0,0,100)
        y_int = np.linspace(min(ARR_Y),max(ARR_Y),100)
        z_int = (Slope_Int[2]*y_int)+Slope_Int[1]
        graph.plot(x_int,y_int,z_int,color="purple")
        print("Y-Z PLOT:")
        print("Coef of Determination = ", LinReg_DCT[STR_Y][STR_Z][0])
        print("Y - Intercept = ", LinReg_DCT[STR_Y][STR_Z][1])
        print("Slope = ", LinReg_DCT[STR_Y][STR_Z][2])
    plt.show()
    
#print(LinReg_DCT['MEDV'])
print(ARR_X)
MakeGraph(Dimension)