#!/usr/bin/env python
"""Gcloud deploy manager template script to create network"""
from common import default

def GenerateConfig(context):
    """Creates the network with environment variables."""
    if context.properties['autoCreateSubnetworks']:
        vpc = [{
                'name': context.properties['name'],
                'type': default.NETWORK,
                'properties': {
                    'autoCreateSubnetworks': context.properties['autoCreateSubnetworks'],
                    'description': context.properties['description']
                }
            }]
    else:
        # we are just adding the ipCidrRange with custom subnet is requested to be provisioned
        vpc = [{
                'name': context.properties['name'],
                'type': default.NETWORK,
                'properties': {
                    'ipCidrRange': context.properties['ipCidrRange'],
                    'autoCreateSubnetworks': context.properties['autoCreateSubnetworks'],
                    'description': context.properties['description']
                }
            }]
    return {'resources': vpc}
