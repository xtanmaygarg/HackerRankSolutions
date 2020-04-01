import re
[print('Valid') if re.match(r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}$', input()) else print('Invalid') for _ in range(int(input()))]
