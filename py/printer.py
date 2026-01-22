import os

def write_out(f,Jobs_seen: str= "", job_title:str= "", location:str= "", job_id:str= "", url:str= ""):
    f.write(f"\nJob {Jobs_seen}: Title:{job_title.strip() if job_title else 'N/A'}\nLocation:{location.strip() if location else 'N/A'}\nID:{job_id.strip() if job_id else 'N/A'}\nURL:{url if url else 'N/A'}")
    return


def print_out(Jobs_seen: str= "", job_title:str= "", location:str= "", job_id:str= "",url:str= ""):
    print(f"\nJob {Jobs_seen}: Title:{job_title.strip() if job_title else 'N/A'}\nLocation:{location.strip() if location else 'N/A'}\nID:{job_id.strip() if job_id else 'N/A'}\nURL:{url if url else 'N/A'}")
    return