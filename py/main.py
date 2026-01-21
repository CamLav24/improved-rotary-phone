#main code
#!/usr/bin/env python3
import os
import random
import time
from dotenv import load_dotenv

import py.web_core as web_core 

if __name__ == "__main__":
    load_dotenv()
    website = os.getenv("website")
    web_core.web_core(website)  