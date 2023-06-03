import psutil

memory_usage = psutil.virtual_memory()
print(memory_usage)
print(f"메모리 사용량: {memory_usage[2]:.2f}%")
print(f"CPU 사용량: {psutil.cpu_percent(interval=0.1):.2f}%")