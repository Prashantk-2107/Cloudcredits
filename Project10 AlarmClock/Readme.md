# Alarm Clock
A simple and functional **Python Alarm Clock** that allows you to set an alarm for a specific time.  
When the current time matches the alarm time, it triggers a sound notification.

## Features
- Set a custom alarm time (hour, minute, second)
- Play alarm sound when time matches
- Uses Python's `datetime` and `time` modules
- Simple command-line interface (CLI)
- Option to stop the alarm manually

## Tech Stack
- **Language:** Python  
- **Libraries Used:**  
  - `datetime` — for managing time  
  - `time` — for delay and checking  
  - `playsound` or `pygame` — to play alarm sound  

## How It Works

1. The program asks the user to enter the alarm time in `HH:MM:SS` format.  
2. It continuously checks the current system time.  
3. When the system time matches the set alarm time, a sound is played.  
4. The alarm keeps ringing until stopped manually (you can modify it to stop automatically).

