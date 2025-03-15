import ssl,socket,argparse,random,re,pathlib,sys,chardet,traceback,itertools as it
from urllib.parse import urlparse
from multiprocessing import Pool
from datetime import datetime 

banner = r"""
    __  ___      ____  _    ______                                      __
   /  |/  /_  __/ / /_(_)  /_  __/________ __   _____  ______________ _/ /
  / /|_/ / / / / / __/ /    / / / ___/ __ `/ | / / _ \/ ___/ ___/ __ `/ / 
 / /  / / /_/ / / /_/ /    / / / /  / /_/ /| |/ /  __/ /  (__  ) /_/ / /  
/_/  /_/\__,_/_/\__/_/    /_/ /_/   \__,_/ |___/\___/_/  /____/\__,_/_/   

by Alecto_Fsociety (https://github.com/Alecto-Fsociety)

"""

print(banner)

class Multi_Traversal:
    def __init__(self,target_url,path_name,port):
        self.target_url = target_url
        self.path_name = path_name

        self.base_url = urlparse(self.target_url)
        self.scheme = (self.base_url).scheme
        self.domain = (self.base_url).netloc

        self.ua_list = self.ua_lists()
        self.path_list = self.path_lists()

        self.port = port if port is not None else (443 if self.scheme == "https" else 80)  
        
        self.cycle = it.cycle(r"/-\|")

        self.date = datetime.now()

        self.status_list = {"200","301","302"}

        self.out_dir_name = "Checked_Dir_Paths"
        self.out_file = f"{self.date.year}_{self.date.month}-{self.date.day}_{self.date.hour}-{self.date.minute}_traversal.log"
        self.out_file_name = self.out_file
        self.err_dir_name = "Checked_Err_Dir"
        self.err_file_name = "err.log"

        self.err_tags = f"Error_{self.date.year}_{self.date.month}-{self.date.day}_{self.date.hour}-{self.date.minute}"

    def ua_lists(self,ua_path="ua.txt"):
        return [ua.strip("\n") for ua in open(ua_path,"r",encoding="utf-8").readlines()]

    def path_lists(self):
        return [path.strip("\n") for path in open(self.path_name,"r",encoding="utf-8").readlines()]

    def get_headers(self,path):
        return f"GET /{path} HTTP/1.1\r\nHost:{self.domain}\r\nUser-Agent:{random.choice(self.ua_list)}\r\nAccept:*/*\r\n\r\n"

    def checked_log(self,list_data=[]):
        try:
            lines = [line.strip("\n") for line in open(f"{self.out_dir_name}/{self.out_file_name}","r",encoding="utf-8").readlines()]
            for data in lines:
                if data and data not in list_data:
                    list_data.append(data)
            new_file_name = ((self.out_file_name).split(".")[0]) + "_checked.log"
            with open(f"{self.out_dir_name}/{new_file_name}","w+",encoding="utf-8")as save_files:
                [save_files.write(f"{data}\n") for data in list_data]

        except KeyboardInterrupt:
            pass
 
    def requests(self):
        pathlib.Path(self.out_dir_name).mkdir(exist_ok=True)
        lines = len(self.path_list)
        for point,path in enumerate(self.path_list,start=1):
            try:
                if self.scheme == "https":
                    with (ssl.create_default_context()).wrap_socket(
                            socket.create_connection((self.domain,self.port)),server_hostname=self.domain
                            )as ssock:
                        ssock.settimeout(1.5)
                        ssock.send(bytes(self.get_headers(path),"utf-8"))

                        response = ssock.recv(1024*10)

                        detected = chardet.detect(response)
                        encoding = detected["encoding"] if detected["encoding"] else "utf-8"

                        response_data = response.decode(encoding)

                        status_match = re.search(r"HTTP/\d\.\d (\d+)",response_data)
                        status = status_match.group(1) if status_match else "000"

                        sys.stdout.write(f"\r[*] Path_Traversal <{point}/{lines}> / {self.target_url}:{self.port} / [{next(self.cycle)}] {path}")
                        sys.stdout.flush()

                        if status in self.status_list:
                            with open(f"{self.out_dir_name}/{self.out_file_name}","a+",encoding="utf-8")as files:
                                files.write(f"[GET/{self.port}/{status}] {self.scheme}://{self.domain}/{path}\n")
                else:
                    with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as sock:
                        sock.settimeout(1.5)
                        sock.connect((self.domain,self.port))
                        sock.sendall(bytes(self.get_headers(path),"utf-8"))

                        response = sock.recv(1024*10)
                        
                        detected = chardet.detect(response)
                        encoding = detected["encoding"] if detected["encoding"] else "utf-8"

                        response_data = response.decode(encoding)

                        status_match = re.search(r"HTTP/\d\.\d (\d+)",response_data)
                        status = status_match.group(1) if status_match else "000"

                        sys.stdout.write(f"\r[*] Path_Traversal <{point}/{lines}> / {self.target_url}:{self.port} [{next(self.cycle)}] {path}")
                        sys.stdout.flush()

                        if status in self.status_list:
                            with open(f"{self.out_dir_name}/{self.out_file_name}","a+",encoding="utf-8")as files:
                                files.write(f"[GET/{self.port}/{status}] {self.scheme}://{self.domain}/{path}\n")
                
            except Exception as e:
                pathlib.Path(self.err_dir_name).mkdir(exist_ok=True)
                with open(f"{self.err_dir_name}/{self.err_file_name}","a+",encoding="utf-8")as err_files:
                    err_files.write(f"[-] {self.err_tags}\n{traceback.format_exc()}")

def instance_works(instance_traversal):
    instance_traversal.requests()

def main():
    try:
        arg = argparse.ArgumentParser()
        arg.add_argument("-url",type=str,required=True,help="[>] target_url / -url <target_url>")
        arg.add_argument("-w",type=str,required=True,help="[>] wordlists / -w <wordlists>")
        arg.add_argument("-p",type=int,help="[>] Port_Numbers / -p <port_numbers>")
        arg.add_argument("-t",type=int,default=4,help="[>] Thread_Number / -t <thread_number>")
        parse = arg.parse_args()

        instance_traversal = Multi_Traversal(parse.url,parse.w,parse.p)

        with Pool(parse.t) as pool:
            pool.starmap(instance_works, [(instance_traversal,)] * parse.t,chunksize=1)

        instance_traversal.checked_log()
    except KeyboardInterrupt:
        instance_traversal.checked_log()
        sys.stdout.write(f"\n[#] Stop_Multi_Traversal...\n")

if __name__ == "__main__":
    sys.exit(main())
