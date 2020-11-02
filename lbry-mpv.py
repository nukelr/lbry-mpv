import sys,json,requests,subprocess

def main():
	answer = requests.post("http://localhost:5279", json={"method": "get", "params": {"uri": sys.argv[1]}}).json()
	stream_type=answer["result"]["metadata"]["stream_type"]
	
	if stream_type != "video":
		sys.exit("Not a video file, exiting...")
	
	URL = answer["result"]["streaming_url"]
	print("Streaming URL:",URL )
	if "metadata" in answer["result"]:
		if "description" in answer["result"]["metadata"]:
			description=answer["result"]["metadata"]["description"]
			print("\nVideo description:\n",description, "\n")
	print("Playing with mpv...\n")
	subprocess.run(["mpv", URL])
 

if __name__=="__main__":
    main()


