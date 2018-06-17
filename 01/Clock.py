
import time

t = time.localtime(time.time())
year = int(t[0])
month = int(t[1])
day = int(t[2])

print (time.strftime("%Y/%m/%d-%H:%M:%S", t)) # output in format
print (year,month,day) # output by manually