import sys
import requests
import json
import os
import ruamel.yaml

# Initial thingies
yaml = ruamel.yaml.YAML(typ='rt')
yaml.default_style = False
yaml.preserve_quotes = True

# run ngrok on port 3000 in background using  "ngrok http 3000 &"
os.popen("ngrok http 3000 &")
print("ngrok has been started")

# Get the url public url from ngrok
tunnels = os.popen(f"ngrok api tunnels list").read()
j = json.loads(tunnels)
tunnel_url = j["tunnels"][0]["public_url"]
print(f"\n\n{tunnel_url =}")

# remove the https:// part from the url
public_url = tunnel_url.split('/')[-1]
print(f"public url is {public_url}")

# add ngrok url to beef.http.public.host
print("opening config.yaml")
with open('beef/config.yaml', 'r') as f:
    config = yaml.load(f)

print("setting public host to ngrok public url")
config['beef']['http']['public']['host'] = str(public_url)

print(f"{config['beef']['http']['public']['host'] = }")

with open('beef/config.yaml', 'w') as f:
    # write changes to config.yaml
    print("writing changes")
    yaml.dump(config, f)

# Start beef
print("starting beef")
try:
    os.system("cd beef && ./beef")
    print(f'example url: {tunnel_url}/demos/basic.html')

except KeyboardInterrupt:
    print('stopping ngrok')
    os.system("pkill 'ngrok'")
    sys.exit(0)
