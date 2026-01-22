import os
import random
import time  
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from printer import print_out, write_out
load_dotenv()
website = os.getenv("website")


def web_core(website: str = ""):
    Jobs_seen = 0
    with sync_playwright() as p:
        f = open("first_test.log", "w")
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(website)
        page.wait_for_load_state("networkidle")
        while True:
            job_items = page.locator("li", has=page.locator("a[data-automation-id='jobTitle']")).all()
            for i, job in enumerate(job_items):
                job_title = job.locator("a[data-automation-id='jobTitle']").text_content()
                location = job.locator("div[data-automation-id='locations'] dd").text_content()
                job_id = job.locator("ul[data-automation-id='subtitle'] li").text_content()
                job.locator("a[data-automation-id='jobTitle']").click()
                page.wait_for_selector("div[data-automation-id='jobPostingDescription']", timeout=5000)
                job_description = job.locator("div[data-automation-id='jobPostingDescription']").text_content()
                print(job_description)
                Jobs_seen = Jobs_seen + 1
                print_out(Jobs_seen, job_title, location, job_id)
                write_out(f,Jobs_seen, job_title, location, job_id)
                time.sleep(random.uniform(1, 2))  # Random sleep between 2 to 4 seconds
            next_button = page.locator("button[data-uxi-element-id='next']")
            if next_button.get_attribute("aria-disabled") == "true" or next_button.is_disabled():
                print("\n✓ Reached the last page!")
                break
            print("\n→ Moving to next page...")
            next_button.click()
            page.wait_for_load_state("networkidle")
            time.sleep(random.uniform(2, 4))  # Random sleep between 2 to 4 seconds
        input("\nPress Enter to close the browser...")
        browser.close()
        f.close()
    return