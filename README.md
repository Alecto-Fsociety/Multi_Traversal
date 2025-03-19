# 🚀 Multi Traversal

Multi Traversal is a high-speed, multi-threaded tool for performing **directory traversal** on a target URL, identifying accessible paths. It is fully independent of external dependencies and optimized for efficient security testing.

---

```
    __  ___      ____  _    ______                                      __
   /  |/  /_  __/ / /_(_)  /_  __/________ __   _____  ______________ _/ /
  / /|_/ / / / / / __/ /    / / / ___/ __ `/ | / / _ \/ ___/ ___/ __ `/ / 
 / /  / / /_/ / / /_/ /    / / / /  / /_/ /| |/ /  __/ /  (__  ) /_/ / /  
/_/  /_/\__,_/_/\__/_/    /_/ /_/   \__,_/ |___/\___/_/  /____/\__,_/_/   


```

---

## **🔧 Features**
👉 Supports **HTTP & HTTPS** requests 🚀  
👉 Multi-threaded execution for high-speed scanning ⚡  
👉 Randomized **User-Agent** selection for stealth 🎭  
👉 **Automatic logging** of scanned paths 📂  
👉 No external dependencies required ❌  
👉 Supports custom **status code detection** (`-s 403,500`) 🔍  

---

## **🚀 Usage**
### **🔹 Basic Execution**
```bash
python3 multi_traversal.py -url "https://example.com" -w wordlist.txt
```

### **🔹 Available Options**
| Option | Description |
|--------|-------------|
| `-url` | **(Required)** Target URL for scanning (e.g., `https://example.com`) |
| `-w` | **(Required)** Wordlist file path (e.g., `directories.txt`) |
| `-s` | *(Optional)* Comma-separated HTTP status codes to detect (default: `200,301,302`) |
| `-p` | *(Optional)* Custom port number (default: `80/443`) |
| `-t` | *(Optional)* Number of threads (default: `4`, recommended: `4-10`) |

---

## **📂 Logging**
👉 **Checked Paths** are stored in `Checked_Dir_Paths/`  
👉 **Error Logs** are stored in `Checked_Err_Dir/`  
👉 Log files are named based on the scan timestamp  

---

## **💡 Examples**
### **🔹 Standard Traversal Scan**
```bash
python3 multi_traversal.py -url "https://target.com" -w wordlist.txt
```

### **🔹 Scan with Custom Status Codes**
```bash
python3 multi_traversal.py -url "https://target.com" -w wordlist.txt -s 403,500
```

### **🔹 Scan on Custom Port 8080**
```bash
python3 multi_traversal.py -url "https://target.com" -w wordlist.txt -p 8080
```

---

## **⚠️ Disclaimer**
🚨 This tool is intended **for security research and testing only**.  
⚖️ **Unauthorized testing on third-party systems is illegal** and may result in legal consequences.  

> **The developer assumes no liability for the misuse of this tool.**

---

## **🐝 License**
This project is licensed under the **[MIT License](https://github.com/Alecto-Fsociety/Alecto-Fsociety/blob/main/LICENSE)**.  
You are free to use and modify it, but must comply with the license terms when using it for commercial purposes.

---

## **🌍 Contributing**
💡 **Bug reports, feature requests, and pull requests are welcome!** 🚀  
Feel free to open an issue or submit a pull request on GitHub.  

---

## **👥 Contact**
📌 Developer: **[Alecto-Fsociety](https://github.com/Alecto-Fsociety)**  
📌 GitHub: **[https://github.com/Alecto-Fsociety/Multi-Traversal](https://github.com/Alecto-Fsociety/Multi-Traversal)**  
📧 Proton Mail: goodbye_friend1111@proton.me

