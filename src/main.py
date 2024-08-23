from azure.mgmt.network import NetworkManagementClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
network_client = NetworkManagementClient(credential, "your-subscription-id")

def list_firewall_rules(resource_group_name, firewall_name):
    firewall = network_client.azure_firewalls.get(resource_group_name, firewall_name)
    for rule in firewall.firewall_policy_rule_collection_groups:
        print(rule.name)

if __name__ == "__main__":
    list_firewall_rules("your-resource-group", "your-firewall-name")
