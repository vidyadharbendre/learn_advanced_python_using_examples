import requests

url = 'https://download.library.lol/main/27000/f3aa83fb7adab9c8675871a717db6231/%28McGraw-Hill%20series%20in%20computer%20science%29%20Tom%20M.%20Mitchell%20-%20Machine%20Learning-McGraw-Hill%20%281997%29.djvu'


try:
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Success! Resource found.")
        with open('downloaded_file.ext', 'wb') as f:
            f.write(response.content)
        print("File downloaded successfully.")
    elif response.status_code == 404:
        print("Error: Resource not found.")
    else:
        print(f"Failed to retrieve the file. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
