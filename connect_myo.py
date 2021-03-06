# Connect_myo.py
# Purpose: This file provides the functionality to interact with the Myo and calculate the direction that the user is
# pointing in. Includes various testing bits. As of 8:11pm Feb. 3, there are two functions


# Import the needed items from Myo
import myo as libmyo


# Advanced mathematical calculations required for quaternion vectors
import math

class MyFeed(libmyo.Feed):

    def __init__(self):
        super(MyFeed, self).__init__()
        self.orientation = None
        self.pose = libmyo.Pose.rest
        self.locked = False

    def on_pose(self,myo,timestamp,pose):
        self.pose = pose
        self.handler(pose=pose)

    def on_orientation_data(self,myo,timestamp,orientation):
        self.orientation = orientation
        self.handler(orientation=orientation)

    def handler(self,pose=None,orientation=None):
        global is_fist, is_in
        is_fist = is_in = False
        if pose == libmyo.Pose.fist:
            is_fist = True
        elif pose == libmyo.Pose.wave_in:
            is_in = True


def calculate_yaw_from_myo():
    # Purpose: returns the measurement of yaw from myo. This measurement is used as the direction of movement of
    # the player in movement.py

    # Why do we need a global variable?
    global myo, sonarActivated, feed

    # if not myo:
    #     # When no Myo connects, say so
    #     print("No Myo connected after 2 seconds")

    # Get the quaternion vectors from the connected Myo
    quat = myo.orientation

    # Testing
    # print(orientation)
    # print(myo.x_direction)
    # orientation = {'x': quat.x, 'y': quat.y, 'z': quat.z, 'w': quat.w}

    # Other irrelevant info
    # After careful physical testing, it was determined that yaw is what determines the direction
    # roll = math.atan2(2.0*(quat.y*quat.z + quat.w*quat.x), quat.w*quat.w - quat.x*quat.x - quat.y*quat.y + quat.z*quat.z);
    # pitch = math.asin(-2.0 * (quat.x * quat.z - quat.w * quat.y))


    # Calculate the yaw, and print to console
    yaw = math.atan2(2.0 * (quat.x * quat.y + quat.w * quat.z), quat.w * quat.w + quat.x * quat.x - quat.y * quat.y - quat.z * quat.z)

    # Testing for printing the other irrelevant information
    # "Pitch:", pitch*180/3.14159265358979323846264338327950288, "Roll:", roll*180/3.14159265358979323846264338327950288)

    # look for double tap
    #if feed.on_event(kind=myo.pose, event=myo.Pose.fist):
        #sonarActivated = True

    # if feed.on_pose(myo, 0, myo._pose.fist):
    #     sonarActivated = True
    #     print("beep in connect")
    # else:
    #     sonarActivated = False

    # Pass the value of yaw to the caller
    return yaw


def close_connection_to_myo():
    # Purpose: closes the connection to the Myo. From the documentation: "Free all resources associated with this Hub.
    # Will disconnect all connected Myo devices. After shutting down, init must be called before using the Hub again."
    hub.shutdown()  # !! crucial.


libmyo.init()
feed = MyFeed()
hub = libmyo.Hub()
hub.set_locking_policy(libmyo.LockingPolicy.none)
hub.run(1000, feed)
# print("Hello, Myo!")
myo = feed.wait_for_single_device(timeout=5.0)
if myo is None:
    print("Myo is not connected")
    exit()

sonarActivated = False

# some global variables
is_fist = False
is_in = False

calculate_yaw_from_myo()