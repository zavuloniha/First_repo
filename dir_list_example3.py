
import os

def list_directories(path, prefix=""):
    for item in sorted(os.listdir(path)):
        item_path = os.path.join(path, item)
        print(prefix + item)
        if os.path.isdir(item_path):
            list_directories(item_path, prefix + "    ")

# Задайте шлях до кореневої директорії
root_dir = "/Users/lmohylna/Documents/backups/.kube-2/"
#print(f"{root_dir}/")
print(os.path.basename(root_dir) + "/")
list_directories(root_dir, prefix="    ")

