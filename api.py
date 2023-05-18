from pypresence import Presence
import time

client_id = '993442275533271050'  
RPC = Presence(client_id)  
RPC.connect() 

print(RPC.update(state = "Scanning for Vulnerabilities",large_image = "burp",large_text = "Scanning",small_image = "cover",small_text = "Burp Suite",))  

while True:  
    time.sleep(15) 