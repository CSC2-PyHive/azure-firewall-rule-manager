import unittest
from src.main import list_firewall_rules

class TestFirewallRules(unittest.TestCase):
    def test_list_firewall_rules(self):
        # You can mock Azure responses here
        # For now, just checking if the function runs without errors
        try:
            list_firewall_rules("test-group", "test-firewall")
        except Exception as e:
            self.fail(f"list_firewall_rules raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
