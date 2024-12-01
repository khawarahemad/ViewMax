
# ViewMax - GitHub View Increaser Tool

**ViewMax** is a tool designed to increase views on GitHub repositories by automating multiple browser visits.

## How to Use

You can run ViewMax on **Mac**, **Windows**, and **Termux**. Below are the instructions for each platform.

### Prerequisites
Before using ViewMax, you need to install the following dependencies:

- **Python 3.x**: Ensure you have Python 3 installed. You can check this with:
  ```bash
  python --version
  ```

- **Selenium** library: A Python library for web automation.
- **ChromeDriver**: WebDriver used to control Google Chrome.

You can install these using pip.

---

### How to Run on Mac

1. **Install Python** (if not already installed).
   - Download and install Python from [here](https://www.python.org/downloads/).
   
2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv ~/myenv
   ```
   
3. **Activate the Virtual Environment**:
   ```bash
   source ~/myenv/bin/activate
   ```

4. **Install Selenium**:
   ```bash
   pip install selenium
   ```

5. **Run the Tool**:
   ```bash
   python3 -u "/path/to/ViewMax/site_refresher.py"
   ```

6. **Deactivate the Virtual Environment** after running:
   ```bash
   deactivate
   ```

---

### How to Run on Windows

1. **Install Python** (if not already installed).
   - Download and install Python from [here](https://www.python.org/downloads/).

2. **Create a Virtual Environment**:
   ```bash
   python -m venv C:\path\to\myenv
   ```

3. **Activate the Virtual Environment**:
   ```bash
   C:\path\to\myenv\Scripts\activate
   ```

4. **Install Selenium**:
   ```bash
   pip install selenium
   ```

5. **Run the Tool**:
   ```bash
   python C:\path\to\ViewMax\site_refresher.py
   ```

6. **Deactivate the Virtual Environment** after running:
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

4. **Install ChromeDriver** (you may need to manually install ChromeDriver or use an appropriate version):
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
   python /path/to/ViewMax/site_refresher.py
   ```

---

## Features

- **Safe Mode**: Safely increase views by using fewer browsers.
- **Extreme Mode**: Increase views rapidly with more browsers.
- **Progress Feedback**: ViewMax provides real-time updates on the progress of the tool.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

- **Selenium**: Web automation framework used for automating browser actions.
- **ChromeDriver**: Required to interact with Chrome browsers.

---

### Troubleshooting

If you run into any issues, ensure the following are correctly configured:
- **ChromeDriver** must be installed and added to your PATH.
- Ensure that your **virtual environment** is active when installing dependencies and running the tool.
