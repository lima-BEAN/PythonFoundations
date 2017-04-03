import webbrowser
import time

for x in range(1):
    # ctime gives CURRENT TIME
    print("This program started on " + time.ctime())
    time.sleep(3)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
