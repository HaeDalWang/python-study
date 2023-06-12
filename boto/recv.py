import boto3
import random
import time

# Create SQS client
sqs = boto3.client('sqs')

# Get the queue. This returns an SQS.Queue instance
queue_url = "https://sqs.ap-northeast-2.amazonaws.com/863422182520/test"

while True:
    response = sqs.receive_message(QueueUrl=queue_url)
    # 있으면 처리 아니면 또 돌려
    if 'Messages' in response:
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']
        print('Hello: %s' % message['Body'])
        sqs.delete_message(QueueUrl=queue_url,ReceiptHandle=receipt_handle)
    # 15 ~ 30초
    set = random.randrange(15,30)
    # 멈춰
    print ("Sleep " + str(set) + " seconds")
    time.sleep(set)
    # 다시
    print("wake up!")