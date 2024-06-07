#! /usr/bin/env python3

from flask import Flask, request, jsonify

app = Flask(__name__)

WHITE_IP = '192.168.xxx.xxx'
WHITE_MAC = 'XX:XX:XX:XX:XX:XX'
CAM_URL = 'http://SOMETHIng:8081/'

def big_mac(ip):
    try:
        pid = subprocess.Popen(["arp", "-n", ip], stdout=subprocess.PIPE)
        s = pid.communicate()[0].decode('utf-8')
        for line in s.split('\n'):
            if ip in line:
                mac = line.split()[2]
            else:
                mac = None
    except Exception as e:
        print(f'Error finding mac address: {e}')
        mac = None
    return mac

@app.route('/catch', methods=['POST'])
def door_status():
    data = request.get_json()
    status = data.get("status")
    timestamp = data.get("timestamp")
    print(f"Received status: {status} at {timestamp}")
    if str(status) == 'OPEN':
        # Save clip of stream
        try:
            subprocess.run(["timeout","8","curl", "{CAM_URL}", "-o", f"{timestamp}.mp4"], check=True)
        except Exception as e:
            print(f'Error saving video: {e}')
    return jsonify({"message": "Status received"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1312)
