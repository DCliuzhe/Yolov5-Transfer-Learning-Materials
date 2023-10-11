import os

def get_file_addresses(folder_path):
    file_addresses = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_addresses.append(file_path)
    return file_addresses

def write_to_txt(file_addresses, output_file):
    with open(output_file, 'w') as f:
        for address in file_addresses:
            f.write(address + '\n')

# 设置文件夹路径和输出文件名
folder_path = './train/images'
output_file = 'output.txt'

# 获取文件地址列表
addresses = get_file_addresses(folder_path)

# 写入txt文件
write_to_txt(addresses, output_file)
