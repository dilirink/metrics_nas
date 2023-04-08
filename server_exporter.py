from http.server import HTTPServer, BaseHTTPRequestHandler
import psutil
import json
import time
# print("cpu", psutil.cpu_percent())
def metrics():
    metrics_dict = {}
    temp= psutil.sensors_temperatures().get("coretemp")[0]
    metrics_dict.update({"cpu_temp_current:":  str(temp.current)})
    metrics_dict.update({"cpu_temp_high:":  str(temp.high)})
    # print("cpu_temp",temp.current ,"/", temp.high )

    hdd = psutil.disk_usage('/srv/dev-disk-by-uuid-57607a6a-f579-43cf-8ab3-f07467566ae6')
    # metrics_dict.update({"storage": [int(hdd.free / (2**30)),int(hdd.used / (2**30)),int( hdd.total / (2**30))]})
    metrics_dict.update({"storage_total": int( hdd.total / (2**30))})
    metrics_dict.update({"storage_free": int(hdd.free / (2**30))})

    # print ("Total:  GiB" ,int( hdd.total / (2**30)))
    # print ("Used: GiB" , int(hdd.used / (2**30)))
    # print ("Free: GiB" , int(hdd.free / (2**30)))
    metrics_dict.update({"ram_usage":psutil.virtual_memory().percent})
    # print("ram-", psutil.virtual_memory().percent)
    la= psutil.getloadavg( )
    metrics_dict.update({"la_5":la[0]})
    metrics_dict.update({"la_10":la[1]})
    metrics_dict.update({"la_15":la[2]})
    #print("la - ",psutil.getloadavg( ))
    # metrics_dict.update({"cpu_percent":psutil.cpu_percent(interval=0.5)})
    
    # net_stat=psutil.net_io_counters(pernic=True, nowrap=True)["enp1s0"]
    # net_in_1 = net_stat.bytes_recv
    # net_out_1 = net_stat.bytes_sent
    # time.sleep(1)
    # net_stat = psutil.net_io_counters(pernic=True, nowrap=True)["enp1s0"]
    # net_in_2 = net_stat.bytes_recv
    # net_out_2 = net_stat.bytes_sent

    # net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 3)
    # net_out = round((net_out_2 - net_out_1) / 1024 / 1024, 3)
    # print(f"Current net-usage:\nIN: {net_in} MB/s, OUT: {net_out} MB/s")
    # metrics_dict.update({"net_speed":str(str(net_in)+"/"+str(net_out))})
    
    return metrics_dict

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):


    # определяем метод `do_GET`
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")

        self.end_headers()
        self.wfile.write(bytes(str(metrics()), 'utf-8'))#b'Hello, world!')


httpd = HTTPServer(('192.168.50.45', 8009), SimpleHTTPRequestHandler)
httpd.serve_forever()
# print(type(str(metrics())),"\n", str(metrics()))
