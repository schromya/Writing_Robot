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