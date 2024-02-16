import requests


# Function to search for images using the Unsplash API
def search_and_get_image_url(query, access_key):
    url = f"https://api.unsplash.com/photos/random/?query={query}&client_id={access_key}&count=1"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        if data:
            image_url = data[0]['urls']['full']  # Extract URL of the first image
            return image_url
        else:
            print("No images found for the query:", query)
            return None
    except requests.RequestException as e:
        print("Error fetching image:", e)
        return None


if __name__ == "__main__":
    access_key = 'fZ2rZc6HMDHDUgSlvYm_4gj_xkLENBi8fZv7DbM0eg8'  # Replace with your Unsplash access key
    query = input("Enter your search query: ")
    image_url = search_and_get_image_url(query, access_key)
    if image_url:
        print("Image URL:", image_url)
