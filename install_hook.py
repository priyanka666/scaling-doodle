import os
import stat

def setup(HOOK_SOURCE_DIRECTORY_RELATIVE_PATH='tools/githooks/', HOOK_TARGET_DIRECTORY_RELATIVE_PATH='.git/hooks'):
    # checking existence of .git folder
    if os.path.isdir(HOOK_TARGET_DIRECTORY_RELATIVE_PATH):
        old_file_list = os.listdir(HOOK_TARGET_DIRECTORY_RELATIVE_PATH)
        for file_name in old_file_list:
            if file_name.endswith(".sample"): # ignores deleting default samples
                continue
            # removing previous hook versions first
            os.remove(os.path.join(HOOK_TARGET_DIRECTORY_RELATIVE_PATH, file_name))

        file_list = os.listdir(HOOK_SOURCE_DIRECTORY_RELATIVE_PATH) # list of files in hook directory
        for file_name in file_list:
            if file_name.startswith('.'): # ignores hidden files
                continue
            source_path = os.path.abspath(os.path.join(HOOK_SOURCE_DIRECTORY_RELATIVE_PATH, file_name))
            target_path = os.path.join(HOOK_TARGET_DIRECTORY_RELATIVE_PATH, file_name)
            # adding executable permission for the file
            os.chmod(source_path, stat.IRWXU)
            os.symlink(source_path, target_path)
    else:
        exit("Failed to install hooks. Git directory not initialised")
