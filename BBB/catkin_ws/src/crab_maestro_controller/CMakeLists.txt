cmake_minimum_required(VERSION 2.8.3)
project(crab_maestro_controller)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)


###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES maestro_controller
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_library(polstro src/PolstroSerialInterface.cpp src/PolstroSerialInterfacePOSIX.cpp)
target_link_libraries(polstro ${catkin_LIBRARIES})

# add_executable(maestro_joint_sub src/maestro_joint_sub.cpp)
# target_link_libraries(maestro_joint_sub polstro ${catkin_LIBRARIES})
# 
# add_executable(maestro_leg_sub src/maestro_leg_sub.cpp)
# target_link_libraries(maestro_leg_sub polstro ${catkin_LIBRARIES})

add_executable(controller_sub src/controller_sub.cpp)
target_link_libraries(controller_sub polstro ${catkin_LIBRARIES})


