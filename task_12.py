# 12. Implement a function that checks if a string is a valid URL.

from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result  = urlparse(url)     # result is an object which save url scheme i.e httpor https and its netlock that is domain and path etc
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

url_to_check = "https://www.example.com"

if is_valid_url(url_to_check):
    print(f"{url_to_check} is valid")
else:
    print(f"{url_to_check} is not valid")






# from urllib.parse import urlparse

# def is_valid_url(url):
#     try:
#         result = urlparse(url)
#         return all([result.scheme, result.netloc])
#     except ValueError:
#         return False

# # Example usage:
# url_to_check = "https://www.example.com"
# if is_valid_url(url_to_check):
#     print(f"{url_to_check} is a valid URL.")
# else:
#     print(f"{url_to_check} is not a valid URL.")
