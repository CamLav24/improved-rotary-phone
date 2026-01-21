import os

def write_out(f,Jobs_seen: str= "", job_title:str= "", location:str= "", job_id:str= ""):
    f.write(f"\nJob {Jobs_seen}:")
    f.write(f"  Title: {job_title.strip() if job_title else 'N/A'}")
    f.write(f"  Location: {location.strip() if location else 'N/A'}")
    f.write(f"  ID: {job_id.strip() if job_id else 'N/A'}")
    return


def print_out(Jobs_seen: str= "", job_title:str= "", location:str= "", job_id:str= ""):
    print(f"\nJob {Jobs_seen}:")
    print(f"  Title: {job_title.strip() if job_title else 'N/A'}")
    print(f"  Location: {location.strip() if location else 'N/A'}")
    print(f"  ID: {job_id.strip() if job_id else 'N/A'}")
    return