from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda as lambda_,
    aws_lambda_python_alpha as lambda_python,
)
from constructs import Construct


class LambdaPythonPerformanceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_python.PythonFunction(
            self,
            "Say Hi",
            entry="./src/functions/without_layer",
            index="query_star_trek_characters.py",
            runtime=lambda_.Runtime.PYTHON_3_10,
        )

        lambda_python.PythonFunction(
            self,
            "Say Hi with Layer",
            entry="./src/functions/with_layer",
            index="query_star_trek_characters.py",
            runtime=lambda_.Runtime.PYTHON_3_10,
            layers=[
                lambda_python.PythonLayerVersion(
                    self,
                    "PoetryLayer",
                    entry="./src/layer",
                    compatible_runtimes=[lambda_.Runtime.PYTHON_3_10],
                )
            ],
        )

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "LambdaPythonPerformanceQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
