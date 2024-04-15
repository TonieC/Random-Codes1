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
    {"messages": ["Sana'y hindi na lang Pinilit pa"], "display_duration": 1.5},
    {"messages": ["Wala ring patutunguhan"], "display_duration": 2},
    {"messages": ["Kahit sabihin ko pang mahal kita"], "display_duration": 3},
    {"messages": ["Nalulungkot, nayayamot, nagmumukmok"], "display_duration": 1.5},
    {"messages": ["Hindi ko pa yata kaya pang"], "display_duration": 0.3},
    {"messages": ["Labanan ang damdamin ko"], "display_duration": 5},
    {"messages": ["Sana'y hindi na lang pinilit pa"], "display_duration": 2},
    {"messages": ["Wala ring patutunguhan"], "display_duration": 1.5},
    {"messages": ["Kahit sabihin ko pang mahal kita"], "display_duration": 3},
    {"messages": [":("], "display_duration": 10},
]

typing_speed = 0.1  

for cluster in message_clusters:
    display_duration = cluster["display_duration"]
    for message in cluster["messages"]:
        display_message(message, typing_speed)
        time.sleep(display_duration)
        clear_message(message)
