#!/usr/bin/python3

import sys,json,requests,subprocess

answer = requests.post("http://localhost:5279", json={"method": "get", "params": {"uri": sys.argv[1]}}).json()
URL = answer["result"]["streaming_url"]
print("Streaming URL:\n",URL )
print("Playing with mpv...\n")
subprocess.run(["mpv", URL])
 

