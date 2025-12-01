# Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import  time

wait_time = 1
max_tries = 5
attempts = 0

while attempts < max_tries:
    print(f'attempts: {attempts + 1}, - waiting time: {wait_time}s')
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
