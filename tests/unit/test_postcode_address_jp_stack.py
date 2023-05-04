import aws_cdk as core
import aws_cdk.assertions as assertions

from postcode_address_jp.postcode_address_jp_stack import PostcodeAddressJpStack

# example tests. To run these tests, uncomment this file along with the example
# resource in postcode_address_jp/postcode_address_jp_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PostcodeAddressJpStack(app, "postcode-address-jp")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
