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
        if get_job_count() < 2:
            command = "./arachni --output-verbose --checks=* --http-user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' " + url + " --report-save-path=./report/" + url.replace(":", "_").replace("/", "_") + ".afr &"
            print "Executing command: " + command
            os.system(command)
            sleep(2)
            break
        else:
            sleep(5)
