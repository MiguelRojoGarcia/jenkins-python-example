import psutil

def get_system_resume():
    current_memory_usage = psutil.virtual_memory()[2]
    cpu_usage = psutil.cpu_percent(4)

    return {
        "current_memory_usage":current_memory_usage,
        "cpu_usage":cpu_usage
    }
    