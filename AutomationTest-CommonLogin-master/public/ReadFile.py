#coding=utf-8

def read_txt(path,match,splitSymbol,lr=1):
    with open(path, 'r') as f:
        for line in f.readlines():
            if match in line:
                value = line.split(splitSymbol)[lr]
                return value.strip('\n')








if __name__ == "__main__":
    from public.readConfig import *
    headerfilepath = headerManage['head_path']
    match = headerManage['init_cookie']
    joinSymbol = "==>"
    print(read_txt(headerfilepath,match,joinSymbol,1))

