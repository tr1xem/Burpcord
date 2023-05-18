import Burpcord.rpc as rpc
import time

print("Demo for python-discord-rpc")
client_id = '993442275533271050' #Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) #Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = time.time()
while True:
    activity = {
            "state": "Scanning for Vulnerabilities",
            "details": "",
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "",
                "small_image": "cover",
                "large_text": "",
                "large_image": "burp"
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(30)