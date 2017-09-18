"""Creates the Network Resource with VPC"""
from common import default

def GenerateConfig(context):
    """Creates the Compute Engine with network and firewall."""

    resources = []
    subnetwork_resources = []
    vpc = {
        'name': context.env['name'],
        'type': 'vpc.py',
        'properties': {
            'name': context.env['name'],
            'autoCreateSubnetworks': context.properties['auto-create-subnets'],
            'description': context.env['name']+ " vpc managed by deploymanager "
        }
    }
    if not (context.properties['auto-create-subnets']):
        vpc_additions = {
            'ipCidrRange': context.properties['network-range'],
        }
        # appends the network range
        vpc['properties'].update(vpc_additions)

        for project in context.properties['projects']:
            for subnet in project['subnets']:
                subnetname = context.env['name'] + "-" + subnet['region'] + "-" + project['name']
                subnetwork = {
                    'name': subnetname,
                    'type': 'subnetwork.py',
                    'properties': {
                        'name': subnetname,
                        'description': "PROJECT: " + project['name'] + " REGION: " + subnet['region'],
                        'ipCidrRange': subnet['cidr'],
                        'network': default.REFERENCE_PREFIX + context.env['name'] + default.SELF_LINK,
                        'region': subnet['region']
                    }
                }
                resources.append(subnetwork)

    resources.append(vpc)

    return { 'resources': resources }
