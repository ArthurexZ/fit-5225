import json
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

# Delete an image
def lambda_handler(event, context):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('ass2-image-tags')  
        s3 = boto3.resource('s3')

        try:
            body = json.loads(event['body'])
            image_key = body.get('s3url')
            table.delete_item(Key={"s3-url" : image_key})
            responseS3 = s3.Object('image-trigger', image_key).delete()
            x = 'sucess'
            return {
                'statusCode': 200,
                'body': json.dumps(x)

            }
   
        except ClientError as e:
            print(e)
            return e
