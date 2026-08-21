import requests
try: 
    response = requests.get( 
        "https://api.github.com/repos/kubernetes/kubernetes/pulls", timeout=5 
        ) 
    response.raise_for_status() 
    data = response.json() 
    print(f"Total PRs: {len(data)}") 
except requests.exceptions.Timeout: 
    print("API request timed out.") 
except requests.exceptions.RequestException as error: 
    print(f"API request failed: {error}") 
finally: print("API operation completed.")