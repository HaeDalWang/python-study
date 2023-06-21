import argparse
import boto3

parser = argparse.ArgumentParser()
parser.add_argument("--instance-id", help="instance-id")
args = parser.parse_args()
instance_id = args.instance_id

client = boto3.client('ec2')
