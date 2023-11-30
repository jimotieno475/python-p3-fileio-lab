# def write_file(file_name, file_content):
#     with open('file_name.txt',mode='w',encoding='utf-8')as file_name:
#         file_name.write("logfile")

#     with open('file_content.txt',mode='w',encoding='utf-8')as file_content:
#         file_content.write("Log 1: 5 bananas added") 
#     pass

# def append_file(file_name, append_content):

#     with open('file_name.txt',mode='a',encoding='utf-8')as file_name:
#         file_name.write("logfile")

#     with open('file_content.txt',mode='a',encoding='utf-8')as append_content:
#         append_content.write("Log 2: 3 bananas subtracted") 
#     pass

# def read_file(file_name):
#     file_name=open('file_name.txt',encoding='utf-8')
#     print(file_name.read())
#     pass
# file_io.py

def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode='w', encoding='utf-8') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode='a', encoding='utf-8') as file:
        file.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt', encoding='utf-8') as file:
        return file.read()


write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

read_file(file_name="logfile")
