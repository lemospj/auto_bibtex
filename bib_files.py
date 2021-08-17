import os
import glob


def find_bib_path():
    cwd = os.getcwd()
    print('Current directory: {cwd}'.format(cwd = cwd))
    cur_dir = input('\nUse current directory? (Y/N)\n> ')

    if cur_dir.lower() == 'y':
        target_path = cwd
    elif cur_dir.lower() == 'n':
        target_path = input('\nWhat is the directory where you want the .bib file to be?\n> ')

    bib_path = os.path.join(target_path, '*.bib')
    bib_list = glob.glob(bib_path)

    bib_file = 0

    while bib_file == 0:
        if len(bib_list) == 1:
            use_bib = input('Use {bibf}?\n> '.format(bibf = bib_list[0]))
            if use_bib.lower() == 'y':
                bib_file = bib_list[0]
            else:
                bib_list.pop()
        else:
            bib_file = input('\nFile name: ')
            if bib_file[-4:] != '.bib':                         # The user will be allowed to enter the file name
                bib_file = ''.join([bib_file, '.bib'])          # with or without specifying the extension. The
            bib_file = os.path.join(target_path, bib_file)      # program will detect whether the extension .bib
    return bib_file                                             # was included or not.

def create_bib(bib_file, bib_entry):
    with open(bib_file, 'a') as bib_write:
        bib_write.write(bib_entry)
