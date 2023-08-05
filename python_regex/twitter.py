import re
# re.split(pattern, string, maxsplit=, flags=0)
# re.findall(pattern, string, flags=0)

url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")
# username = url.removeprefix('https://twitter.com/') ## from python 3.9+

# re.sub(pattern, repl, string, count=0, flags=0)
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# username = re.sub(r"^(http|https)://twitter\.com/", "", url)

# print(f"username: {username}")


# matches = re.search(r'^https?://(www\.)?twitter\.com/(.+)$', url, re.IGNORECASE)
# matches = re.search(r'^https?://(?:www\.)?twitter\.com/(.+)$', url, re.IGNORECASE)
matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
if matches:
    print(f"username: ", matches.group(1))