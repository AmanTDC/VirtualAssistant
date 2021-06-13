import threading

def input1():
    for i in range(100):
        print(str(i)+'\n')

t1=threading.Thread(target=input1)

t1.start()
for d in ['a','b','c','d','e','f','g','h','i']:
    print(d)
import subprocess
proc = subprocess.Popen('cmd.exe', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
stdout, stderr = proc.communicate('dir c:\\')
stdout
