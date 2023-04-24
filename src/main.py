def shorten_url(full_url):
  url_hash = "123456"  
  return f"https://shorturl.com/{url_hash}"

input_url = input("Enter a URL: ")
short_url = shorten_url(input_url)
print("Shortened URL: " + short_url)