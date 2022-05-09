import os, sys
import shutil
import time
import subprocess
import random
from flask import Flask
from flask import send_file, request




total_memory = 0
total_core = 0
quequed_task = 0
available_memory = 0
available_core = 0
estimated_time_to_be_available_again = 0
threshold = 0.1
Backend_ID = 0
'''
service_detail = {
    "service1":(100,2,30),
    "service2":(500,5,90),
    "service3":(50,5,10)
}
'''

app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>this is a demo .onion for research purpose only!</h1>"



@app.route('/service/<req_memory>/<req_core>/<req_time>', methods=['POST', 'GET'])
def service(req_memory, req_core, req_time):
    #subprocess.run("clear")
    #print("here 1")
    global service_detail, total_memory, total_core, task_queue_size, available_memory, \
    available_core, estimated_time_to_be_available_again, threshold, quequed_task
    _service_required_memory = int(req_memory)
    _service_required_core = int(req_core)
    _service_required_time = int(req_time)
    #print("here 2")

    #_service_required_memory = random.randint(100, 5000)
    #_service_required_core = random.randint(1, 5)
    #_service_required_time = random.randint(10, 100)
    #print("required memory : " + str(_service_required_memory) + ' core : ' + str(_service_required_core) + " time : " + str(_service_required_time))
    final_response = ""
    if available_memory < _service_required_memory or available_core < _service_required_core:
        final_response = "Task execution was failed."
    else:
        final_response = "Task has been executed properly."
    available_memory = available_memory - _service_required_memory
    available_core = available_core - _service_required_core
    quequed_task += 1
    #print("available memory : " + str(available_memory))
    #print("available core : " + str(available_core))
    time.sleep(_service_required_time)
    quequed_task -= 1
    available_memory = available_memory + _service_required_memory
    available_core = available_core + _service_required_core
    
    
    return final_response



@app.route('/getStateInfo')
def getStateInfo():
    #subprocess.run("clear")
    global Backend_ID, available_memory, available_core, total_memonry, total_core, quequed_task, threshold, estimated_time_to_be_available_again
    response = "{\"backend_ID\":\"" + str(Backend_ID) + "\",\"total_memory\":\"" + str(total_memory) + "\",\"available_memory\":\"" + str(available_memory) + \
    "\",\"total_core\":\"" + str(total_core) + "\",\"available_core\":\"" + str(available_core) + "\",\"queued_task\":\"" + str(quequed_task) +\
    "\",\"threshold\":\"" + str(threshold) + "\", \"estimated_time_to_be_available_again\":\"" + str(estimated_time_to_be_available_again) + "\"}"
    return response




@app.route('/hello')
def hello_world():
   return "<h1>Hello world!!!</h1>"

@app.route('/spoof/<ip>/<gaurd_ip>/<gaurd_port>')
def tor_download(ip, gaurd_ip, gaurd_port):
    global spoofed_ip, dst_ip, dst_port
    spoofed_ip = ip
    dst_ip = gaurd_ip
    dst_port = int(gaurd_port)
    print("spoofed ip = " + str(spoofed_ip))
    print("Dst IP = " + str(dst_ip))
    print("Dst Port = " + str(dst_port))
    return str(src_port)

@app.route('/startspoofing/')
def startSpoof():
    time.sleep(1)
    print('starting spoofing')
    print("src ip = " + spoofed_ip + " src port = " + str(src_port) + ' port type = ' + str(type(src_port)))
    print("dst ip = " + dst_ip + ' dst port = ' + str(dst_port) + ' port type = ' + str(type(dst_port)))

    fp = open("example1.file", 'rb')
    input = fp.read()
    splitLen = 1024
    obj = AES.new('1234567890123456', AES.MODE_CBC, 'This is an IV456')
    start = time.time()
    count = 0
    ss = conf.L3socket()
    #payload = input[0:20]
    #spoofed_packet = (IP(src=spoofed_ip, dst=dst_ip) / UDP(sport=src_port, dport=dst_port) / payload)
    #payload2 = spoofed_packet['payload']
    for lines in range(0, len(input), splitLen):
        
        b = hex(count)
        #print()
        payload = obj.encrypt(bytes(b[:2] + (16-len(b)) * "0" + b[2:], encoding='utf-8') + input[lines:lines+splitLen])
        #print(payload[:16])
        elapsed1 = time.time()
        spoofed_packet = IP(src=spoofed_ip, dst=dst_ip) / UDP(sport=src_port, dport=dst_port) / payload
        
        ss.send(spoofed_packet)
        count += 1
        end1 = time.time()
        elapsed2 = time.time()
        payload = input[lines:lines+splitLen]
        end2 = time.time()
        #time.sleep(0.0008)

        print("count = " + str(count) + ' elapsed1 time = ' + str(end1 - elapsed1) + 's 2 = ' + str(end2 - elapsed2) + 's')
    payload = b'EOF'
    spoofed_packet = IP(src=spoofed_ip, dst=dst_ip) / UDP(sport=src_port, dport=dst_port) / payload
    ss.send(spoofed_packet)
    payload = b'EOF'
    spoofed_packet = IP(src=spoofed_ip, dst=dst_ip) / UDP(sport=src_port, dport=dst_port) / payload
    ss.send(spoofed_packet)
    payload = b'EOF'
    spoofed_packet = IP(src=spoofed_ip, dst=dst_ip) / UDP(sport=src_port, dport=dst_port) / payload
    ss.send(spoofed_packet)
    print("sending done!!!" + str(time.time() - start) + 's')
    return 'ok'


@app.route('/download', methods=['POST', 'GET'])
def download():
    return send_file('example.file', attachment_filename='example.file')




if __name__ == '__main__':
    total_memory = 64000
    total_core = 20
    task_queue_size = 0
    available_memory = total_memory
    available_core = total_core
    estimated_time_to_be_available_again = 0
    app.run(port=54321, debug= False, threaded=True)
