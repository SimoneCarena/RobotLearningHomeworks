#! /usr/bin/env python3

import rospy
import numpy as np

from single_pendulum_ros.msg import StateData
from single_pendulum_ros.msg import OutputData

def callback(real_data):

    # Noise the measurements
    measurement_noise_var = 0.05 # Actual measurement noise variance
    x = np.array([real_data.x1, real_data.x2]).T
    z = x + np.sqrt(measurement_noise_var)*np.random.randn()

    # Send noisy measurements
    sensor_data = OutputData()
    sensor_data.y = z[0]

    pub.publish(sensor_data)


def sensor():

    # Subscriber Init
    rospy.init_node('sensor', anonymous=False)
    rospy.Subscriber('real_data',StateData,callback)

    rospy.spin()


if __name__ == '__main__':
    try:
        # Publisher Init
        pub = rospy.Publisher('sensor_data',OutputData,queue_size=1)
        sensor()
    except rospy.ROSInterruptException:
        pass