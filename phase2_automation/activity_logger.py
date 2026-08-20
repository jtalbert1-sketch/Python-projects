import datetime
with open("activity_tracker.log", "a") as log:
    now = datetime.datetime.now()
    log.write(f"Activity logged at: {now}\n")