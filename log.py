from datetime import datetime
from datetime import timezone

loggingEnabled = True
logFile = "output.log"

# Define 'log' function to redirect console output to a local file on operating system
# with timestamp for the local timezone.
def log(msg):
    dtNow = datetime.now(timezone.utc)
    time = dtNow.strftime("%Y-%m-%d_%H:%M:%S_{}+{}".format(dtNow.tzname(), dtNow.utcoffset()))
    timestamp = "[{}] ".format(time)

    if loggingEnabled:
        f = open(logFile, 'a')
        f.write(timestamp+msg+"\n")
        f.close()
        print(msg)
    else:
        print(msg)

print("Logging enabled: {}\n".format(loggingEnabled))

testString = "Hello World! My name is Marcel, I hope you have a pleasant day! :)"

log(testString)
