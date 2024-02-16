import requests
import json

base_url = 'https://mateserver.onrender.com/'


# Get all data from the server
def get_all_data():
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            try:
                data = response.json()
                print("All Data:", data)
            except json.JSONDecodeError:
                print("No data returned from the server")
        else:
            print("Failed to fetch data")
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)


# Add data to the server
def add_data(data):
    try:
        response = requests.post(base_url, json=data)
        if response.status_code == 201:
            print("Data added successfully")
        else:
            print("Failed to add data")
    except requests.exceptions.RequestException as e:
        print("Error adding data:", e)


# Update data on the server
def update_data(index, data):
    try:
        response = requests.put(f'{base_url}{index}', json=data)
        if response.status_code == 200:
            print("Data updated successfully")
        elif response.status_code == 404:
            print("Index not found")
        else:
            print("Failed to update data")
    except requests.exceptions.RequestException as e:
        print("Error updating data:", e)


# Delete data from the server
def delete_data(index):
    try:
        response = requests.delete(f'{base_url}{index}')
        if response.status_code == 200:
            print("Data deleted successfully")
        elif response.status_code == 404:
            print("Index not found")
        else:
            print("Failed to delete data")
    except requests.exceptions.RequestException as e:
        print("Error deleting data:", e)


def get_data_at_index(index):
    try:
        response = requests.get(f"{base_url}/{index}")
        if response.status_code == 200:
            data = response.json()
            print(f"Data at index {index}: {data}")
        else:
            print(f"No data found at index {index}")
    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    all_data = get_all_data()
    # print("All Data:", all_data)

    # Example data to add, update, and delete
    data_to_add = {'title': 'hello', 'image': 'https://delhiupdate.com/wp-content/uploads/2021/06/Technology-Bloggers-in-Delhi.jpg', 'para': 'hefrjfbjewbkfbjwbrhjbvjhbjht'}

    # data_to_update = {"name": "Jane", "age": 25}

    # Add data
    add_data(data_to_add)
    # get_all_data()  # Fetch all data to see the changes

    # # Update data
    # update_data('0', data_to_add)
    # get_all_data()  # Fetch all data to see the changes

    # Delete data
    # delete_data('12')

    # index_to_read = '12'
    # get_data_at_index(index_to_read)
    # get_all_data()  # Fetch all data to see the changes
