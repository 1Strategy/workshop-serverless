import boto3
import json

training_role_arn = "arn:aws:iam::281782457076:role/1s_user_provisioning"
client = boto3.client('sts')
assumed_role_response = client.assume_role( RoleArn=training_role_arn,
                                            RoleSessionName="prod-lambda-trainingUserProvision")

training_creds = assumed_role_response["Credentials"]

sfn_client = boto3.client(  'stepfunctions',
                            aws_access_key_id=training_creds["AccessKeyId"],
                            aws_secret_access_key=training_creds["SecretAccessKey"],
                            aws_session_token=training_creds["SessionToken"])


def lambda_handler(event, context):

    if event['httpMethod'] == 'GET':
        return get_response(event)
    if event['httpMethod'] == 'POST':
        return post_response(event)
    return {
        "statusCode": 500,
        "headers":  {
                        'Access-Control-Allow-Origin': '*',
                        'Content-Type': 'text/html'
        },
        "body": "HTTP method Unsupported"
    }

def post_response(event):

    task_token = event['body']
    return_payload = {
        "statusCode": 200,
        "headers": {'Access-Control-Allow-Origin': '*', 'Content-Type': 'text/html'}
    }

    try:
        sfn_client.send_task_success(taskToken=task_token, output="{}")
    except Exception as e:
        print(e)
        return_payload['body'] = "Firing Code Invalid!\n"
        return return_payload

    return_payload['body'] = "Firing Code Accepted!\n"
    return return_payload

def get_response(event):
    return {
        "statusCode": 200,
        "headers": {'Access-Control-Allow-Origin': '*', 'Content-Type': 'text/html'},
        "body": build_body(event)
    }


def build_body(event):
    url = '\'https://' + event['headers']['Host'] + '/prod'+event['resource']+"/\',"

    body = """<html>
            <body bgcolor=\"#E6E6FA\">
            <head>
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
            <script>

            $(document).ready(function(){
                $("button").click(function(){
                  var input = document.getElementById("input").value;
                  $.ajax({
                    type: 'POST',
                    headers: {
                    'Content-Type':'application/json'
                    },
                    url:"""

    body += url
    body +=         """
                    crossDomain: true,
                    data: input
                    dataType: 'json',
                    success: function(responseData) {

                    }
                    error: function (responseData) {
                        alert('POST failed.'+ JSON.stringify(responseData));
                    }
                  });
                });
            });
            </script>
            </head>
            <body>"""
    body += event['resource'][1:]
    body += """<form class="form" action="" method="post">
                    <textarea rows="4" cols="50" name="text" id="input" placeholder="Enter Firing Code"></textarea>
              </form>
            <button>Send Firing Code</button>



            </body>
            </html>"""
    return body
