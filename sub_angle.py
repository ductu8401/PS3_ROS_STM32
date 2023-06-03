#!/usr/bin/env python3
# import roslib; roslib.load_manifest('Phoebe')
import rospy
import csv  
import pandas as pd
from std_msgs.msg import Int16

data1=[]
a1=0
def angle_sub(msg):
    global a1
    a = msg.data/100
    rospy.loginfo("Angle current: {}".format(a))
    a1 = a/10-a1
    data1.append(a)
    data_angle = {
        "x": data1
    }
    df = pd.DataFrame(data_angle)
    # print("sub: ",df)
    df.to_csv("angle.csv")
    a1=a
    
if __name__ == "__main__":
    rospy.init_node('angle_sub', anonymous=True) #make node 
    rospy.Subscriber('/angle', Int16,angle_sub)
    
    rospy.spin()
