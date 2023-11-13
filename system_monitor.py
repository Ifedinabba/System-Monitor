import psutil
import time

def get_system_health():
    """Gathers system health information such as CPU usage, memory utilization, and disk space."""
    health_info = {
        'cpu_percentage': psutil.cpu_percent(interval=1),
        'memory_usage': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent
    }
    return health_info

def main():
    """Main function to monitor system health."""
    try:
        while True:
            health = get_system_health()
            print(f"CPU Usage: {health['cpu_percentage']}%, Memory Usage: {health['memory_usage']}%, Disk Usage: {health['disk_usage']}%")
            time.sleep(60)  # Pause for 60 seconds
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
