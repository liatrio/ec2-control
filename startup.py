import boto3
from functools import reduce

client = boto3.client('ec2', region_name='us-west-2',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_ACCESS_KEY_ID)

response = client.describe_instances()
instances = reduce(lambda a,b:a+b['Instances'], response['Reservations'], [])

#get all the instances tagged with 'Uptime = daily'
daily_startup_instances = list(filter(lambda instance: {'Key':'Uptime', 'Value':'daily'} in instance['Tags'], instances))
#reduce the list to only stopped instances
daily_startup_instances = list(filter(lambda instance: {'Code': 80, 'Name': 'stopped'} == instance['State'], daily_startup_instances))

daily_startup_instance_ids = [i['InstanceId'] for i in daily_startup_instances]

if not daily_startup_instance_ids:
	print('No instances to start')
else:
  client.start_instances(InstanceIds=daily_startup_instance_ids)
