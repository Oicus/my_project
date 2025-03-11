# Keylogger Project

## Overview

This project is a keylogger designed to capture and send keystrokes to a specified server. The keylogger uses the `pynput` library to capture keystrokes and `requests` library to send the data.

## Features

- Captures keystrokes including special keys like Enter, Tab, and Space.
- Sends captured keystrokes to a specified server at regular intervals.
- Configurable server IP address, port, and time interval.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Oicus/my_project.git
    cd my_project
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure the server is running and configured to receive data.

## Usage

To run the keylogger, use the following command:
```sh
python keylogger.py
```

## Legal Disclaimer

This project is intended for educational purposes only. The use of this tool for capturing keystrokes without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

## Development and Contributions

This project is open to contributions and further development. Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](LICENSE)
