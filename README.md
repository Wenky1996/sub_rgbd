##   ros package to get depth and rgb image using python 

[ how to build it] 

* mkdir -p d435iRgbd_ws/src
* cd d435iRgbd_ws/src
* git clone https://github.com/Wenky1996/sub_rgbd.git
*  cd  ..
*  catkin_make

[ how to run it]
*  roslaunch realsense2_camera rs_rgbd.launch
* source devel/setup.zsh or setup.bash
*  rosrun sub_rgbd sub_rgbd.py 
 **   
 
