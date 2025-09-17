import os
import shutil

# Paths
# src_dir = './data/parse_labels/originals'
# parse_dir = './data/parse_labels'

src_dir = './data/parse_preds_fixed/originals'
parse_dir = './data/parse_preds_fixed'

test_lst_path = os.path.join(parse_dir, 'test.lst')

# Get all files in src_dir
files = sorted([f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))])

# Prepare to append to test.lst
with open(test_lst_path, 'a') as test_lst:
    for file in files:
        base_name = os.path.splitext(file)[0]
        # Remove extension if double extension
        if '.' in base_name:
            base_name = base_name.split('.')[0]
        folder_path = os.path.join(parse_dir, base_name)
        os.makedirs(folder_path, exist_ok=True)
        src_file_path = os.path.join(src_dir, file)
        dst_file_path = os.path.join(folder_path, 'vessel.nii.npz')
        shutil.copy2(src_file_path, dst_file_path)
        test_lst.write(base_name + '\n')
print('Done!')
