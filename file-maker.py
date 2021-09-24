import datetime
import os

# --- Make Folders for 100 Days of Code #100daysofcode ---

root_path = 'path'
folders = []

for i in range(1,101):
    folders.append('day' + str(i).zfill(3))

try:
    os.mkdir(root_path)
except FileExistsError:
    print(root_path, "folder already exists! Will continue to make 100 Days of Code folders in", root_path)

for folder in folders:
    try:
        os.mkdir(os.path.join(root_path, folder))
    except FileExistsError:
        print(folder, "folder already exists!")

# Add some md to each folder

for folder in folders:
    if not os.path.exists(root_path + "/" + folder + "/" + folder + ".md"):
        with open(root_path + "/" + folder + "/" + folder + ".md", 'a') as fn:
            fn.write(f"# {folder}\n\n")
            fn.write("## TODO\n\n")
            fn.write("- [ ] \n")
            fn.write("- [ ] \n")
            fn.write("- [ ] \n")
            fn.write("- [ ] \n")
            fn.write("- [ ] \n")
    else:
        print(root_path + "/" + folder + "/" + folder + ".md" + " already exists!")

# Add some py to each folder

for folder in folders:
    if not os.path.exists(root_path + "/" + folder + "/" + folder + ".py"):
        with open(root_path + "/" + folder + "/" + folder + ".py", 'a') as fn:
            fn.write(f"# {folder}\n")
            fn.write("# \n\n")
    else:
        print(root_path + "/" + folder + "/" + folder + ".py" + " already exists!")

# Add some scratch py to each folder
for folder in folders:
    if not os.path.exists(root_path + "/" + folder + "/" + "scratch" + folder + ".py"):
        with open(root_path + "/" + folder + "/" + "scratch" + folder + ".py", 'a') as fn:
            fn.write(f"# scratch {folder}\n")
            fn.write("# \n\n")
    else:
        print(root_path + "/" + folder + "/" + "scratch" + folder + ".py" + " already exists!")

print("Done")


# --- Making Journal Files ---

# start = datetime.datetime.strptime("2021-01-01", "%Y-%m-%d")
# end = datetime.datetime.strptime("2021-12-31", "%Y-%m-%d")
# date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

# markdown_file_list = []

# for date in date_generated:
#     markdown_file_list.append(date.strftime("%Y-%m-%d") + ".md")

# for filename in markdown_file_list:
#     os.mkdir(os.path.join(root_path, filename))

# print(markdown_file_list)

# print(date_generated)

# ---

# import pandas as pd
# from datetime import datetime

# datelist = pd.date_range(start="2021-01-01",end="2021-12-31").tolist()

# print(datelist)

# ---

# import os
# from datetime import datetime, date, time, timezone

# root_path = 'C:\path'
# date = datetime.now().strftime("%Y-%m-%d")

# print(f"filename-{date}")

# date_file_list = []

# for i in range(1,366):
#     date_file_list.append(f"{date}.md")

# ---

