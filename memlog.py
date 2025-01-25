import psutil
import time
import logging
from datetime import datetime


def monitor_memory(threshold_mb=100, duration_sec=60, interval=5):
    logging.basicConfig(filename='memory_usage.log', level=logging.INFO)

    end_time = time.time() + duration_sec
    while time.time() < end_time:
        for proc in psutil.process_iter():
            try:
                with proc.oneshot():
                    mem_info = proc.memory_info()
                    if mem_info:
                        mem_mb = mem_info.rss / (1024 * 1024)
                        if mem_mb > threshold_mb:
                            logging.warning(
                                f"{datetime.now()} - High memory usage:\n"
                                f"Process: {proc.name()}\n"
                                f"PID: {proc.pid}\n"
                                f"Memory: {mem_mb:.2f} MB\n"
                            )
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        time.sleep(interval)


if __name__ == '__main__':
    monitor_memory(threshold_mb=200, duration_sec=300)