#! /bin/bash

python /home/ubuntu/python/file.py
sudo ansible-playbook /home/ubuntu/python/hosts.yml
sudo chown ubuntu:ubuntu /home/ubuntu/python/inventory
cat /home/ubuntu/python/output.txt >> /home/ubuntu/python/inventory
