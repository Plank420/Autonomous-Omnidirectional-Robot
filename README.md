# Autonomous-Omnidirectional-Robot



This project contains two code files, one for the laptop and the other for the Arduino board. The project involves controlling a robot using a laptop and a camera connected to it. The robot can move forward, backward, left, and right based on the camera input.

# Objective 

Movement of goods from one point to another is integral to Logistics and Storage of goods 
within a warehouse. Individuals Such as warehouse workers are responsible for storage and 
movement of goods in such warehouses for efficient and effective safe keeping of goods and 
resources. 
The process involves use of manual labour which are responsible for transportation and 
organization of such goods and resources for storage purposes. Items need to be moved to 
and from one place to another and this can be tedious and very repetitive. Robots are well 
known for completing tasks that are repetitive in nature and hardly deviate from their original 
goal. 
Through this project it is aimed to develop a Mobile robot that can carry goods from one 
place to another with the help of concepts that involve computer vision for identification of 
goods and place them accordingly using a Manipulator Arm


The robot will be set in a workspace with a particular-coloured object to be picked up.
The robot will be placed at a certain distance from the object and in an orientation that the 
object is in the field of view of the camera that will be mounted on the Robot for Computer 
Vision purposes
The robot is then asked to mauver itself and orient itself according to the position of the 
object and allow the attached manipulator on the robot to grab said object. 
The robot will then return from where it started with the object.


The code files are as follows:

"laptop_code.py" - This file contains the code that runs on the laptop. It captures the video stream from the camera, applies some image processing techniques to detect objects, and sends commands to the Arduino board based on the object's position. The commands are sent through a serial port to the Arduino board.

"arduino_code.ino" - This file contains the code that runs on the Arduino board. It receives commands from the laptop and controls the motors of the robot based on the received commands.

# Requirements:

Python 3.x

OpenCV library

Numpy library

Imutils library

Pyserial library

Arduino board

L293D motor driver

DC motors

# Usage:

Connect the camera to the laptop and make sure it is working correctly.

Upload the "arduino_code.ino" file to the Arduino board using the Arduino IDE.

Connect the L293D motor driver to the Arduino board and the DC motors.

Connect the laptop to the Arduino board using a USB cable.

Run the "laptop_code.py" file on the laptop.

A GUI window will appear, showing the camera feed with some controls to adjust the object detection parameters.

Place an object in front of the camera and move it around.

The robot will move forward, backward, left, and right based on the object's position.

# Note: 
The object detection algorithm is hardcoded in the "laptop_code.py" file, and it may not work correctly for all objects. The algorithm may need to be modified based on the specific use case.

#Images and Media

1) Side View of the Robot

![omni](https://user-images.githubusercontent.com/70264127/224153035-572e186f-433a-4125-8030-30d23da328b7.png)










2) Top View of the Robot and Internal comoponents
![omni inside](https://user-images.githubusercontent.com/70264127/224153200-f6f587fd-a062-40fb-9ba0-e35e04d9b1af.png)



















3) Working of the Robot in controlled enviorment






https://user-images.githubusercontent.com/70264127/224153563-8ce699b3-fc61-40a7-af9b-d332ed075761.mp4




