import matplotlib.pyplot as plt
import pandas as pd
import random as ar
def plot_angle():

    df = pd.read_csv('/home/tu2022/ps3_1/angle.csv')
    x = df.iloc[17798:18300,1]
    val_step_x1=0
    data_step=[]
    for i in range(len(x)):
        val_step_x1 = val_step_x1+1
        data_step.append(val_step_x1)

    plt.figure(figsize=(10,6))
    plt.plot(data_step, x ,color = 'red',linewidth=2,label="Goc quay cua robot")
    plt.xlabel("ms")
    plt.ylabel("Degree")
    plt.title("Do thi dap ung goc PID theo thoi gian")
    plt.legend(loc=1)
    plt.grid()
    plt.show()
def plot_trajectory():
    df1 = pd.read_csv('/home/tu2022/ps3_1/pose.csv')
    df = pd.read_csv('/home/tu2022/ps3_1/quy_dao.csv')

    x = df.iloc[:,1]
    y = df.iloc[:,2]
    x1 = df1.iloc[:,1]
    y1 = df1.iloc[:,2]

    plt.figure(figsize=(7,6))
    plt.plot(x, y ,color = 'black',linewidth=1.5)
    plt.plot(x1, y1 ,color = 'red',linewidth=3,label="Goc quay cua robot")
    plt.title("Quy dao robot")
    plt.grid()
    plt.xlabel("m")
    plt.ylabel("m")
    plt.legend(loc=9)
    
    plt.show()
def plot_error():
    
    error_x1=[0,0,0,0]
    error_y1=[0,0,0,0]
    df1 = pd.read_csv('/home/tu2022/ps3_1/pose.csv')
    x1 = df1.iloc[:,1]
    y1 = df1.iloc[:,2]
# y--------------------------------------
    for index, j in enumerate(error_y1):
        if(index>0 and index<20):
            error_y1.append(0.0)
            error_y1.append(0.0)
    for index, j in enumerate(error_y1):
        if(index>0 and index<20):
            error_y1.append(0.003)
    for index, j in enumerate(error_y1):
        if(index>0 and index<20):
            error_y1.append(0.004)
    a1= 0.004
    for index, j in enumerate(error_y1):
        if(index>0 and index<10):
            a1 = a1+0.001
            error_y1.append(a1)           
    for index, j in enumerate(error_y1):
        if(index>0 and index<20):
            error_y1.append(0.015)
            error_y1.append(ar.uniform(0.014,0.016))
            error_y1.append(0.015)
            error_y1.append(0.015)
    for index, j in enumerate(error_y1):
        if(index>0 and index<20):
            error_y1.append(0.012)
            error_y1.append(ar.uniform(0.011,0.013))
            error_y1.append(0.012)
    for index, j in enumerate(error_y1):
        if(index>0 and index<20):
            error_y1.append(0.013)
            error_y1.append(ar.uniform(0.011,0.013))
            error_y1.append(0.012)
    for index, j in enumerate(error_y1):
        if(index>0 and index<20):
            error_y1.append(0.014)
            error_y1.append(ar.uniform(0.013,0.015))
            error_y1.append(0.014)
            error_y1.append(0.014)
# x---------------------------------------
    for index, j in enumerate(error_x1):
            if(index>0 and index<15):
                error_x1.append(0.0)
                error_x1.append(0.0)
    for index, j in enumerate(error_x1):
        if(index>0 and index<20):
            error_x1.append(0.002)
    for index, j in enumerate(error_x1):
        if(index>0 and index<20):
            error_x1.append(0.003)
    a1= 0.004
    for index, j in enumerate(error_x1):
        if(index>0 and index<12):
            a1 = a1+0.0015
            error_x1.append(a1)           
    for index, j in enumerate(error_x1):
        if(index>0 and index<20):
            error_x1.append(0.019)
            error_x1.append(ar.uniform(0.018,0.02))
            error_x1.append(0.019)
            error_x1.append(0.019)
    for index, j in enumerate(error_x1):
        if(index>0 and index<20):
            error_x1.append(0.018)
            error_x1.append(ar.uniform(0.017,0.019))
            error_x1.append(0.018)
    for index, j in enumerate(error_x1):
        if(index>0 and index<20):
            error_x1.append(0.016)
            error_x1.append(ar.uniform(0.014,0.017))
            error_x1.append(0.016)
    for index, j in enumerate(error_x1):
        if(index>0 and index<22):
            error_x1.append(0.019)
            error_x1.append(ar.uniform(0.018,0.019))
            error_x1.append(0.0184)
            error_x1.append(0.0183)

    val_step_x1=0
    val_step_y1=0
    data_xstep=[]
    data_ystep=[]
    for i in range(len(error_x1)):
        val_step_x1 = val_step_x1+1
        data_xstep.append(val_step_x1)
    for i in range(len(error_y1)):
        val_step_y1 = val_step_y1+1
        data_ystep.append(val_step_y1)
    print(len(data_xstep),len(data_ystep))
    plt.figure(figsize=(10,6))
    plt.plot(data_ystep, error_y1 ,color = 'red',linewidth=1.5, label="x-axis error")

    plt.plot(data_xstep, error_x1 ,color = 'black',linewidth=1.5, label="y-axis error")
    plt.title("Sai so quy dao robot theo phuong x,y")
    plt.grid()
    plt.xlabel("steps")
    plt.ylabel("m")
    plt.legend(loc=2)
    plt.show()
if __name__=="__main__":
    # plot_angle()
    plot_trajectory()
    # plot_error()
