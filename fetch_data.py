import requests
import json
import csv
# Define the URL for the endpoint you want to access
url = "https://api.fillout.com/v1/api/forms/owxwseT6C3us/submissions"

# Define your API key
api_key = 'sk_prod_NAIQj0skzcLnFpj8DsuloKcdM5GJ4AaUB89TpVRE4HXWXNSMxwgXYGUgfKLWkVduszhNAOHofpAobKD0F9gT4ji4441EG7nIc9V_6893'

# Define headers with API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Send the GET request with headers
response = requests.get(url, headers=headers)

# Check the response status code
if response.status_code == 200:
    # Request was successful
    response_content = response.content.decode('utf-8')
    data = json.loads(response_content)
    print(data)  # Process the response data as needed
    with open('forms_data.json', 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
        print("JSON response saved to forms_data.json")
    column_headers = ["submissionId", "submissionTime", "lastUpdatedAt"] + [q["name"] for q in data["responses"][0]["questions"]]
    csv_data = []
    for row in data['responses']:
        row_values = [row["submissionId"], row["submissionTime"], row["lastUpdatedAt"]] + [q["value"][0] if isinstance(q["value"], list) else q["value"]  for q in row["questions"]]
        csv_data.append(dict(zip(column_headers, row_values)))

    # Define the CSV file name
    csv_file = "data_list.csv"

    # Write to CSV file
    try:
        with open(csv_file, 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=column_headers)
            writer.writeheader()
            writer.writerows(csv_data)
        print(f"Data saved to {csv_file}")
    except IOError:
        print("I/O error")
            
else:
    # Request failed
    print(f"Request failed with status code {response.status_code}")
    print(response.text)  # Print the error response

