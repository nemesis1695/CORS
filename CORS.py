import requests

def check_cors_policy(url):
    # Set the Origin header to simulate a cross-origin request
    origin = 'https://www.example.com'  # Replace with your website's domain
    headers = {
        'Origin': origin,
    }
    
    # Send an OPTIONS request to the given URL with the Origin header
    response = requests.options(url, headers=headers)

    # Check if Access-Control-Allow-Origin header is present in the response
    if 'Access-Control-Allow-Origin' in response.headers:
        allowed_origin = response.headers['Access-Control-Allow-Origin']
        if allowed_origin == '*' or allowed_origin == origin or allowed_origin == 'null':
            print("CORS vulnerability found!")
            print(f"Access-Control-Allow-Origin header allows requests from any origin or '{origin}'.")
            print("Consider limiting it to specific origins to improve security.")
        else:
            print("No CORS vulnerability found.")
    else:
        print("No CORS vulnerability found.")

    # Check if Access-Control-Allow-Methods header is present in the response
    if 'Access-Control-Allow-Methods' in response.headers:
        allowed_methods = response.headers['Access-Control-Allow-Methods']
        print(f"Allowed HTTP methods: {allowed_methods}")

    # Check if Access-Control-Allow-Headers header is present in the response
    if 'Access-Control-Allow-Headers' in response.headers:
        allowed_headers = response.headers['Access-Control-Allow-Headers']
        print(f"Allowed HTTP headers: {allowed_headers}")

    # Check if Access-Control-Max-Age header is present in the response
    if 'Access-Control-Max-Age' in response.headers:
        max_age = response.headers['Access-Control-Max-Age']
        print(f"Max Age: {max_age}")

    # Check if Access-Control-Expose-Headers header is present in the response
    if 'Access-Control-Expose-Headers' in response.headers:
        exposed_headers = response.headers['Access-Control-Expose-Headers']
        print(f"Exposed HTTP headers: {exposed_headers}")

    # Check if Access-Control-Allow-Credentials header is present in the response
    if 'Access-Control-Allow-Credentials' in response.headers:
        allow_credentials = response.headers['Access-Control-Allow-Credentials']
        print(f"Allow credentials: {allow_credentials}")

    # Check if Access-Control-Allow-Methods is properly configured
    if 'Access-Control-Allow-Methods' in response.headers:
        allowed_methods = response.headers['Access-Control-Allow-Methods']
        if 'GET' not in allowed_methods or 'POST' not in allowed_methods or 'OPTIONS' not in allowed_methods:
            print("CORS vulnerability found!")
            print("Access-Control-Allow-Methods header does not allow required HTTP methods (GET, POST, OPTIONS).")
            print("Consider updating it to include these methods for proper CORS configuration.")
        else:
            print("No CORS vulnerability found.")

    # Check if Access-Control-Allow-Headers is properly configured
    if 'Access-Control-Allow-Headers' in response.headers:
        allowed_headers = response.headers['Access-Control-Allow-Headers']
        if 'Origin' not in allowed_headers or 'Content-Type' not in allowed_headers:
            print("CORS vulnerability found!")
            print("Access-Control-Allow-Headers header does not allow required HTTP headers (Origin, Content-Type).")
            print("Consider updating it to include these headers for proper CORS configuration.")
        else:
            print("No CORS vulnerability found.")

    # Check if Access-Control-Expose-Headers is properly configured
    if 'Access-Control-Expose-Headers' in response.headers:
        exposed_headers = response.headers['Access-Control-Expose-Headers']
        print(f"Exposed HTTP headers: {exposed_headers}")

    # Check if Access-Control-Max-Age is properly configured
    if 'Access-Control-Max-Age' in response.headers:
        max_age = response.headers['Access-Control-Max-Age']
        print(f"Max Age: {max_age} seconds")

    # Check if Access-Control-Allow-Credentials is properly configured
    if 'Access-Control-Allow-Credentials' in response.headers:
        allow_credentials = response.headers['Access-Control-Allow-Credentials']
        if allow_credentials.lower() == 'true':
            print("Access-Control-Allow-Credentials is enabled.")
        else:
            print("Access-Control-Allow-Credentials is disabled.")

# Example usage
url = 'https://example.com'
check_cors_policy(url)
