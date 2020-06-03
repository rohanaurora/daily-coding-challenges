# Defanging an IP Address
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".
#
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
#
# Source: https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address):
        add_list = list(address)
        for i, value in enumerate(add_list):
            if value == ".":
                add_list[i] = "[.]"
        return "".join(add_list)
        # return ''.join('[.]' if c == '.' else c for c in address)


s = Solution()
defanged_ip = s.defangIPaddr("255.100.50.0")
print(defanged_ip)