from http.server import HTTPServer, BaseHTTPRequestHandler
import psutil
import json
# print("cpu", psutil.cpu_percent())
def metrics():
    metrics_dict = {}
    temp= psutil.sensors_temperatures().get("coretemp")[0]
    metrics_dict.update({"cpu_temp:":  str(temp.current)+'/'+str(temp.high)})
    # print("cpu_temp",temp.current ,"/", temp.high )

    hdd = psutil.disk_usage('/srv/dev-disk-by-uuid-57607a6a-f579-43cf-8ab3-f07467566ae6')
    metrics_dict.update({"storage": [int(hdd.free / (2**30)),int(hdd.used / (2**30)),int( hdd.total / (2**30))]})
    # print ("Total:  GiB" ,int( hdd.total / (2**30)))
    # print ("Used: GiB" , int(hdd.used / (2**30)))
    # print ("Free: GiB" , int(hdd.free / (2**30)))
    metrics_dict.update({"ram_usage":psutil.virtual_memory().percent})
    # print("ram-", psutil.virtual_memory().percent)
    metrics_dict.update({"la":psutil.getloadavg( )})
    #print("la - ",psutil.getloadavg( ))
    return metrics_dict

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):


    # определяем метод `do_GET`
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")

        self.end_headers()
        self.wfile.write(bytes(str(metrics()), 'utf-8'))#b'Hello, world!')


httpd = HTTPServer(('your_ip', 8009), SimpleHTTPRequestHandler)
httpd.serve_forever()
# print(type(str(metrics())),"\n", str(metrics()))
