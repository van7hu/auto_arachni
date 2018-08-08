import os, time

counter = 0
while(1):
    counter = counter + 1
    print "Counter: " + str(counter)
 
    command = 'ps aux | grep "\-\-output\-verbose" | wc -l'
    print "Number of job(s) - not so accuracy :D "
    os.system(command)

    command = 'ls report/ | wc -l'
    print "Number of report generated :D "
    os.system(command)

    time.sleep(10)

    print "----------------"
