import os

def get_cpu_temperature():
    temp_str = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
    temp_c = float(temp_str) / 1000.0
    return temp_c

def main():
    temp = get_cpu_temperature()
    print(f"Jetson CPU Temperature: {temp:.2f} °C")

if __name__ == "__main__":
    main()
