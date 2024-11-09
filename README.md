# Writing Robot
M^3 project


## Setup
1. First you will need to start a venv:

    **Mac/Linux**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    **Windows**:
    ```bash
    python3 -m venv venv
    .\venv\Scripts\Activate.ps1
    ```
    If this doesn't work, you may have to run this in an Admin shell first:
    ```bash
    set-executionpolicy remotesigned
    ```


2. Next, install all the python requirements
    ```bash
    pip install -r requirements.txt
    ```

## Running
To run the simulation, make sure you are in this directory and run:

```bash
python3 simulation.py
```

You should see a window pop up with the simulation.

To run the pinocchio test, make sure you are in this directory and run:

```bash
python3 pinocchio_test.py
```




### Mya notes: please ignore
```bash
mkdir rbdl-build
cd rbdl-build/
ccmake ../rbdl 
```

Enable RBDL_BUILD_ADDON_URDFREADER, RBDL_BUILD_EXECUTABLES,  RBDL_BUILD_PYTHON_WRAPPER, RBDL_BUILD_TESTS 

Click c and then later g

```bash
cd rbdl
doxygen Doxyfile
cd ../rbdl-build
python3 python/setup.py install
cd ..
```

Drag and drop /rbdl/doc/html/index.html into browser to view documentation.


```bash
echo 'export PYTHONPATH=$PYTHONPATH:/workspace/rbdl/python' >> ~/.bashrc
source ~/.bashrc
```



Pinocchio: https://github.com/stack-of-tasks/pinocchio/blob/master/examples/README.md
https://ramoncalvo.com/blog/joint-space-inertia/

https://github.com/bhtxy0525/A_Example_for_Calculating_Robot_Dynamics_Using_Pinocchio_Library/blob/main/README.md

Install conda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html
```bash
pip install pin

```