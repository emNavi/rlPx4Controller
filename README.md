# rlPx4Controller

rlPx4Controller is a quadcopter control library implemented in C++ and provides a python interface through pybind11. ***The motivation of this work is to build a parallel flight control for large-scale quadrotor reinforcement learning (RL) and Sim-to-Real on the PX4 stack.*** Thus, the implementation of the controller is consistent with the Px4 flight control to ensure the consistency of sim2real.

## Features
rlPx4Controller is developed for DRL simulation flight control. The attributes include:
- CPU-based parallel flight geometric control computation.
- Strict **PX4-like** flight controller with differential flatness.
- Parallel control for different levels that supports: position & yaw control (**PY**), velocity & yaw control (**LV**), collective thrust & attitude angle (**CTA**), collective thrust & body rate (**CTBR**)

4 modules have been implemented so far:

- PolyTrajGen: Fifth degree polynomial trajectory generation
- Lemniscate:  Figure-eight curve generation
- pyControl: Single aircraft controller
- pyParallelControl：Multi-aircraft controller for reinforcement learning in vectorized environments.

For usage and more details, please refer to the [documentation](https://rlpx4controller.readthedocs.io/).


## Installation 
This project was tested on Ubuntu 2004. Generally, you can successfully install it by executing the following command
```bash
sudo apt install libeigen3-dev
```
Its function is to install `Eigen==3.3.7` to expose the python interface.

If you are using Ubuntu 2204, executing the above command usually cannot install the specified version of Eigen, but it can still be used. If you use the conda environment, you only need to execute the following command:
```bash
conda install -c conda-forge eigen==3.3.7
```
It can be installed and used normally

Then execute:

```bash
pip install -e .
bash stubgen.sh
```