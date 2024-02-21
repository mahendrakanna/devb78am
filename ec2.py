import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# List all EC2 instances
response = ec2.describe_instances()

# Print the IDs of all EC2 instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'])