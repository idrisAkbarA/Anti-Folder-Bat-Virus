import os


def main():
    path = input('Input dir: ')
    dirs = os.walk(path, topdown=False)
    print('\n')
    # loop through dir to scan for viruses
    for root, files in dirs:
        for name in files:
            path = os.path.join(root, name)
            if isVirus(path):
                print(path + ' ' + 'is virus. Deleting...')
                os.remove(path)
                print('Done\n')


def isVirus(path):
    path_segments = path.split('\\')
    file = path_segments[len(path_segments)-1].split('.')
    dirName = path_segments[len(path_segments)-2]

    # check if file has extension
    if len(file) < 2:
        return False

    # check if file is a bat file
    if file[1] != 'bat':
        return False

    # check if file name is equal to dir name
    if file[0] != dirName:
        return False

    # check if bat file contain virus code
    f = open(path, 'r')
    contents = f.readlines()
    virus_code = 'for /r "d:\\" /d %%a in (*) do copy %0 "%%~fa\\%%~nxa.bat"'
    if contents[1] != virus_code:
        return False

    return True


main()
