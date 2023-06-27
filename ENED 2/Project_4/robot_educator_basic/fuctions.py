# check gyro sensor angle
gyrovalue=(gyro_sensor.angle())
robot.turn(190)
nextRead = gyro_sensor.angle()
if (gyrovalue + 5 >= nextRead - 180 >= gyrovalue - 5):
    robot.drive(steering, -overshoot)
elif (gyrovalue + 5 < nextRead - 180):
    robot.drive(steering, overshoot)
else:
    robot.drive(steering, overshoot)