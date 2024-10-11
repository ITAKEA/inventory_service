import requests

def fetch_product_details(product_id):
    response = requests.get(f'http://localhost:5000/products/{product_id}')
    if response.status_code == 200:
        return response.json()
    return None