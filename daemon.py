import requests
from concurrent.futures import ThreadPoolExecutor
import time
import json
import subprocess
import time


def estimator(totalMemory, avaiableMemory, totalCore, avaiableCore, threshold):
    if (avaiableMemory >= (totalMemory * (threshold))) \
    and (avaiableCore >= int(totalCore  * (threshold))):
        return 1
    else:
        return 0



def get_url(url):
    time.sleep(1)
    return requests.get(url).content, time.time()

def writeConfg(backend_list, backend_status_list):

    command = 'user www-data;\n\
    worker_processes auto;\n\
    pid /run/nginx.pid;\n\
    include /etc/nginx/modules-enabled/*.conf;\n\
    \n\
    events {\n\
        worker_connections 768;\n\
        # multi_accept on;\n\
    }\n\
    \n\
    http {\n\
    \n\
        upstream test{\n'

    for i in range(len(backend_list)):
        if backend_status_list[i]:
            command = command + "\n\t\t\tserver " + backend_list[i] + ';'
    command = command + '	\n\t\t}\n\
        server {\n\
            listen 54324;\n\
                #server_name localhost;\n\
                location / {\n\
                    proxy_pass http://test/;\n\
                }\n\
    }\n\
    }\n'
    return command

list_of_urls = [
    'http://127.0.0.1:54321/getStateInfo',
    'http://127.0.0.1:54322/getStateInfo',
    'http://127.0.0.1:54323/getStateInfo'
    ]
backend_list = [
    '127.0.0.1:54321',
    '127.0.0.1:54322',
    '127.0.0.1:54323'
]




for i in range(len(list_of_urls)):
    with open('daemon_' + str(i) + '.csv', 'a') as fp:
        fp.write("backend_ID,total_memory,available_memory,total_core,available_core,Queued task,threshold,estimated_time_to_be_available_again,Status,Memory usage,CPU usage\n")


while True:
    _start = time.time()
    response = []
    with ThreadPoolExecutor(max_workers=10) as pool:
        response = (list(pool.map(get_url,list_of_urls)))
    
    #total_requests_list = []
    backend_status_list = []
    pre_backend_status_list = []
    for i in response:
        if i == 'Stopped':
            print("stopped")
            break
        timestamp = i[1]
        #print(i[0])
        d = json.loads(i[0].decode('utf-8'))
        with open('daemon_'+ str(d['backend_ID'])  +'.csv', 'a') as fp:
            memory_usage = ((float(d['total_memory']) - float(d['available_memory']))/ float(d['total_memory']) ) * 100 
            cpu_usage = ((float(d['total_core']) - float(d['available_core']))/ float(d['total_core']) ) * 100 
            status = estimator(float(d['total_memory']), float(d['available_memory']), int(d['total_core']), int(d['available_core']), float(d['threshold']))
            backend_status_list.append(status)
            fp.write( str(timestamp) + "," + str(d['backend_ID']) + ',' + str(d['total_memory']) + ',' + str(d['available_memory']) + "," + \
            str(d['total_core']) + "," + str(d['available_core']) + ',' + str(d['queued_task']) + ','  + str(d['threshold']) + ',' \
             + str(d['estimated_time_to_be_available_again']) +  ',' + str(status) +  ',' + str(memory_usage) + ',' + str(cpu_usage) + "\n" )
    updateNow = 0
    print(backend_status_list)
    if sum(backend_status_list) == 0:
        backend_status_list = [1,1,1]
    if backend_status_list != pre_backend_status_list and 1:
        updateNow = 1
        f = open('nginx_edge.conf', 'w')
        _config = writeConfg(backend_list, backend_status_list)
        f.write(_config)
        f.close()
        time.sleep(0.1)
        subprocess.run("nginx -s reload -c '/home/malazad@unomaha.edu/Desktop/Cloud_project_2/new/nginx_edge.conf'", shell=True)
        #time.sleep(10)
        print('Updating.....')




