import os

def split_file(file_path, folder_path1,folder_path2):
    with open(file_path, 'r') as file:
        data = file.read()
        total_size = len(data)
        split_size = total_size // 2

        first_half = data[:split_size]
        second_half = data[split_size:]

        # write first half to new file
        with open(os.path.join(folder_path1, f"{os.path.basename(file_path)}.part1"), 'w') as file1:
            file1.write(first_half)

        # write second half to new file
        with open(os.path.join(folder_path2, f"{os.path.basename(file_path)}.part2"), 'w') as file2:
            file2.write(second_half)

if __name__ == '__main__':
    file_path = 'D:\\subishkrish\\randm.txt'
    folder_path1 = 'D:/subishkrish/split/part1/'
    folder_path2 = 'D:/subishkrish/split/part2/'
    split_file(file_path, folder_path1,folder_path2)