from serverless_notification import lambda_handler
import pytest



event = {
        "sqs_name": "your-name-queue",
        "activity_arn": "arn:aws:states:us-west-2:281782457076:activity:serverless_issue_fire_command",
        "cannon_3_charge_status": "successful",
        "cannon_1_charge_status": "successful",
        "travel_distance": 86,
        "cannon_2_charge_status": "successful",
        "planet_name": "Corellia",
        "sns_arn": "arn:aws:sns:us-west-2:281782457076:jiravani-notification",
        "message": {
            "message_context": "planet_name",
            "message_payload": "congratulations, you are now the ultimate power in the universe."
        },
        "commander": {
        	"name": "<REPLACE ME>",
        	"rank": "<REPLACE ME>"
        }
    }
def test_answer():
    del event['message']

    with pytest.raises(ValueError):
         lambda_handler(event,{})

    # assert lambda_handler(event, {}) == 0
