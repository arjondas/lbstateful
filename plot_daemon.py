import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import numpy as np
from matplotlib.pyplot import step, show, plot

#plt.style.use('fivethirtyeight')
previous_time = 0
number_of_backend = 3
metrics = ['Memory usage', 'CPU usage', 'Queued task', 'Status']
Max_limit = 41000
stop = False
previous_len = 0
#with open('ideal_task_rate.csv', 'a') as fp:
#        fp.write("ideal_task_rate\n")
def subplotgrid(n):
    root = math.ceil(math.sqrt(n))
    if (root -1 ) * root >= n:
        rows = root - 1
        return root-1,root
    else:
        return root,root

def anime(i):
    global stop, Max_limit, previous_len
    plt.clf()
    count = 0
    for _m in range(len(metrics)):
        plt.subplot(rows, columns, _m + 1)
        if metrics[_m] == 'Memory usage':
            title = 'Required Memory'
        elif metrics[_m] == 'CPU usage':
            title = 'Required CPU'
        else:
            title = metrics[_m]

        plt.gca().set_title(title)
        completed = 0
        ideal_task_rate = 0
        for _backend in range(number_of_backend):
            data = pd.read_csv('daemon_'+ str(_backend) +'.csv')
            metrics_list = data[metrics[_m]]
            if metrics[_m] == 'Status':
                
                x = []
                for _ in data[metrics[_m]]:
                    x.append(_ + count)
                    #print(metrics[_m] + '   :   ' + str(_backend) + str(x))
                step(np.arange(0,len(data[metrics[_m]]),1), x, label= "Backend : " + str(_backend))
                plt.yticks([])
                count += 2
            else:
                metrics_list_len = []
                for _ in range(len(metrics_list)):
                    metrics_list_len.append(_)
                
                plt.plot(metrics_list_len, metrics_list, label= "Backend : " + str(_backend))
            '''
            if metrics[_m] == "task_rate":
                #print(type(list(data["task_rate"])))
                #print(list(data["task_rate"])[-1])
                for _ in range(len(metrics_list)):
                    ideal_task_rate = ideal_task_rate + list(data["task_rate"])[_]
            '''
            #quequed_task_len.append(len(quequed_task))
            #data2 = pd.read_csv('users/result.csv')

            
            #print("len : " + str( len(quequed_task_len)))
            #print("queqe : " + str(len(quequed_task)))
            #plt.subplot(rows, columns, _backend + 1)
            
            #plt.plot(metrics_list_len, metrics_list, label= "Backend : " + str(_backend))
            #plt.plot(quequed_task_len, reused, label= "reused")
        if metrics[_m] == "task_rate":
            #ideal_task_rate_list.append(ideal_task_rate/number_of_backend)
            None
            #with open('ideal_task_rate.csv', 'a') as fp:
            #    fp.write(str(ideal_task_rate/number_of_backend) + "\n")
            '''
            data2 = pd.read_csv('ideal_task_rate.csv')
            
            print(metrics_list_len)
            print(data2["ideal_task_rate"])
            plt.plot(metrics_list_len, data2["ideal_task_rate"], label= "ideal")
            '''
        #plt.legend(loc='upper left')
        plt.legend(loc='best')
        plt.tight_layout()

rows,columns = subplotgrid(len(metrics))
fig = FuncAnimation(plt.gcf(),anime,interval = 1000)
plt.tight_layout()
plt.show()
