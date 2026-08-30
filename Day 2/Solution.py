import re

# Saare rules ek list mein hain
RULES = [
    {
        "family": "Linux",
        "name": "Ubuntu",
        "match": r"ubuntu",
        "ver_regex": r"(\d+(?:[\._]\d+)*)"
    },
    {
        "family": "Windows",
        "name": "Windows Server",
        "match": r"(?:windows|win)",
        "ver_regex": r"(\d{4})"
    },
    {
        "family": "Linux",
        "name": "Red Hat Enterprise Linux",
        "match": r"(?:rhel|red\s*hat|redhat)",
        "ver_regex": r"(\d+(?:[\._]\d+)*)"
    }
]

def normalize_os(raw_text):
    text = raw_text.lower()
    for rule in RULES:
        if re.search(rule["match"], text):
            ver = re.search(rule["ver_regex"], text)
            clean_ver = ver.group(1).replace("_", ".") if ver else "Unknown"
            return {
                "os_family": rule["family"],
                "os_name": rule["name"],
                "os_version": clean_ver
            }

    return {"os_family": "Unknown", "os_name": "Unknown", "os_version": "Unknown"}


# --- Example Test Run ---
if __name__ == "__main__":
    os_list = [
        "Ubuntu 22.04",
        "ubuntu_22.04",
        "Ubuntu Linux 22.04 LTS",
        "Windows_Server_2022",
        "Microsoft Windows Server 2022",
        "win_2022",
        "RHEL-9.3",
        "RedHat Enterprise Linux 9.3"
    ]

    for os in os_list:
        print(f"{os:<32} -> {normalize_os(os)}")
