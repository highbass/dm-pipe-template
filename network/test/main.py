import unittest
import yaml
from .. import main


AUTOCREATE_ENABLED_YAML = '''
env:
    name: test
properties:
    auto-create-subnets: true
'''

AUTOCREATE_DISABLED_YAML = '''
env:
    name: test
properties:
    auto-create-subnets: false
    network-range: '192.168.0.0/16'
    projects:
      -
        name: test-proj
        subnets:
          - region: 'us-central1'
            cidr: '192.168.1.0/24'
          - region: 'us-west1'
            cidr: '10.0.2.0/24'
'''

#### testing output

EXPECTED_OUTPUT_ENABLED = {
    'resources': [{
        'name': 'test'
        'type': 'compute.v1.subnetwork',
        'properties': {
          'privateIpGoogleAccess': True,
          'region': 'us-east1',
          'ipCidrRange': '10.116.0.0/21',
          'network': '$(ref.core-1.selfLink)'
          }
        }, {
        'type': 'compute.v1.subnetwork',
        'name': 'core-1-us-east1-pcf-2-ert',
        'properties': {
          'privateIpGoogleAccess': True,
          'region': 'us-east1',
          'ipCidrRange': '10.116.48.0/22',
          'network': '$(ref.core-1.selfLink)'
          }
    }]
}

EXPECTED_OUTPUT_DISABLED = {
    'resources': [{
        'type': 'compute.v1.subnetwork',
        'name': 'core-1-us-east1-core',
        'properties': {
          'privateIpGoogleAccess': True,
          'region': 'us-east1',
          'ipCidrRange': '10.116.0.0/21',
          'network': '$(ref.core-1.selfLink)'
          }
        }, {
        'type': 'compute.v1.subnetwork',
        'name': 'core-1-us-east1-pcf-2-ert',
        'properties': {
          'privateIpGoogleAccess': True,
          'region': 'us-east1',
          'ipCidrRange': '10.116.48.0/22',
          'network': '$(ref.core-1.selfLink)'
          }
    }]
}


class TestNetworkTemplates(unittest.TestCase):
    def test_happy_generate_config(self):
        """
            Happy path for generate config
        """
        yaml_input = yaml.load(MOCK_YAML)
        yaml_with_dot_notation = common.dotdict(yaml_input)
        generate_config_return = subnets_template.generate_config(yaml_with_dot_notation)
        self.assertEquals(generate_config_return, EXPECTED_OUTPUT)
