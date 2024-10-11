find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)

install(PROGRAMS
  scripts/distance_publisher.py
  scripts/distance_monitor.py
  DESTINATION lib/${far_c1f_tavolsagmero}
)

ament_package()
