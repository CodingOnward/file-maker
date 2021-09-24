import datetime
import os

root_path = 'path'

start = datetime.datetime.strptime("2021-07-11", "%Y-%m-%d")
end = datetime.datetime.strptime("2021-12-31", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

markdown_file_list = []

for date in date_generated:
    markdown_file_list.append(date.strftime("%Y-%m-%d"))

  
# path of the current script
path = ".//daily//"
  
# Before creating
dir_list = os.listdir(path) 
print("List of directories and files before creation:")
print(dir_list)
print()
  
# Creates a new file
for filename in markdown_file_list:
    file_to_open = f".//daily//{filename}.md"
    with open(file_to_open, 'w') as fp:
        fp.write(f"# {filename}\n\n")
        fp.write("## TODO\n\n")
        fp.write("- [ ] \n")
        fp.write("- [ ] \n")
        fp.write("- [ ] \n")
        fp.write("- [ ] \n")
        fp.write("- [ ] \n")
        pass
  
# After creating 
dir_list = os.listdir(path)
print("List of directories and files after creation:")
print(dir_list)
