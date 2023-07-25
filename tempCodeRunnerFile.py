import shutil
target_folder="c:\Users\admin\Downloads"
extensions={item.split(.)[-1] for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, item))}