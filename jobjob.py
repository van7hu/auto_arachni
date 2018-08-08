import subprocess, os, sys
from time import sleep

# 10 jobs is recommended for 4G of RAM
#subprocess.check_output('ps aux | grep "\-\-output\-verbose" | wc -l', stdout=subprocess.PIPE)

def get_job_count():
    me = subprocess.check_output(['ps aux | grep "\-\-output\-verbose" | wc -l'], shell=True)
    me = int(me.replace("\n", ""))

    return me

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

urls = []

for line in lines:
    urls.append(line.replace("\n", ""))

for url in urls:
    while True:
        if get_job_count() < 10:
            command = "./arachni --output-verbose --checks=* " + url + " --report-save-path=./report/" + url.replace(":", "_").replace("/", "_") + ".afr &"
            print "Executing command: " + command
            os.system(command)
            sleep(1)
            break
        else:
            sleep(5)
