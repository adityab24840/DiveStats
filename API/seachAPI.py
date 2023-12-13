import requests
from bs4 import BeautifulSoup

# Prompt user for input
first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")

# Define the URL
url = 'https://secure.meetcontrol.com/divemeets/system/memberlist.php'

# Make a request to the website
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the search input fields and submit button
    first_name_input = soup.find('input', {'id': 'first'})
    last_name_input = soup.find('input', {'id': 'last'})
    search_button = soup.find('input', {'id': 'search'})

    # Check if the elements are found
    if first_name_input and last_name_input and search_button:
        # Extract the value of the 'name' attribute from the input fields
        first_name_input_name = first_name_input.get('name')
        last_name_input_name = last_name_input.get('name')

        # Prompt the user for input (only once)
        first_name_value = input(f"Enter the value for '{first_name_input_name}': ")
        last_name_value = input(f"Enter the value for '{last_name_input_name}': ")

        # Submit the form
        form_data = {
            first_name_input_name: first_name_value,
            last_name_input_name: last_name_value,
            'Search': 'Search'  # The value of the submit button
        }

        # Make a POST request to submit the form
        response = requests.post(url, headers=headers, data=form_data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the search results page
            search_results_soup = BeautifulSoup(response.text, 'html.parser')

            # Extract and print the search results
            results = search_results_soup.find_all('div', {'class': 'showresults'})
            for result in results:
                print(result.text)
        else:
            print(f"Failed to retrieve search results. Status code: {response.status_code}")
    else:
        print("Failed to find the search input fields and submit button.")
else:
    print(f"Failed to retrieve the initial page. Status code: {response.status_code}")
