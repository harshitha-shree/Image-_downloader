import requests

def download_image(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad status codes

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"Image successfully downloaded and saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download image: {e}")

# Example usage
image_url = "https://example.com/image.jpg"
save_path = "downloaded_image.jpg"
download_image(image_url, save_path)
