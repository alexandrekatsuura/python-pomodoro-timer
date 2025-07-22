
# 📝 Pomodoro Timer with Sound Notification

![GitHub repo size](https://img.shields.io/github/repo-size/alexandrekatsuura/python-pomodoro-timer?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/alexandrekatsuura/python-pomodoro-timer?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/alexandrekatsuura/python-pomodoro-timer?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/alexandrekatsuura/python-pomodoro-timer?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/alexandrekatsuura/python-pomodoro-timer?style=for-the-badge)

## 📚 Academic Use Disclaimer

> ⚠️ This is an academic project created for learning purposes only.
> It is not intended for production use.

## ℹ️ About

This project is a command-line Pomodoro timer application built in Python. It helps users manage their work and break sessions using the Pomodoro Technique, providing sound notifications to signal the end of each interval. The timer is configurable and designed with a clean, object-oriented structure, making it easy to understand, extend, and test.

## 🚀 Features

*   **Customizable Sessions**: Set custom durations for work, short breaks, and long breaks.
*   **Configurable Cycles**: Define how many work/short break cycles to complete before a long break.
*   **Sound Notifications**: Plays a sound to alert the user when a session ends.
*   **Command-Line Interface (CLI)**: Simple and interactive, runs in any standard terminal.
*   **Error Handling**: Validates inputs to ensure the timer runs correctly.
*   **Unit Tested**: Includes a suite of `pytest` tests to verify functionality.
*   **Clean Project Structure**: Organized into `src` and `tests` directories for maintainability.

## 🛠️ Technologies Used

*   **Python 3.x**
*   **`pytest`**: For creating and running unit tests.

## ⚙️ How to Run the Project

### Prerequisites

*   Python 3.x installed on your system.
*   (Optional) A sound player application for your operating system (e.g., `aplay` on Linux, `afplay` on macOS).

### Installation

1.  Clone this repository:

    ```bash
    git clone https://github.com/alexandrekatsuura/python-pomodoro-timer
    cd python-pomodoro-timer
    ```

2.  (Recommended) Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate      # On Linux/macOS
    # .venv\Scripts\activate       # On Windows
    ```

3.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

To start the timer, run the following command from the project root:

```bash
python src/main.py
```

The timer will start, and you will see the countdown for the first work session. Follow the on-screen prompts to proceed through the cycles.

## ✅ Running the Tests

To run the unit tests, execute the following command from the project root directory:

```bash
pytest -v
```

This command will discover and run all tests located in the `tests/` directory.

## 📁 Project Structure

```bash
python-pomodoro-timer/
├── src/
│   ├── __init__.py
│   └── pomodoro_timer.py   # Contains the PomodoroTimer class
│   └── main.py             # Contains main execution logic
├── tests/
│   ├── __init__.py
│   └── test_pomodoro_timer.py # Unit tests for the PomodoroTimer class
├── .gitignore              # Standard Python .gitignore
├── README.md               # This documentation file
└── requirements.txt        # Project dependencies
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).


