# Qualification checker
import os
from dotenv import load_dotenv
load_dotenv()
def check_qualifications(job_description)-> bool:
    blacklist = os.getenv("blacklist").split(",")
    for term in blacklist:
        if term.lower() in job_description.lower():
            return False
    return True

def url_builder(href: str) -> str:
    base_url = os.getenv("website").split("/",3)[:3]
    base_url = "/".join(base_url)
    full_url = base_url + href
    return full_url