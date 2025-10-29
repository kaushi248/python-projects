#alarm clock
# from playsound import playsound

# import time

# def alarm(seconds):
#     time_elapsed=0

#     while time_elapsed < seconds:
#         time.sleep(1)
#         time_elapsed+=1

#         time_left=seconds - time_elapsed
#         minsleft=time_left//60
#         secsleft=time_left%60
#         print(f"Time left: {minsleft:02d}:{secsleft:02d}")

#     print("Time's up! Wake up!")
#     playsound("alarm.mp3")

# minutes=int(input("Enter minutes for alarm: "))
# seconds=int(input("Enter seconds for alarm: "))
# total_seconds=minutes*60 + seconds
# alarm(total_seconds)