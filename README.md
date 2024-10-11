# `far_c1f_tavolsagmero` package
z a ROS2 csomag két node-ot tartalmaz, amelyek egymással együttműködve figyelik egy távolságadat forrását. A rendszer célja egy szimulált szenzor által generált távolságadatok valós idejű monitorozása, és annak jelzése, ha a távolság elér egy kritikus határértéket.  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)
## Packages and build

It is assumed that the workspace is `~/ros2_ws/`.

### Clone the packages
``` r
cd ~/ros2_ws/src
```
``` r
git clone https://github.com/Wolreg/far_c1f_tavolsagmero
```

### Build ROS 2 packages
``` r
cd ~/ros2_ws
```
``` r
colcon build --packages-select far_c1f_tavolsagmero
```

<details>
<summary> Don't forget to source before ROS commands.</summary>

``` bash
source ~/ros2_ws/install/setup.bash
```
</details>

``` r
ros2 launch far_c1f_tavolsagmero tavolsagmero.launch.py
```

