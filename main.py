websites = (
    "https://google.com",
    "airbnb.com",
    "https://facebook.com",
    "twitter.com",
    "tiktok.com"
)

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
print(websites)