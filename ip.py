import boto3
client = boto3.client('ec2')
response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Env',
            'Values': [
                'Dev',
            ]
        },
    ])

for x in response['Reservations']:
    for instance in x['Instances']:
        print(instance['PrivateIpAddress'])
