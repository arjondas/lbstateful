import subprocess
import time
import random
import matplotlib.pyplot as plt
import os
random.seed(1)

number_of_requests = 1000
request_rate = 10
for i in range(number_of_requests):
    print("sending....." + str(i))
    #subprocess.run('curl http://127.0.0.1:54324/service/1000/2/3', shell=True)
    command = 'curl http://127.0.0.1:54324/service/' + str(random.randint(100, 5000)) + '/' + str(random.randint(1, 3)) + "/" + str(random.ran 
    subprocess.Popen(command, shell=True)
    time.sleep(1/request_rate)


subprocess.run('clear')
f = open('responses.txt')

success_count = 0
failed_count = 0
content = f.read().split(' ')
for word in content:
    if 'properly' in word:
        success_count += 1
    elif 'failed' in word:
        failed_count += 1
print("Success : " + str(success_count))
print("Failed : " + str(failed_count))
success_rate = (float(success_count)/number_of_requests) * 100
failed_rate = (float(failed_count)/number_of_requests) * 100
print("Success : " + str(success_rate) + ' %')
print("Failed : " + str(failed_rate) + ' %')





