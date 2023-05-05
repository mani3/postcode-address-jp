#!/usr/bin/env python3
import os

import aws_cdk as cdk

from postcode_address_jp.postcode_address_jp_stack import \
    PostcodeAddressJpStack

app = cdk.App()
PostcodeAddressJpStack(
  app, "PostcodeAddressJpStack",
  env=cdk.Environment(region='ap-northeast-1'),
)

app.synth()
