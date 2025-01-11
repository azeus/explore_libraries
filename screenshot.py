import os
import subprocess
import schedule
import time
from datetime import datetime


def take_safari_screenshot():
    # Generate the filename with the current date
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"safari_screenshot_{date_str}.png"

    # AppleScript to activate Safari and focus on the last open tab
    applescript = """
    tell application "Safari"
        activate
        set theTabCount to count of tabs in window 1
        if theTabCount > 0 then
            set current tab of window 1 to tab theTabCount of window 1
        end if
    end tell
    """
    subprocess.run(["osascript", "-e", applescript])

    # Use screencapture to take a screenshot of the entire screen
    filepath = os.path.join(os.getcwd(), filename)
    subprocess.run(["screencapture", "-o", filepath])

    print(f"Safari screenshot saved as {filename}")


# Schedule the task for 11:11 AM every day
schedule.every().day.at("11:11").do(take_safari_screenshot)

print("Safari screenshot scheduler is running. Press Ctrl+C to stop.")
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nScheduler stopped.")
