#!/usr/bin/python3

import boto3
from functools import reduce

client = boto3.client('ec2', region_name='us-west-2',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

response = client.describe_instances()
instances = reduce(lambda a,b:a+b['Instances'], response['Reservations'], [])
non_critical_instances = list(filter(lambda instance: {'Key':'Uptime', 'Value':'critical'} not in instance['Tags'], instances))
non_critical_instances = list(filter(lambda instance: {'Code': 16, 'Name': 'running'} == instance['State'], non_critical_instances))

non_critical_instance_ids = [i['InstanceId'] for i in non_critical_instances]

if not non_critical_instance_ids:
  print('No instances need to be stopped')
else:  
  client.stop_instances(InstanceIds=non_critical_instance_ids)
