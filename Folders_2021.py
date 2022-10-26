import glob
import os
import pandas as pd
import time


parent_dir = r"C:\Users\DavidHolroyd\OneDrive - American Plant Maintenance\CD"

folders = os.listdir(parent_dir)
print(len(folders))


lst1 = glob.glob(rf"{parent_dir}\*\2021")
lst2 = glob.glob(rf"{parent_dir}\*\*\2021")
lst3 = glob.glob(rf"{parent_dir}\*\*\*\2021")
lst4 = glob.glob(rf"{parent_dir}\*\*\*\*\2021")
lst5 = glob.glob(rf"{parent_dir}\*\*\*\*\*\2021")
lst6 = glob.glob(rf"{parent_dir}\*\*\*\*\*\*\2021")

lstoflsts = [lst1, lst2, lst3, lst4, lst5, lst6]

folders_to_skip = []
folders_to_create = []

for lst in lstoflsts:
    for folder in lst:
        parent_folder, check_2021 = folder[:-4], folder[-4:]
        if check_2021 == '2021':
            subfolders = os.listdir(parent_folder)
            if '2022' in subfolders:
                print(f'2022 subfolder already exists in {parent_folder}')
                folders_to_skip.append(folder)
            else:
                folder = folder[:-1]
                folder_2022 = folder + "2"
                time.sleep(0.1)
                folders_to_create.append(folder_2022)
                os.mkdir(folder_2022)
        else:
            folders_to_skip.append(folder)
            print(f"Skipping {folder}")

df_skipped = pd.DataFrame(folders_to_skip)
df_created = pd.DataFrame(folders_to_create)

df_created.to_csv("2022_created_folders.csv", header=False, index=False)
df_skipped.to_csv("2022_skipped_folders.csv", header=False, index=False)

