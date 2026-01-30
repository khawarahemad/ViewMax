import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
import sys
import time
import os
import platform

# Lock for thread-safe printing
log_lock = threading.Lock()

def get_chromedriver_path():
    """Auto-detect chromedriver path based on OS."""
    system = platform.system()
    
    if system == "Linux":
        # Common Linux paths
        common_paths = [
            "/usr/bin/chromedriver",
            "/usr/local/bin/chromedriver",
            "/usr/lib/chromium-browser/chromedriver",
            "/snap/bin/chromium.chromedriver"
        ]
        for path in common_paths:
            if os.path.exists(path):
                return path
        # If not found, let Selenium find it in PATH
        return "chromedriver"
    elif system == "Darwin":  # macOS
        return "/opt/homebrew/bin/chromedriver"
    else:  # Windows
        return "chromedriver.exe"

def get_chrome_options():
    """Configure Chrome options for Linux/VPS environment."""
    chrome_options = Options()
    
    # Essential options for headless operation
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    
    # Additional options for VPS/server environments
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    # User agent to avoid detection
    chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    # Memory optimization for VPS
    chrome_options.add_argument("--disable-background-networking")
    chrome_options.add_argument("--disable-background-timer-throttling")
    chrome_options.add_argument("--disable-backgrounding-occluded-windows")
    chrome_options.add_argument("--disable-breakpad")
    chrome_options.add_argument("--disable-component-extensions-with-background-pages")
    chrome_options.add_argument("--disable-features=TranslateUI,BlinkGenPropertyTrees")
    chrome_options.add_argument("--disable-ipc-flooding-protection")
    chrome_options.add_argument("--disable-renderer-backgrounding")
    
    return chrome_options

def visit_site_safe(url, browser_id, progress, progress_message):
    """Safe method: Visit the site using a single browser instance."""
    driver = None
    try:
        chrome_options = get_chrome_options()
        chromedriver_path = get_chromedriver_path()
        
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Update progress message for the browser visiting
        with log_lock:
            progress_message[browser_id] = f"Browser {browser_id + 1} visiting {url}"
        
        driver.get(url)
        time.sleep(3)  # Wait for page to load
        progress[browser_id] = True
        
        # Update progress message for the browser completion
        with log_lock:
            progress_message[browser_id] = f"Browser {browser_id + 1} has completed."
    except Exception as e:
        with log_lock:
            progress_message[browser_id] = f"Browser {browser_id + 1} failed: {str(e)}"
        progress[browser_id] = False
    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass

def visit_site_extreme(url, browser_id, progress, progress_message):
    """Extreme method: Visit the site using multiple browser instances."""
    driver = None
    try:
        chrome_options = get_chrome_options()
        chromedriver_path = get_chromedriver_path()
        
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Update progress message for the browser visiting
        with log_lock:
            progress_message[browser_id] = f"Browser {browser_id + 1} visiting {url}"
        
        driver.get(url)
        time.sleep(3)  # Wait for page to load
        progress[browser_id] = True
        
        # Update progress message for the browser completion
        with log_lock:
            progress_message[browser_id] = f"Browser {browser_id + 1} has completed."
    except Exception as e:
        with log_lock:
            progress_message[browser_id] = f"Browser {browser_id + 1} failed: {str(e)}"
        progress[browser_id] = False
    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass

def display_progress(progress, total_visits):
    """Function to update the progress in a clean, professional way."""
    completed = sum(progress)
    percentage = (completed / total_visits) * 100
    progress_bar = "#" * (int(percentage) // 2)
    remaining_bar = "-" * (50 - len(progress_bar))
    sys.stdout.write(f"\rProgress: [{progress_bar}{remaining_bar}] {completed}/{total_visits} ({int(percentage)}%)")
    sys.stdout.flush()

def print_summary(progress, total_visits, mode, start_time):
    """Print the final summary of the execution."""
    completed = sum(progress)
    success_rate = (completed / total_visits) * 100
    end_time = time.time()
    duration = end_time - start_time
    status = "SUCCESS" if completed == total_visits else "FAILED"
    
    print(f"\n\n----- Execution Summary -----")
    print(f"Mode: {'Safe' if mode == '1' else 'Extreme'} mode")
    print(f"Total Visits: {total_visits}")
    print(f"Total Successful Visits: {completed} ({success_rate:.2f}%)")
    print(f"Execution Status: {status}")
    print(f"Time Taken: {duration:.2f} seconds")
    print(f"-----------------------------\n")

def main():
    print(f"Running on: {platform.system()} {platform.release()}")
    print(f"Chromedriver path: {get_chromedriver_path()}\n")
    
    # Get GitHub username from the user
    username = input("Enter your GitHub username: ").strip()
    url = f"https://github.com/{username}"
    print(f"Target URL: {url}\n")

    # Choose mode: Safe or Extreme
    mode = input("Enter 1 for Safe mode or 2 for Extreme mode: ").strip()
    
    # Safe Mode
    if mode == "1":
        total_visits = int(input("Enter the total number of visits: ").strip())
        progress = [False] * total_visits
        progress_message = [""] * total_visits
        start_time = time.time()

        # Visit the site in safe mode
        for i in range(total_visits):
            visit_site_safe(url, i, progress, progress_message)
            display_progress(progress, total_visits)

        print_summary(progress, total_visits, mode, start_time)

    # Extreme Mode
    elif mode == "2":
        total_visits = int(input("Enter the total number of visits: ").strip())
        max_browsers = int(input("Enter the number of concurrent browsers (recommended: 3-5 for VPS): ").strip())
        progress = [False] * total_visits
        progress_message = [""] * total_visits
        start_time = time.time()

        # Use ThreadPoolExecutor to run multiple browsers in parallel
        with ThreadPoolExecutor(max_workers=max_browsers) as executor:
            futures = []
            for i in range(total_visits):
                futures.append(executor.submit(visit_site_extreme, url, i, progress, progress_message))

            # Monitor progress
            while sum(progress) < total_visits:
                time.sleep(1)
                display_progress(progress, total_visits)

        print_summary(progress, total_visits, mode, start_time)

    else:
        print("Invalid choice. Please enter 1 for Safe mode or 2 for Extreme mode.")

if __name__ == "__main__":
    main()