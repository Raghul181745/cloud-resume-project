import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-counter') # Replace with your actual table name if different

def lambda_handler(event, context):
    # Update the visitor count
    response = table.update_item(
        Key={'id': 'visitor'},
        UpdateExpression='ADD #c :inc',
        ExpressionAttributeNames={'#c': 'count'},
        ExpressionAttributeValues={':inc': 1},
        ReturnValues='UPDATED_NEW'
    )
    
    # Return the updated count
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": "*", # Required for frontend fetch
        },
        'body': json.dumps({'visits': int(response['Attributes']['count'])})
    }
