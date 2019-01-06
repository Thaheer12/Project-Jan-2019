import subprocess
with open("output.txt", "w+") as output:
    subprocess.call(["python", "/home/ubuntu/python/ip.py"], stdout=output);
