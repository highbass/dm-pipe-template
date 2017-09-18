
"""
Default constants
"""

# Deploymen Manager constructs
REFERENCE_PREFIX = '$(ref.'
SELF_LINK = '.selfLink)'

# Resource type defaults names
ADDRESS = 'compute.v1.address'
AUTOSCALER = 'compute.v1.autoscaler'
BACKEND_SERVICE = 'compute.v1.backendService'
DISK = 'compute.v1.disk'
ENDPOINT = 'serviceregistry.v1alpha.endpoint'
FIREWALL = 'compute.v1.firewall'
GF_RULE = 'compute.v1.globalForwardingRule'
HEALTHCHECK = 'compute.v1.httpHealthCheck'
IGM = 'compute.v1.instanceGroupManager'
IAM_GROUP = 'clouduseraccounts.beta.group'
IAM_SERVICEACCOUNTT = 'iam.v1.serviceAccount'
IAM_SVCACT_KEY = 'iam.v1.serviceAccounts.key'
IAM_USER = 'clouduseraccounts.beta.user'
INSTANCE = 'compute.v1.instance'
NETWORK = 'compute.v1.network'
PROXY = 'compute.v1.targetHttpProxy'
SUBNETWORK = 'compute.v1.subnetwork'
TEMPLATE = 'compute.v1.instanceTemplate'
URL_MAP = 'compute.v1.urlMap'

# Regions and zones
REGION = {
    'us-east4': ['us-east-4-a', 'us-east4-b', 'us-east4-c'],
    'us-east1': ['us-east1-b', 'us-east1-c', 'us-east1-d']
}
