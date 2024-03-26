from test import get_content, get_status
import os
import schedule
import time
ntfy_channel_name = "Enter YOur nfty channel name"
def case(id:int):
    status = get_status(id)
    content = str(get_content(id))
    cmd = f"curl -d \"{status}\" ntfy.sh/{ntfy_channel_name}"
    os.system(cmd)
    cmd = f"curl -d \"{content}\" ntfy.sh/{ntfy_channel_name}" 
    os.system(cmd)

# case(enter you tracking id)