from myo import init, Hub, Feed
import time
import math


def get_angle():
    global myo
    if not myo:
        print("No Myo connected after 2 seconds")
        print("Hello, Myo!")
    try:
        quat = myo.orientation
        orientation = {'x': quat.x, 'y': quat.y, 'z': quat.z, 'w': quat.w}
        #print(orientation)
        #print(myo.x_direction)
        roll = math.atan2(2.0*(quat.y*quat.z + quat.w*quat.x), quat.w*quat.w - quat.x*quat.x - quat.y*quat.y + quat.z*quat.z);
        pitch = math.asin(-2.0 * (quat.x * quat.z - quat.w * quat.y))
        yaw = math.atan2(2.0 * (quat.x * quat.y + quat.w * quat.z), quat.w * quat.w + quat.x * quat.x - quat.y * quat.y - quat.z * quat.z)
        print("Yaw:", yaw*180/3.14159265358979323846264338327950288)
              #"Pitch:", pitch*180/3.14159265358979323846264338327950288, "Roll:", roll*180/3.14159265358979323846264338327950288)
        time.sleep(0.5)
        return yaw
    finally:
      hub.shutdown()  # !! crucial



init()
feed = Feed()
hub = Hub()
hub.run(1000, feed)

myo = feed.wait_for_single_device(timeout=2.0)
