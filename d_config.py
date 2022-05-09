import os


def writeConfg(backend_list, backend_status_list):

    command = 'user www-data;\n\
    user www-data;\n\
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
    }\n'


    return command


backend_list = [
    '127.0.0.1:54321',
    '127.0.0.1:54322',
    '127.0.0.1:54323'
]
backend_status_list = [0, 1, 1]

f = open('temp.conf', 'w')
_config = writeConfg(backend_list, backend_status_list)
f.write(_config)