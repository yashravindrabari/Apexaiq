import re


class OSNormalizer:

    def __init__(self):
        self.rules = {
            "ubuntu": ("Linux", "Ubuntu"),
            "windows": ("Windows", "Windows Server"),
            "win": ("Windows", "Windows Server"),
            "rhel": ("Linux", "Red Hat"),
            "redhat": ("Linux", "Red Hat")
        }

    def normalize(self, text):
        text = text.lower()

        for key, (family, name) in self.rules.items():
            if key in text:
                version = re.search(r"\d+(?:\.\d+)?", text)

                return {
                    "os_family": family,
                    "os_name": name,
                    "os_version": version.group() if version else "Unknown"
                }

        return {
            "os_family": "Unknown",
            "os_name": "Unknown",
            "os_version": "Unknown"
        }

    def add_rule(self, key, family, name):
        self.rules[key] = (family, name)


# Test
os_list = [
    "Ubuntu 22.04",
    "Windows_Server_2022",
    "RHEL-9.3"
]

normalizer = OSNormalizer()

for os in os_list:
    print(normalizer.normalize(os))
