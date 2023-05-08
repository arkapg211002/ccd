import requests
import os
from bs4 import BeautifulSoup
# headers = {'Cookie': 'codechef_session=YOUR_CODECHEF_SESSION_COOKIE_VALUE'}

headers = {'Cookie': 'codechef_session=AP8dLtzP56CSW7EZ5KpiindGeb1vGe2a6-uuNGEqcM7koUHCaQKo71Qag9PEOpr63eqRv45y8-w'}

url = 'https://www.codechef.com/api/contests/PRACTICE/submissions?username=arka21102002&limit=300&offset=0'

response = requests.get(url, headers=headers)
data = response.json()

folder_name = "CodeChef Submissions"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

submissions = data['result']['data']

for submission in submissions:
    submission_id = submission['id']
    problem_code = submission['problemCode']
    submission_date = submission['date']
    solution_code = submission['program']
    
    # Create a file name for the submission
    file_name = f"{problem_code}_{submission_id}.cpp" # You can change the extension to any language you want

    # Create the full file path by joining the folder path and file name
    file_path = os.path.join(folder_name, file_name)

    # Save the solution code to the file
    with open(file_path, "w") as f:
        f.write(solution_code)
    
    print(f"Downloaded submission {submission_id} for problem {problem_code}")

url_template = 'https://www.codechef.com/api/contests/PRACTICE/submissions?username=arka21102002&limit=300&offset={}'

offset = 0
while True:
    url = url_template.format(offset)
    response = requests.get(url, headers=headers)






