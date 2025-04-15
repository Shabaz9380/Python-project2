import psutil
import csv
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def monitor_resources(interval, duration, output_file, email_address,
                      thresholds={'cpu': 80, 'memory': 80, 'disk': 80}):
    """Monitors CPU, memory, and disk usage with graphical output, data analysis,
    and email alerts.

    Args:
        interval (int): Interval in seconds between measurements.
        duration (int): Total duration of monitoring in seconds.
        output_file (str): Path to the CSV output file.
        email_address (str): Email address for sending alerts.
        thresholds (dict): Thresholds for resource usage (default: CPU: 80%,
                           memory: 80%, disk: 80%).
    """

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Timestamp', 'CPU Utilization (%)', 'Memory Usage (%)',
                      'Disk Usage (%)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    timestamps = []
    cpu_percentages = []
    memory_percentages = []
    disk_usages = []

    start_time = time.time()
    end_time = start_time + duration

    fig, ax1 = plt.subplots()
    cpu_line, = ax1.plot(timestamps, cpu_percentages, label='CPU')
    ax2 = ax1.twinx()
    memory_line, = ax2.plot(timestamps, memory_percentages, label='Memory')
    ax3 = ax1.twinx()
    disk_line, = ax3.plot(timestamps, disk_usages, label='Disk')

    def update_plot(i):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cpu_percent = psutil.cpu_percent(interval=interval)
        memory_percent = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        timestamps.append(timestamp)
        cpu_percentages.append(cpu_percent)
        memory_percentages.append(memory_percent)
        disk_usages.append(disk_usage)

        cpu_line.set_xdata(timestamps)
        cpu_line.set_ydata(cpu_percentages)
        memory_line.set_ydata(memory_percentages)
        disk_line.set_ydata(disk_usages)

        ax1.set_xlim(timestamps[0], timestamps[-1])
        ax1.set_ylim(0, 100)
        ax2.set_ylim(0, 100)
        ax3.set_ylim(0, 100)

        ax1.set_xlabel('Timestamp')
        ax1.set_ylabel('CPU (%)')
        ax2.set_ylabel('Memory (%)')
        ax3.set_ylabel('Disk (%)')
        plt.title('Resource Utilization Over Time')
        plt.grid(True)
        plt.legend()

        # Check for resource usage exceeding thresholds and send email alerts
        if cpu_percent > thresholds['cpu']:
            send_alert(email_address, f"CPU usage exceeded {thresholds['cpu']}%")
        if memory_percent > thresholds['memory']:
            send_alert(email_address, f"Memory usage exceeded {thresholds['memory']}%")
        if disk_usage > thresholds['disk']:
            send_alert(email_address, f"Disk usage exceeded {thresholds['disk']}%")

        return cpu_line, memory_line, disk_line

    def send_alert(email_address, message):
        """Sends an email alert to the specified address."""

        msg = MIMEMultipart()
        msg['From'] = 'System Monitor'
        msg['To'] = email_address
        msg['Subject'] = 'Resource Usage Alert'
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('gmail', 'password')
        server.sendmail('System Monitor', email_address, msg.as_string())
        server.quit()

    animation = FuncAnimation(fig, update_plot, interval=interval * 1000, repeat=True)
    plt.show()

    # Calculate summary statistics
    avg_cpu = sum(cpu_percentages) / len(cpu_percentages)
    avg_memory = sum(memory_percentages) / len(memory_percentages)
    avg_disk = sum(disk_usages) / len(disk_usages)

    print(f"Average CPU Utilization: {avg_cpu:.2f}%")
    print(f"Average Memory Usage: {avg_memory:.2f}%")
    print(f"Average Disk Usage: {avg_disk:.2f}%")

if __name__ == "__main__":
    interval = 5  # Monitoring interval in seconds
    duration = 60  # Monitoring duration in seconds
    output_file = 'resource_utilization.csv'
    email_address = 'your_email@example.com'  # Replace with your email address
    thresholds = {'cpu': 80, 'memory': 85, 'disk': 90}  # Customize thresholds

    print("Monitoring CPU, memory, and disk usage...")
    monitor_resources(interval, duration, output_file, email_address, thresholds)
    print("Monitoring complete. Data logged to", output_file)
