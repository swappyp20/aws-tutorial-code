"""
-*- coding: utf-8 -*-
========================
AWS Lambda
========================
Contributor: Swapnil Pawar
========================
"""
def lambda_handler(event, context):
    #this will print the payload from the source function if supplied
    print(event)
    return "Thanks"
