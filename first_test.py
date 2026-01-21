import os  
from dotenv import load_dotenv
load_dotenv()
website = os.getenv("website")
from playwright.sync_api import sync_playwright
def test_example(website: str = ""):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(website)
        
        page.wait_for_load_state("networkidle")

        # Find all job listing items (li elements with class css-1q2dra3)
        job_items = page.locator("li.css-1q2dra3").all()
        print(f"Found {len(job_items)} job listings")
 #       print(page.getByText('JOBS FOUND'))
        for i, job in enumerate(job_items):
            # Extract job title
            job_title = job.locator("a[data-automation-id='jobTitle']").text_content()
            
            # Extract location
            location = job.locator("dd.css-129m7dg").first.text_content()
            
            # Extract job ID from subtitle
            job_id = job.locator("li.css-h2nt8k").text_content()
            
            print(f"\nJob {i+1}:")
            print(f"  Title: {job_title.strip() if job_title else 'N/A'}")
            print(f"  Location: {location.strip() if location else 'N/A'}")
            print(f"  ID: {job_id.strip() if job_id else 'N/A'}")
           
            # # Check if next button is enabled
            # next_button = page.locator("button[data-uxi-element-id='next']")
            
            # # If next button is disabled, we've reached the end
            # if next_button.get_attribute("aria-disabled") == "true" or next_button.is_disabled():
            #     print("\n✓ Reached the last page!")
            #     break
            
            # # Click next button
            # print("\n→ Moving to next page...")
            # next_button.click()
            # page.wait_for_load_state("networkidle")
    
        #print(f"\n✓ Total jobs processed: {job_count}")
        # Wait for keyboard input before closing
        input("\nPress Enter to close the browser...")
        browser.close()

if __name__ == "__main__":
    test_example(website)