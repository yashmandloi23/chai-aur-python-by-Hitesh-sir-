import time

wait_time = 1
max_retry = 5
attempt = 0

while attempt < max_retry:
    print("attempt",attempt+1,"wait_time",wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempt += 1
