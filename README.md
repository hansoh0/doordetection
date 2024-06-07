
# doordetection

Client/server app where client notifies the server of the status of a door (open/closed) and captures video footage for 8 seconds depending on the status created by @hansoh0 (https://www.github.com/hansoh0)


## Installation

Install requirements with pip

```
client_server:~$ pip install -r client_require.txt
```

```
host_server:~$ pip install -r server_require.txt
```
## How to Use
Both processes should be started on bootup, this can be done by creating a service for each of the respective scripts and enabling them
### Client
```
client_server:~$ sudo vi /etc/systemd/system/door_detection.service
```
```
[Unit]                                                                                                                                        
Description=Door detection script (client side)
After=networking.target
                
[Service]               
User=client                
ExecStart=/usr/bin/python3 /home/client/app/client.py
                                                                                                                                                           
[Install]                
WantedBy=multi-user.target
```
```
client_server:~$ sudo systemctl daemon-reload
client_server:~$ sudo systemctl enable door_detection.service
client_server:~$ sudo systemctl start door_detection.service
```
### Host
```
host_server:~$ sudo vi /etc/systemd/system/door_detection.service
```
```
[Unit]                                                                                                                                        
Description=Door detection script (server side)
After=networking.target
                
[Service]               
User=client                
ExecStart=/usr/bin/python3 /home/host/app/server.py
                                                                                                                                                        
[Install]                
WantedBy=multi-user.target
```
```
host_server:~$ sudo systemctl daemon-reload
host_server:~$ sudo systemctl enable door_detection.service
host_server:~$ sudo systemctl start door_detection.service
```
This will not work if the reed switch is not connected to pin 40 on the raspberry pi or unless you change the pin mapping within the client.py file.

RPIZ GPIO Map: (https://github.com/hansoh0/doordetection/assets/48212912/1b718b2f-521c-4daa-b838-8339ba4e10ef)

