from time import sleep, time
from dashing import *
import math
from os import system
from datetime import datetime
import os
import blessed
import requests
import json
ui = VSplit(
	HSplit(
		Text(text=None, border_color=2,),  # ui.items[0].items[0]


	),
	HSplit(
		VSplit(

			HSplit(
				# ui.items[1].items[0].items[0].items[0]
				HGauge(title="cpu_temp", label="43°C", val=43, border_color=5),
				# ui.items[1].items[0].items[0].items[1]
				HGauge(title="storage(0.91TB)", label="250GB",
					   val=100, border_color=1, color=1),
			),
			VSplit(
				HSplit(
					#ui.items[1].items[0].items[1].items[0].items[0]
					HGauge(
						title="ram_usage(8GB)", label="45%", val=45, border_color=1, color=3,), 
					# ui.items[1].items[0].items[1].items[0].items[0]
					Text(
						title="la", text="          1.3/0.4/0.3", border_color=1, color=2),
				),
			)

		),

	)
)


r1 = {
	"1":
		"    \u2588\u2588",
		"2":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"3":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"4":
		"\u2588\u2588  \u2588\u2588",
		"5":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"6":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"7":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"8":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"9":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"0":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		":":
		"      "
}
r2 = {
	"1":
		"    \u2588\u2588",
		"2":
		"    \u2588\u2588",
		"3":
		"    \u2588\u2588",
		"4":
		"\u2588\u2588  \u2588\u2588",
		"5":
		"\u2588\u2588    ",
		"6":
		"\u2588\u2588    ",
		"7":
		"    \u2588\u2588",
		"8":
		"\u2588\u2588  \u2588\u2588",
		"9":
		"\u2588\u2588  \u2588\u2588",
		"0":
		"\u2588\u2588  \u2588\u2588",
		":":
		"  \u2588\u2588  "
}

r3 = {
	"1":
		"    \u2588\u2588",
		"2":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"3":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"4":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"5":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"6":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"7":
		"    \u2588\u2588",
		"8":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"9":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"0":
		"\u2588\u2588  \u2588\u2588",
		":":
		"      "
}

r4 = {
	"1":
		"    \u2588\u2588",
		"2":
		"\u2588\u2588    ",
		"3":
		"    \u2588\u2588",
		"4":
		"    \u2588\u2588",
		"5":
		"    \u2588\u2588",
		"6":
		"\u2588\u2588  \u2588\u2588",
		"7":
		"    \u2588\u2588",
		"8":
		"\u2588\u2588  \u2588\u2588",
		"9":
		"    \u2588\u2588",
		"0":
		"\u2588\u2588  \u2588\u2588",
		":":
		"  \u2588\u2588  "
}

r5 = {
	"1":
		"    \u2588\u2588",
		"2":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"3":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"4":
		"    \u2588\u2588",
		"5":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"6":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"7":
		"    \u2588\u2588",
		"8":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"9":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		"0":
		"\u2588\u2588\u2588\u2588\u2588\u2588",
		":":
		"      "
}


def times():
	ctime = datetime.now()
	hour = str(ctime.hour)
	minute = str(ctime.minute)
	second = str(ctime.second)
	if (len(hour) < 2):
		hour = "0"+hour
	if (len(minute) < 2):
		minute = "0"+minute
	if (len(second) < 2):
		second = "0"+second
	times = (
		"   \x1B[37m"+r1[hour[0]]+" "+r1[hour[1]]+r1[':']+r1[minute[0]]+" "+r1[minute[1]]+r1[':']+r1[second[0]]+" "+r1[second[1]] + "\x1B[0m\n" +
		"   \x1B[37m"+r2[hour[0]]+" "+r2[hour[1]]+r2[':']+r2[minute[0]]+" "+r2[minute[1]]+r2[':']+r2[second[0]]+" "+r2[second[1]] + "\x1B[0m\n" +
		"   \x1B[37m"+r3[hour[0]]+" "+r3[hour[1]]+r3[':']+r3[minute[0]]+" "+r3[minute[1]]+r3[':']+r3[second[0]]+" "+r3[second[1]] + "\x1B[0m\n" +
		"   \x1B[37m"+r4[hour[0]]+" "+r4[hour[1]]+r4[':']+r4[minute[0]]+" "+r4[minute[1]]+r4[':']+r4[second[0]]+" "+r4[second[1]] + "\x1B[0m\n" +
		"   \x1B[37m"+r5[hour[0]]+" "+r5[hour[1]]+r5[':']+r5[minute[0]]+" " +
		r5[minute[1]]+r5[':']+r5[second[0]]+" "+r5[second[1]] + "\x1B[0m\n"
		# "                     \x1B[31m date: "+ str(ctime.day)+"."+str(ctime.month)+"."+str(ctime.year)
	)
	return times


def main(term):
	timeS=ui.items[0].items[0]
	cpuTEMP = ui.items[1].items[0].items[0].items[0]
	stor = ui.items[1].items[0].items[0].items[1]
	ram =ui.items[1].items[0].items[1].items[0].items[0]
	la = ui.items[1].items[0].items[1].items[0].items[1]
	with term.cbreak(), term.hidden_cursor(), term.fullscreen():
		while True:
			met = load_metrics()
			ctime = datetime.now()
			timeS.text = times()  
			timeS.title = str(str(ctime.day)+"."+str(ctime.month)+"."+str(ctime.year))
			cpuTEMP.label = str(met["cpu_temp_current:"])+'°C'  # cpu_temp
			cpuTEMP.append( float(met["cpu_temp_current:"])*100/float(met["cpu_temp_high:"]) ) # cpu_temp
			stor.append((int(met["storage_total"] )-int(met["storage_free"]))*100/int(met["storage_total"] )) # storage
			ram.label="3"
			la.text = "4" # la
			ui.display()
			time.sleep(1)


def load_metrics():
	url = "http://192.168.50.45:8009"
	try:
		r = requests.get(url=url)
	except:
		return None

	t = r.text.replace("\'", "\"")
	data = json.loads(t)
	return data


def clear():
	system("cls")


if __name__ == "__main__":
	exit(main(blessed.Terminal()))
