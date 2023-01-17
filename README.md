# JPL Autonomous Code and Setup
<b> If there are problems with depth, recalibrate zed stereo camera </b>

## Setup
```sh
roslaunch zed_wrapper zedm.launch
rosrun dynamic_reconfigure dynparam set /zedm/zed_node depth_confidence 99
rosrun dynamic_reconfigure dynparam set /zedm/zed_node depth_texture_conf 90
rosrun dynamic_reconfigure dynparam set /zedm/zed_node depth_confidence 100
roslaunch zed_rtabmap_example zed_rtabmap.launch camera_model:=zedm
```
