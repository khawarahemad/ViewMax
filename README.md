
# ViewMax - GitHub View Increaser Tool

**ViewMax.py** is a tool designed to increase views on GitHub repositories by automating multiple browser visits.

## How to Use

You can run **ViewMax.py** on **Mac**, **Windows**, and **Termux**. Below are the instructions for each platform.

### Prerequisites
Before using **ViewMax.py**, ensure you have the following:

- **Python 3.x**
- **Selenium** library
- **ChromeDriver** installed

---

### How to Run on Mac

1. **Install Python** (if not already installed):
   - Download from [python.org](https://www.python.org/downloads/).

2. **Install ChromeDriver**:
   - Install via Homebrew:
     ```bash
     brew install chromedriver
     ```
   - Add **ChromeDriver** to the PATH:
     ```bash
     sudo ln -s /opt/homebrew/bin/chromedriver /usr/local/bin/chromedriver
     ```

3. **Create a Virtual Environment**:
   ```bash
   python3 -m venv ~/myenv
   ```

4. **Activate the Virtual Environment**:
   ```bash
   source ~/myenv/bin/activate
   ```

5. **Install Selenium**:
   ```bash
   pip install selenium
   ```

6. **Run the Tool**:
   ```bash
   python3 -u "/path/to/ViewMax.py"
   ```

7. **Deactivate the Virtual Environment** after running:
   ```bash
   deactivate
   ```

---

### How to Run on Windows

1. **Install Python** (if not already installed):
   - Download from [python.org](https://www.python.org/downloads/).

2. **Install ChromeDriver**:
   - Download from [ChromeDriver download page](https://sites.google.com/a/chromium.org/chromedriver/).
   - Extract and add **ChromeDriver** to your PATH.

3. **Create a Virtual Environment**:
   ```bash
   python -m venv C:\path\to\myenv
   ```

4. **Activate the Virtual Environment**:
   ```bash
   C:\path\to\myenv\Scripts\activate
   ```

5. **Install Selenium**:
   ```bash
   pip install selenium
   ```

6. **Run the Tool**:
   ```bash
   python C:\path\to\ViewMax.py
   ```

7. **Deactivate the Virtual Environment** after running:
   ```bash
   deactivate
   ```

---

### How to Run on Termux (Android)

1. **Install Termux** from the Play Store or F-Droid.

2. **Install Python**:
   ```bash
   pkg install python
   ```

3. **Install pip**:
   ```bash
   pkg install python-pip
   ```

4. **Install ChromeDriver** (manual installation):
   ```bash
   pkg install wget
   wget https://chromedriver.storage.googleapis.com/your_version/chromedriver_linux64.zip
   unzip chromedriver_linux64.zip
   mv chromedriver /usr/bin/
   ```

5. **Install Selenium**:
   ```bash
   pip install selenium
   ```

6. **Run the Tool**:
   ```bash
   python /path/to/ViewMax.py
   ```

---

## Features

- **Safe Mode**: Safely increase views with fewer browsers.
- **Extreme Mode**: Rapidly increase views with multiple browsers.
- **Progress Feedback**: Get real-time updates during the process.

---

## License

This project is licensed under the MIT License.

---

### Troubleshooting

- Make sure **ChromeDriver** is correctly installed and added to your PATH.
- Ensure the **virtual environment** is active when installing dependencies and running the tool.
