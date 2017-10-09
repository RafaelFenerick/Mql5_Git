from shutil import copyfile
import os
import shutil

def mql5_to_git_transfer(complement_path):
    mql5_init_path = mql5_general_path + complement_path + "\\"

    dest_mql5_init_path = "SecurityCopy\\mql5\\" + complement_path + "\\"
    dest_git_init_path = "SecurityCopy\\git\\" + complement_path + "\\"

    git_init_path = git_general_path + complement_path + "\\"

    if os.path.exists(dest_mql5_init_path):
        shutil.rmtree(dest_mql5_init_path)
    if os.path.exists(dest_git_init_path):
        shutil.rmtree(dest_git_init_path)
    if not os.path.exists(dest_mql5_init_path):
        os.makedirs(dest_mql5_init_path)
    if not os.path.exists(dest_git_init_path):
        os.makedirs(dest_git_init_path)

    for mql5_full_path, dirs, files in os.walk(mql5_init_path):
        mql5_end_path = mql5_full_path.replace(mql5_init_path, "")
        for file in files:
            add = "\\"
            if mql5_end_path == "":
                add = ""
            src_path = mql5_init_path + mql5_end_path + add
            dest_path = dest_mql5_init_path + mql5_end_path + add
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            copyfile(src_path + file, dest_path + file)

    for git_full_path, dirs, files in os.walk(git_init_path):
        git_end_path = git_full_path.replace(git_init_path, "")
        for file in files:
            add = "\\"
            if git_end_path == "":
                add = ""
            src_path = git_init_path + git_end_path + add
            dest_path = dest_git_init_path + git_end_path + add
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            copyfile(src_path + file, dest_path + file)

    if os.path.exists(git_init_path):
        shutil.rmtree(git_init_path)
    if not os.path.exists(git_init_path):
        os.makedirs(git_init_path)

    for dest_mql5_full_path, dirs, files in os.walk(dest_mql5_init_path):
        dest_mql5_end_path = dest_mql5_full_path.replace(dest_mql5_init_path, "")
        for file in files:
            add = "\\"
            if dest_mql5_end_path == "":
                add = ""
            src_path = dest_mql5_init_path + dest_mql5_end_path + add
            dest_path = git_init_path + dest_mql5_end_path + add
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            if ".mqh" not in file and ".mq5" not in file:
                if ".ex5" in file:
                    pass
                else:
                    copyfile(src_path + file, dest_path + file)
                continue
            try:
                with open(src_path + file, 'rb') as source_file:
                    with open(dest_path + file, 'w+b') as dest_file:
                        contents = source_file.read()
                        dest_file.write(contents.decode('utf-8').encode('utf-8'))
            except:
                try:
                    with open(src_path + file, 'rb') as source_file:
                        with open(dest_path + file, 'w+b') as dest_file:
                            contents = source_file.read()
                            dest_file.write(contents.decode('utf-16').encode('utf-8'))
                except:
                    try:
                        with open(src_path + file, 'rb') as source_file:
                            with open(dest_path + file, 'w+b') as dest_file:
                                contents = source_file.read()
                                dest_file.write(contents.decode('iso8859').encode('utf-8'))
                    except:
                        raise("ERROR - Not Decoded")

def git_to_mql5_transfer(complement_path):
    mql5_init_path = mql5_general_path + complement_path + "\\"

    dest_mql5_init_path = "SecurityCopy\\mql5\\" + complement_path + "\\"
    dest_git_init_path = "SecurityCopy\\git\\" + complement_path + "\\"

    git_init_path = git_general_path + complement_path + "\\"

    if os.path.exists(dest_mql5_init_path):
        shutil.rmtree(dest_mql5_init_path)
    if os.path.exists(dest_git_init_path):
        shutil.rmtree(dest_git_init_path)
    if not os.path.exists(dest_mql5_init_path):
        os.makedirs(dest_mql5_init_path)
    if not os.path.exists(dest_git_init_path):
        os.makedirs(dest_git_init_path)

    for mql5_full_path, dirs, files in os.walk(mql5_init_path):
        mql5_end_path = mql5_full_path.replace(mql5_init_path, "")
        for file in files:
            add = "\\"
            if mql5_end_path == "":
                add = ""
            src_path = mql5_init_path + mql5_end_path + add
            dest_path = dest_mql5_init_path + mql5_end_path + add
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            copyfile(src_path + file, dest_path + file)

    for git_full_path, dirs, files in os.walk(git_init_path):
        git_end_path = git_full_path.replace(git_init_path, "")
        for file in files:
            add = "\\"
            if git_end_path == "":
                add = ""
            src_path = git_init_path + git_end_path + add
            dest_path = dest_git_init_path + git_end_path + add
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            copyfile(src_path + file, dest_path + file)

    if os.path.exists(mql5_init_path):
        shutil.rmtree(mql5_init_path)
    if not os.path.exists(mql5_init_path):
                os.makedirs(mql5_init_path)

    for git_full_path, dirs, files in os.walk(git_init_path):
        git_end_path = git_full_path.replace(git_init_path, "")
        for file in files:
            add = "\\"
            if git_end_path == "":
                add = ""
            src_path = git_init_path + git_end_path + add
            dest_path = mql5_init_path + git_end_path + add
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            copyfile(src_path + file, dest_path + file)

def git_to_mql5():
    # Paths to transfer
    git_to_mql5_transfer("Include")
    git_to_mql5_transfer("Experts")

def mql5_to_git():
    # Paths to transfer
    mql5_to_git_transfer("Include")
    mql5_to_git_transfer("Experts")

# Git directory
git_general_path = "C:\\Git_Directory\\"

# Mql5 directory
mql5_general_path = "C:\\...\\MetaQuotes\\Terminal\\account_number\\MQL5\\"

input_key = raw_input("Mql5_to_git = 1, Git_to_Mql5 = 2\nInput: ")
if input_key == '1':
    mql5_to_git()
elif input_key == '2':
    git_to_mql5()
else:
    print "Not allowed key!"