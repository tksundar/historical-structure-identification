import os
import cv2
# test for corrupt files
def is_jpeg_corrupt(file_path):
    try:
        img = cv2.imread(file_path)
        if img is None:
            return True
        return False
    except Exception as e:
        print(e)
    return True

# remove bad files
def remove_bad_files(bad_files,name):
    print(f'Removing bad files in folder {name}\n')
    try:
        for fp in bad_files:
          print(f'Removing bad file {fp}')
          os.remove(fp)
    except Exception as e:
        print(f"Error removing files: {e}")
# find bad files
def find_bad_files(directory,name):
  print(f'Finding non-image files and wrongly encoded files in folder {name}\n')
  bad_files = list()
  for sub_dir in os.listdir(directory):
          dir_path = os.path.join(directory,sub_dir)
          is_dir = os.path.isdir(dir_path)
          if is_dir:
              print(f'processing  {dir_path}.   number of images {len(os.listdir(dir_path))}')
              files = os.listdir(dir_path)
              for file in files:
                  file_path = os.path.join(dir_path, file)
                  if is_jpeg_corrupt(file_path):
                      bad_files.append(file_path)
  print(f'\n{len(bad_files)} Bad files found in folder {directory} \n')
  return bad_files

# required if we want to run this on kaggle notebooks. Kaggle doesnt accept files with apostrophe
def replace_apostrophe(directory,name):
    print(f'removing apostrophe from folder {name}\n')
    for sub_dir in os.listdir(directory):
        dir_path = os.path.join(directory, sub_dir)
        is_dir = os.path.isdir(dir_path)
        if is_dir:
            print(f'processing  {dir_path}')
            files = os.listdir(dir_path)
            for file in files:
                file_path = os.path.join(dir_path, file)
                if '\'' in file_path:
                    new_file = file_path.replace('\'',"")
                    os.rename(file_path,new_file)
                    print(f'old file {file_path}')
                    print(f'new file {new_file}')

if __name__ == '__main__':
    directory = "C:\\Users\\tksra\\OneDrive\\Desktop\\AIML\\Capstone\\Capstone 2\\Part 1\\dataset_hist_structures_2\\dataset_hist_structures\\Dataset_test\\Dataset_test_original_1478"
    name = 'Dataset_test_original_1478'
    replace_apostrophe(directory,name)
    bad_files = find_bad_files(directory,name)
    remove_bad_files(bad_files,name)
