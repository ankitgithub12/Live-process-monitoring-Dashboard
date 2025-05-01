import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# System info functions
def get_cpu_percent():
    return psutil.cpu_percent()

def get_memory_percent():
    return psutil.virtual_memory().percent

def get_network_utilization():
    net = psutil.net_io_counters()
    return net.bytes_sent, net.bytes_recv

def get_disk_usage():
    return psutil.disk_usage('/').percent

def get_process_count():
    return len(psutil.pids())

# Data storage
cpu_time, cpu_data = [], []
memory_time, memory_data = [], []
network_time, network_sent_data, network_recv_data = [], [], []
disk_time, disk_data = [], []
process_time, process_data = [], []

# Create single figure with subplots
fig, ((ax_cpu, ax_memory), (ax_network, ax_disk), (ax_process, ax_blank)) = plt.subplots(3, 2, figsize=(14, 9))
fig.suptitle("System Monitoring Dashboard", fontsize=16)

# Remove blank axis
fig.delaxes(ax_blank)

# Update all plots
def update_all(frame):
    # Reset data after 100 frames
    if frame % 100 == 0:
        cpu_time.clear(); cpu_data.clear()
        memory_time.clear(); memory_data.clear()
        network_time.clear(); network_sent_data.clear(); network_recv_data.clear()
        disk_time.clear(); disk_data.clear()
        process_time.clear(); process_data.clear()

    # CPU
    cpu = get_cpu_percent()
    cpu_time.append(frame % 100)
    cpu_data.append(cpu)
    ax_cpu.clear()
    ax_cpu.plot(cpu_time, cpu_data, color='blue', label='CPU Usage (%)')
    ax_cpu.set_title('CPU Usage')
    ax_cpu.set_xlabel('Time')
    ax_cpu.set_ylabel('Usage (%)')
    ax_cpu.legend()

    # Memory
    mem = get_memory_percent()
    memory_time.append(frame % 100)
    memory_data.append(mem)
    ax_memory.clear()
    ax_memory.plot(memory_time, memory_data, color='green', label='Memory Usage (%)')
    ax_memory.set_title('Memory Usage')
    ax_memory.set_xlabel('Time')
    ax_memory.set_ylabel('Usage (%)')
    ax_memory.legend()

    # Network
    sent, recv = get_network_utilization()
    network_time.append(frame % 100)
    network_sent_data.append(sent)
    network_recv_data.append(recv)
    ax_network.clear()
    ax_network.plot(network_time, network_sent_data, label='Sent (bytes)', color='orange')
    ax_network.plot(network_time, network_recv_data, label='Received (bytes)', color='purple')
    ax_network.set_title('Network Utilization')
    ax_network.set_xlabel('Time')
    ax_network.set_ylabel('Bytes')
    ax_network.legend()

    # Disk
    disk = get_disk_usage()
    disk_time.append(frame % 100)
    disk_data.append(disk)
    ax_disk.clear()
    ax_disk.plot(disk_time, disk_data, color='red', label='Disk Usage (%)')
    ax_disk.set_title('Disk Usage')
    ax_disk.set_xlabel('Time')
    ax_disk.set_ylabel('Usage (%)')
    ax_disk.legend()

    # Process count
    proc = get_process_count()
    process_time.append(frame % 100)
    process_data.append(proc)
    ax_process.clear()
    ax_process.plot(process_time, process_data, color='brown', label='Process Count')
    ax_process.set_title('Process Count')
    ax_process.set_xlabel('Time')
    ax_process.set_ylabel('Count')
    ax_process.legend()

# Animation
ani = FuncAnimation(fig, update_all, frames=np.arange(0, 1000), interval=1000)

# Adjust layout spacing
plt.tight_layout()
fig.subplots_adjust(top=0.93, hspace=0.5, wspace=0.3)

# Show all plots in one window
plt.show()