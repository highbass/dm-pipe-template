#!/usr/bin/env python
"""Gcloud deploy manager template script to create network"""
from common import default

def GenerateConfig(context):
  """Creates the network with environment variables."""
  subnetwork = [{
      'name': context.properties['name'],
      'type': default.SUBNETWORK,
      'properties': {
        'privateIpGoogleAccess': context.properties['privateIpGoogleAccess'],
        'description': context.properties['description'],
        'ipCidrRange': context.properties['ipCidrRange'],
        'network': context.properties['network'],
        'region': context.properties['region']
      }
  }]
  return {'resources': subnetwork}
