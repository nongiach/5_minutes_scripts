#!/usr/bin/env python3

import psutil
from collections import defaultdict
import matplotlib.pyplot as plt

def get_total_used_ram_by_process_name():
    process_memory = defaultdict(int)
    
    # Iterate through all running processes
    for proc in psutil.process_iter(['name', 'memory_info']):
        try:
            # Get process name and memory usage
            name = proc.info['name']
            mem_info = proc.info['memory_info']
            memory_usage = mem_info.rss
            
            # Add process memory usage to defaultdict
            process_memory[name] += memory_usage
        except psutil.NoSuchProcess:
            # Ignore processes that may have terminated between listing and retrieval
            pass
    
    return process_memory

def byte_to_human(byte):
    if byte < 1024*1024:
        return f"{byte / 1024:.1f} KB"
    elif byte < 1024*1024*1024:
        return f"{byte / (1024*1024):.1f} MB"
    else:
        return f"{byte / (1024*1024*1024):.1f} GB"

def main():
    process_memory = get_total_used_ram_by_process_name()
    
    # Sort process_memory by process name
    sorted_process_memory = sorted(process_memory.items(), key=lambda x: x[1])
    
    # Extract process names and memory usage
    names = [f"{name} - {byte_to_human(memory_usage)}" for name, memory_usage in sorted_process_memory]
    memory_usages = [memory_usage for _, memory_usage in sorted_process_memory]
    
    # Plot pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(memory_usages, labels=names, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title('Memory Usage by Process')
    
    # Save the pie chart as an image
    plt.savefig('memory_usage_pie_chart.png')
    
    # Show the pie chart
    plt.show()

if __name__ == "__main__":
    main()
