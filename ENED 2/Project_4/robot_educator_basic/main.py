#!/usr/bin/env python3
# This is the main program for the El Liftbot for ENED project 4.
# 
# Imports the necessary libraries.
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Direction, Button
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import ImageFile
#
# Initialize the EV3 brick.
ev3 = EV3Brick()
#
# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
#
# The wheel diameter of the Tank Bot is about 54 mm.
WHEEL_DIAMETER = 54
#
# The axle track is the distance between the centers of each of the
# wheels.  This is about 200 mm for the Tank Bot.
AXLE_TRACK = 200
#
# The Driving Base is comprised of 2 motors 6 gears and 2 treads.
robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)
#
gyro_sensor = GyroSensor(Port.S4)
#
# Initialize the steering and overshoot variables.
steering = 60
overshoot = 5
#
# This gyro sensor is mounted on the robot so that it is correct any veering to the left or right, as the robot moves forward, 
# kepting the robot on the straight and narrow.
def veeringcorrection ():
    if gyro_sensor.angle() > 0:
        robot.drive(steering, -overshoot)
    elif gyro_sensor.angle() < 0:
        robot.drive(steering, overshoot)
    else:
        robot.drive(steering, 0)
#
#
T1 = input("Is this the First test? (y/n): ")
if T1 == "y":
    Firsttest = True
else:
    Firsttest = False
if Firsttest == True:
# first move
    y = input("Enter the number of feet the robot will travel: ")
    y = y*500
    Lap1 = y*(.5)
    robot.straight(Lap1)
# second move
    robot.straight(-y)
# third move
    Lap2 =y*(1.5)
    robot.straight(Lap2)
# fourth move






x = 0
y = 0
# is this the second test?
T2 = input("Is this the Second test? (y/n): ")
if T2 == "y":
    SecondTest = True
else:
    SecondTest = False
# first move
if SecondTest == True:
y = input("Enter the number of feet the robot will travel: ")
y = y*500
x = input("Please enter the angle in degrees: ")
    robot.straight(y)
    robot.turn(x)
# second move
    robot.straight(y)
    robot.turn(x)
# third move
    robot.straight(y)
    robot.turn(x)
# fourth move
    robot.straight(y)
    SecondTest = False
# End of subtask 1
