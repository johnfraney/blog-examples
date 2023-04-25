import aws_cdk as core
import aws_cdk.assertions as assertions

from lambda_python_performance.lambda_python_performance_stack import LambdaPythonPerformanceStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lambda_python_performance/lambda_python_performance_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LambdaPythonPerformanceStack(app, "lambda-python-performance")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
