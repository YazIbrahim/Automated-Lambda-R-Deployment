from aws_cdk import (
    aws_lambda as _lambda,
    Stack
)
from constructs import Construct

class AwsLambdaContainerCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        function = _lambda.DockerImageFunction(self, "Simple_R_Lambda_Function",
                                    code=_lambda.DockerImageCode.from_image_asset("./assets"))