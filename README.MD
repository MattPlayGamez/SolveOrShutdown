# Solve Or Shutdown

**Solve Or Shutdown** is a Python-based application designed to periodically check if a specific process (e.g., `FlightSimulator.exe`) is running on your system. If the process is not detected, the program will challenge the user with a simple arithmetic problem randomly. If the user fails to solve the problem correctly within the allotted time (5min), the system will automatically shut down.

## Features

- **Process Monitoring**: Continuously monitors your system for the presence of a specified process.
- **Random Arithmetic Challenge**: If the process is not found, a GUI window presents a random arithmetic problem (addition) for the user to solve.
- **Countdown Timer**: The user has 5 minutes to solve the problem, or the system will shut down.
- **Automatic Shutdown**: If the user fails to provide the correct answer or the time runs out, the system will shut down immediately.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/MattPlayGamez/SolveOrShutdown
    cd SolveOrShutdown
    ```

2. **Install dependencies**:

    The script uses the `tkinter` library for the GUI, which is included in Python's standard library, so no additional packages are required.

3. **Run the script**:

    You can start the program by running the following command:

    ```bash
    python funnywunny.pyw
    ```

## How It Works

- The script starts by running an infinite loop that pauses for one hour at each iteration.
- During each iteration, it generates a random number between 0 and 10.
- If the random number is 5 or higher and the monitored process (`FlightSimulator.exe`) is not running, a GUI window will appear with a simple addition problem.
- The user must solve the problem within 5 minutes, or the system will shut down.
- The countdown timer and the process of checking the answer run concurrently to ensure that the user cannot simply close the window or ignore the prompt.

## Usage

- **Customizing the Monitored Process**: You can change the process that the script monitors by modifying the `process_name` in the `is_process_running()` function.
- **Adjusting the Arithmetic Problem**: The current script generates a random addition problem with numbers ranging from 0 to 1000. This can be modified in the `run_gui()` function.
- **Modifying the Timer**: The shutdown timer is set to 5 minutes by default. This can be adjusted by changing the `time_left` variable in the `run_gui()` function.

## Important Notes

- This script is designed for educational and testing purposes. Use it with caution, especially when testing the shutdown feature.
- Ensure all your work is saved before running this script, as it could result in an unexpected system shutdown if the problem is not solved correctly.
- Put it on friends pc and see how long it takes for them to figure out what's happening

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or report an issue on the GitHub repository.

