import sys,json,requests,subprocess

def main():
	answer = requests.post("http://localhost:5279", json={"method": "get", "params": {"uri": sys.argv[1]}}).json()
	URL = answer["result"]["streaming_url"]
	print("Streaming URL:\n",URL )
	print("Playing with mpv...\n")
	subprocess.run(["mpv", URL])
 
if __name__=="__main__":
    main()

