import aws_cdk as core
import aws_cdk.assertions as assertions

from my_ecs_construct.my_ecs_construct_stack import MyEcsConstructStack

# example tests. To run these tests, uncomment this file along with the example
# resource in my_ecs_construct/my_ecs_construct_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MyEcsConstructStack(app, "my-ecs-construct")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
