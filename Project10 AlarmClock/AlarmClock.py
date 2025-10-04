import datetime
import time
import winsound  # Windows built-in sound library

def set_alarm():
    print("---Alarm Clock---")
    alarm_time = input("Enter alarm time (HH:MM:SS, 24-hour format): ")

    try:
        alarm_hour, alarm_minute, alarm_second = map(int, alarm_time.split(":"))
    except ValueError:
        print("❌ Invalid format! Please use HH:MM:SS (e.g., 07:30:00).")
        return

    print(f"✅ Alarm set for {alarm_time}. Waiting...")

    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")

        if current_time == alarm_time:
            print("\n⏰ Wake up! Time to get going!")
            
            # Play a beep sound repeatedly for a few seconds
            for _ in range(5):
                winsound.Beep(1000, 800)  # (frequency, duration in ms)
            break

        time.sleep(1)

if __name__ == "__main__":
    set_alarm()
