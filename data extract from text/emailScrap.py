import re
import collections
import json



with open('websiteData.txt','r', encoding='UTF-8') as f:
    contents = f.read()
    mail_id = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",contents)
    elements_count = collections.Counter(mail_id)

    robot = 0
    man = 0
    email_info = {}
    for key, value in elements_count.items():
        if len(key) > 8:
            if re.match(r'^\D+.\D+@(gmail|email).com$',key):
                email_info[key] ={
                    "Occurance":value,
                    "EmailType":"Human"
                }
            else:
                email_info[key] ={
                    "Occurance":value,
                    "EmailType":"Non-Human"
                }
        else:
            email_info[key] ={
                "Occurance":value,
                "EmailType":"Non-Human"
            }


    file = open("result.json",'w')
    json.dump(email_info,file)
    print(email_info)