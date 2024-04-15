import time
import sys

def display_message(message, typing_speed):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(typing_speed)

def clear_message(message):
    sys.stdout.write('\r' + ' ' * len(message) + '\r')
    sys.stdout.flush()

message_clusters = [
    {"messages": ["Example"], "display_duration": 1},
    {"messages": ["Example2"], "display_duration": 2},
]

typing_speed = 0.1  

for cluster in message_clusters:
    display_duration = cluster["display_duration"]
    for message in cluster["messages"]:
        display_message(message, typing_speed)
        time.sleep(display_duration)
        clear_message(message)
