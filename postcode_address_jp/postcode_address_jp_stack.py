from aws_cdk import Duration, Stack, aws_apigateway, aws_lambda
from constructs import Construct


class PostcodeAddressJpStack(Stack):

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    handler = aws_lambda.Function(
      self, 'MainHandler',
      runtime=aws_lambda.Runtime.PYTHON_3_8,
      code=aws_lambda.Code.from_asset('handler'),
      handler='main.handler',
      environment={},
      timeout=Duration.seconds(30),
      memory_size=1024,
    )

    api = aws_apigateway.RestApi(self, 'postcode-address-jp-api')
    postal_code_integration = aws_apigateway.LambdaIntegration(handler)
    postal_code_resource = api.root.add_resource('postal_code').add_resource('{postal_code}')
    postal_code_resource.add_method('GET', postal_code_integration)
