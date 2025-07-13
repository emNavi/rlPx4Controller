# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup,find_packages
import subprocess
import os
__version__ = "0.0.2"

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

# Dynamic detection of the path of Eigen3
def get_eigen_include():
    conda_prefix = os.environ.get('CONDA_PREFIX')
    if conda_prefix:
        # Use Conda
        conda_eigen = os.path.join(conda_prefix, 'include', 'eigen3')
        if os.path.exists(conda_eigen):
            print(f"Using Conda Eigen: {conda_eigen}")
            return conda_eigen
    
    # if Conda not has eigen, back to system
    system_eigen = "/usr/include/eigen3"
    print(f"Using System Eigen: {system_eigen}")
    return system_eigen

eigen_include = get_eigen_include()

ext_modules = [
    # annotate this part if eigen version higher than 3.3.7
    Pybind11Extension(
        "rlPx4Controller.traj_tools.polyTrajGen",
        ["bind/polyTrajGen.cpp","src/polynomial_traj.cpp"],
        # Example: passing in the version to the compiled code
        define_macros=[("VERSION_INFO", __version__)],
        include_dirs=["include", eigen_include],  # use detect path

    ),

    
    Pybind11Extension(
        "rlPx4Controller.pyControl",
        ["bind/pyControl.cpp"],
        # Example: passing in the version to the compiled code
        define_macros=[("VERSION_INFO", __version__)],
        include_dirs=["include", eigen_include],
    ),
    Pybind11Extension(
        "rlPx4Controller.pyParallelControl",
        ["bind/pyParallelControl.cpp"],
        # Example: passing in the version to the compiled code
        define_macros=[("VERSION_INFO", __version__)],
        include_dirs=["include", eigen_include],

    ),
]

setup(
    name="rlPx4Controller",
    version=__version__,
    author="Wang Hao",
    author_email="hwangwork@163.com",
    url="https://github.com/pybind/python_example",
    description="Px4 Quadrotor Contorller",
    long_description="",
    packages=find_packages(),
    install_requires=[
        # 'torch',
    ],
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)
