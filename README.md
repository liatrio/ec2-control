# ec2-control
python scripts to be called by runback to manage ec2 nodes


## Startup.py

Checks all ec2 nodes that are currently in a 'stopped' state for the 'Uptime = daily' tag. If the tag is found the instance is started. This is intended to run at 8 am weekdays, so the instance is running during work hours.


## Shutdown.py

Checks all ec2 nodes that are in a 'running' state for the 'Uptime = critical' tag. If the tag is **NOT** found, the instance is shutdown. This is intended to run at the end of every day, so that instances left un-tagged are shutdown

