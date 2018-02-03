from myo import init, Hub, Feed
import time
import math

init()
feed = Feed()
hub = Hub()
hub.run(1000, feed)

try:
  myo = feed.wait_for_single_device(timeout=2.0)
  if not myo:
    print("No Myo connected after 2 seconds")
  print("Hello, Myo!")
  while hub.running and myo.connected:
    quat = myo.orientation
    orientation = {'x': quat.x, 'y': quat.y, 'z': quat.z, 'w': quat.w}
    print(orientation)
    print(myo.x_direction)
    roll = math.atan2(2.0*(quat.y*quat.z + quat.w*quat.x), quat.w*quat.w - quat.x*quat.x - quat.y*quat.y + quat.z*quat.z);
    pitch = math.asin(-2.0 * (quat.x * quat.z - quat.w * quat.y))
    yaw = math.atan2(2.0 * (quat.x * quat.y + quat.w * quat.z), quat.w * quat.w + quat.x * quat.x - quat.y * quat.y - quat.z * quat.z)
    print("Yaw:", yaw*180/3.141592654, "Pitch:", pitch*180/3.141592654, "Roll:", roll*180/3.141592654)
    time.sleep(0.5)
finally:
  hub.shutdown()  # !! crucial