import os
import time
from time import gmtime, strftime

savedate = strftime("%Y-%m-%d-%H-%M", gmtime())

class Dumper:
    def __init__(self, file_path):
        self.file_path = file_path
        self.logs = []
        self.dumps = []

    def dump(self):
        try:
            with open(self.file_path, 'rb') as f:
                byte = f.read(1)
                while byte != b'':
                    self.dumps.append(hex(ord(byte)))
                    byte = f.read(1)
        except Exception as e:
            self.logs.append(str(e))

    def save_dumps(self):
        try:
            with open(f'./dumps/{savedate}.txt', 'w') as f:
                for dump in self.dumps:
                    f.write(dump + '\n')
        except Exception as e:
            self.logs.append(str(e))

    def save_logs(self):
        try:
            with open('./logs/logs.txt', 'a') as f:
                for log in self.logs:
                    f.write(log + '\n')
        except Exception as e:
            self.logs.append(str(e))
    
    def run(self):
        self.dump()
        self.save_dumps()
        self.save_logs()
    
    def get_dumps(self):
        return self.dumps
    
    def get_logs(self):
        return self.logs
    
    def get_file_path(self):
        print(f'File Path: {self.file_path}') 
    
    def set_file_path(self, file_path):
        self.file_path = file_path
    
    def get_file_size(self):
        print(f'File Size: {os.path.getsize(self.file_path)}')
    
    def get_file_creation_date(self):
        print(f'File Creation Time: {time.ctime(os.path.getctime(self.file_path))}')
    
    def get_file_modification_date(self):
        print(f'File Modification Date: {time.ctime(os.path.getctime(self.file_path))}')
    
    def get_file_access_date(self):
        print(f'File Modification Date: {time.ctime(os.path.getctime(self.file_path))}')
        return time.ctime(os.path.getatime(self.file_path))
    
    def get_file_owner(self):
        print(f'File Modification Date: {os.stat(self.file_path).st_uid}')

class Dumper_Manager:
        start = time.time()
        file_input = input('Enter file path: ')
        dumper = Dumper(file_input)
        dumper.run()
        end = time.time()
        print(f'Time Elapsed: {end - start}')

Dumper_Manager()