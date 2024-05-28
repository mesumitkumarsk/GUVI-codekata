def handle_http_method(method, payload=None):
    if method == "GET":
        print("Requested resource data")
    elif method == "POST":
        print(f"Resource created successfully: {payload}")
    elif method == "PUT":
        print(f"Resource updated successfully: {payload}")
    elif method == "DELETE":
        print("Resource deleted successfully")
    else:
        print("Invalid HTTP method")

# Input
http_method = input()
payload = None
if http_method in ["POST", "PUT"]:
    payload = input()

# Output
handle_http_method(http_method, payload)