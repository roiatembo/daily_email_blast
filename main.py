from datetime import date, timedelta, datetime
import requests, math
from smtplib import SMTP
from bs4 import BeautifulSoup

study_date = input("Input date(yyyy-mm-dd) to print study material or type 't' for today: ")
file_name_input = input("Enter file name or press enter to use default: ")
if study_date == "t":
    today = date.today()
else:
    today = datetime.strptime(study_date, '%Y-%m-%d')

if len(file_name_input) >1 :
    file_name = file_name_input
else:
    file_name = "study_material"

formatted_date = today.strftime("%A %d %B %Y")

study_material = open(f"/home/roia/Videos/Tutorials/{file_name}.txt", "w")
summary = "Study Material for " + formatted_date + "\n"
study_plans = ["c_program_study_plan.txt", "web_dev_study_plan.txt", "linux_study_plan.txt", "algorithms_study_plan.txt"]
course_names = ["C Programming", "Web Development", "Linux Course", "Algorithms in C"]
course = 0
todays_min = 0
for plan in study_plans:
    with open(plan, "r") as file:
        lines = file.readlines()
        try:
            todays_index = lines.index(f"{formatted_date}\n")
            sliced_list = lines[todays_index::]
            end_of_day = sliced_list.index("\n")
            todays_list = sliced_list[:end_of_day]
        except ValueError:
            todays_list = ["no material for today\n"]
    
    study_material.write(course_names[course] + "\n\n")
    if len(todays_list) > 1:
        total_minutes = int(todays_list[1].split()[6])
        todays_min += total_minutes
        for i in range(1,len(todays_list)):
            study_material.write(todays_list[i])
    else:
        study_material.write(todays_list[0])
    study_material.write("\n")
    course += 1

study_material.close()

with open(f"/home/roia/Videos/Tutorials/{file_name}.txt", 'r+') as f:
        hours = math.floor(todays_min / 60)
        minutes = todays_min % 60
        content = f.read()
        line = f"Study time for today is {hours} hours {minutes} minutes"
        f.seek(0, 0)
        f.write(summary + line.rstrip('\r\n\n') + '\n' + content)




# url_date = today + timedelta(days=1)
# search_date = url_date.strftime("%Y/%-m/%-d")
# URL = f"https://wol.jw.org/en/wol/h/r1/lp-e/{search_date}"


# response = requests.get(URL)
# website_html = response.text

# soup = BeautifulSoup(website_html, "html.parser")

# scripture = soup.find(name="p", class_="themeScrp").getText()
# context = soup.find(name="p", class_="sb").getText()

# sender = 'roia@theitmogul.co.za'
# receivers = ['roiatembo@gmail.com']

# message = f"""From: Python App <python@theitmogul.co.za>
# To: Roia <roia@theitmogul.co.za>
# MIME-Version: 1.0
# Content-type: text/html
# Subject: A look at today

# <h1>A bit of spirituality first</h1>
# <h5>{scripture}</h5>
# <p>{context}</p>

# <h1>Study Material for today</h1>
# """
# print(message)
# with SMTP(host="mail.theitmogul.co.za", port=465) as smtp:
#     smtp.login(user="roia@theitmogul.co.za", password="temboLAND.44")
#     smtp.sendmail(from_addr=sender, to_addrs=receivers, msg=message)
#     smtp.quit()
