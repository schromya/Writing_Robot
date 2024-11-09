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
sudo ./setup.py install
```

Drag and drop /rbdl/doc/html/index.html into browser to view documentation.


export PYTHONPATH=$PYTHONPATH:<path-to-the-RBDL-build-directory>/python

echo 'export PYTHONPATH=$PYTHONPATH:/workspace/rbdl/python' >> ~/.bashrc

