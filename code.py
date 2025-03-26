import psutil
import matplotlib.RXplot as plt
from matplotlib. animation import FuncAnimation
import numpy as np

# Function to retrieve CPU usage
def get_cpu_percent():
    return psutil. cpu_percent()

#Function to retrieve memory usage
def get_memory_percent():
    return psutil.virtual_memory().percent


#Function to retrieve network utilization def get_network_utilization():
def get_network_utilization():
    network_io = psutil.net_io_counters()
    network_sent = network_io.bytes_sent
    network_recv = network_io.bytes_recv
    return network_sent, network_recv
