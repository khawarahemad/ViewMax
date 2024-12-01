import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
import sys
import time

# Lock for thread-safe printing
log_lock = threading.Lock()

def visit_site_safe(url, browser_id, progress, progress_message):
    """Safe method: Visit the site using a single browser instance."""
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        service = Service("/opt/homebrew/bin/chromedriver")  # Update with your path to chromedriver
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Update progress message for the browser visiting
        with log_lock:  # Ensures that only one thread prints at a time
            progress_message[browser_id] = f"Browser {browser_id + 1} visiting {url}"
        
        driver.get(url)
        progress[browser_id] = True  # Mark this browser ID as completed
        
        # Update progress message for the browser completion
        with log_lock:  # Ensures that only one thread prints at a time
            progress_message[browser_id] = f"Browser {browser_id + 1} has completed."
    except Exception as e:
        with log_lock:  # Ensures that only one thread prints at a time
            progress_message[browser_id] = f"Browser {browser_id + 1} failed to visit {url} due to error: {e}"
        progress[browser_id] = False  # Mark this browser ID as failed
    finally:
        driver.quit()

def visit_site_extreme(url, browser_id, progress, progress_message):
    """Extreme method: Visit the site using multiple browser instances."""
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        service = Service("/opt/homebrew/bin/chromedriver")  # Update with your path to chromedriver
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Update progress message for the browser visiting
        with log_lock:  # Ensures that only one thread prints at a time
            progress_message[browser_id] = f"Browser {browser_id + 1} visiting {url}"
        
        driver.get(url)
        progress[browser_id] = True  # Mark this browser ID as completed
        
        # Update progress message for the browser completion
        with log_lock:  # Ensures that only one thread prints at a time
            progress_message[browser_id] = f"Browser {browser_id + 1} has completed."
    except Exception as e:
        with log_lock:  # Ensures that only one thread prints at a time
            progress_message[browser_id] = f"Browser {browser_id + 1} failed to visit {url} due to error: {e}"
        progress[browser_id] = False  # Mark this browser ID as failed
    finally:
        driver.quit()

def display_progress(progress, total_visits):
    """Function to update the progress in a clean, professional way."""
    completed = sum(progress)
    percentage = (completed / total_visits) * 100
    progress_bar = "#" * (int(percentage) // 2)  # Progress bar of 50 max length
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
    # Get GitHub username from the user
    username = input("Enter your GitHub username: ").strip()
    url = f"https://github.com/{username}"
    print(f"Target URL: {url}\n")

    # Choose mode: Safe or Extreme
    mode = input("Enter 1 for Safe mode or 2 for Extreme mode: ").strip()
    
    # Safe Mode
    if mode == "1":
        total_visits = int(input("Enter the total number of visits: ").strip())
        progress = [False] * total_visits  # Track progress of each visit
        progress_message = [""] * total_visits  # To store messages
        start_time = time.time()

        # Visit the site in safe mode using a single browser instance
        for i in range(total_visits):
            visit_site_safe(url, i, progress, progress_message)
            display_progress(progress, total_visits)
            with log_lock:
                print(f"\r{progress_message[i]}", end="")
            time.sleep(2)  # Simulate wait time between visits

        print_summary(progress, total_visits, mode, start_time)

    # Extreme Mode
    elif mode == "2":
        total_visits = int(input("Enter the total number of visits: ").strip())
        max_browsers = int(input("Enter the number of concurrent browsers: ").strip())
        progress = [False] * total_visits  # Track progress of each visit
        progress_message = [""] * total_visits  # To store messages
        start_time = time.time()

        # Use ThreadPoolExecutor to run multiple browsers in parallel
        with ThreadPoolExecutor(max_workers=max_browsers) as executor:
            futures = []
            for i in range(total_visits):
                futures.append(executor.submit(visit_site_extreme, url, i, progress, progress_message))

            # Monitor progress while threads are working
            while sum(progress) < total_visits:
                time.sleep(1)  # Sleep to simulate monitoring
                display_progress(progress, total_visits)
                with log_lock:
                    for i in range(total_visits):
                        if progress[i]:
                            print(f"\r{progress_message[i]}", end="")

        print_summary(progress, total_visits, mode, start_time)

    else:
        print("Invalid choice. Please enter 1 for Safe mode or 2 for Extreme mode.")

if __name__ == "__main__":
    main()
