from pypresence import Presence
import time
import datetime
client_id = '993442275533271050'  
RPC = Presence(client_id)  
RPC.connect() 

print(RPC.update(state = "Scanning for Vulnerabilities",start= datetime.datetime.now().timestamp()  ,large_image = "burp",large_text = "Scanning",small_image = "cover",small_text = "BurpSuite")) 
print("Running")
while True:  
    time.sleep(15) 