# import re
# import sys


# def main():
#     print(validate(input("IPv4 Address: ")))


# def validate(ip):
#     matches = re.search(r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$', ip)
#     try:
#         if 0 <= int(matches.group(1)) <= 255 and 0 <= int(matches.group(2)) <= 255 and 0 <= int(matches.group(3)) <= 255 and 0 <= int(matches.group(4)) <= 255:
#             return True
#     except (ValueError, AttributeError):
#         return False
#     return False


# if __name__ == "__main__":
#     main()

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ips = ip.split('.')
    if len(ips) != 4:
        return False
    for ip in ips:
        try:
            if int(ip) < 0 or int(ip) > 255:
                return False
        except ValueError:
            return False
    return True


if __name__ == "__main__":
    main()
