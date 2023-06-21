import boto3
import random
import time

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName='test')

# You can now access identifiers and attributes
print(queue.url)

while True:
    # 1 ~ 15초
    set = random.randrange(1,15)
    # 메시지 큐에 넣기
    response = queue.send_message(MessageBody='world')
    # 멈춰
    print ("Sleep " + str(set) + " seconds")
    time.sleep(set)
    # 다시
    print("wake up!")