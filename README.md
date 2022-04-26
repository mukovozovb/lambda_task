# lambda_task
Lambda function can create, delete or decribe instance.
How to run it
- Create aws lambda function with Runtime Python
- Give IAM policy to run/delete/describe EC2 instance
- Put code from file lambda.py to aws lambda

If you invoke lambda from the CLI use next format:
```
aws lambda invoke --function-name test --payload {\"action\":\"delete\"} --cli-binary-format raw-in-base64-out output.json
```
The value of the payload depends on what the lamda will do:
- "create" = create instance
- "delete" = delete instance
- "describe" = describe instance
