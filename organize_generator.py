import os

locations = []
folders = [['Compressed Files', '.zip', '.bin', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],

           ['Audio Files', '.aac', '.adt', '.adts', '.aif', '.aifc', '.aiff', '.m4a', '.mp3', '.wav', '.wma', '.flac',
            '.ogg', '.wv', '.aup3'],

           ['Documents', '.doc', '.docm', '.docx', '.dot', '.dotx', '.pdf', '.txt', '.wbk', '.wps', '.log'],

           ['Pictures', '.gif', '.jpg', '.jpeg', '.png', '.psd', '.tif', '.tiff', '.webp', '.xcf', '.svg', '.ico'],

           ['Videos', '.vob', '.wmv', '.mov', '.mp4', '.m4v', '.m4a'],

           ['Applications', '.exe', '.msi', '.msu', '.msp', '.msc', '.jar', '.iso', '.run'],

           ['Presentations', '.pot', '.potm', '.potx', '.ppam', '.pps', '.ppsm', '.ppsx', '.ppt', '.pptm', '.pptx',
            '.sldm', '.sldx'],

           ['Spreadsheets', '.xla', '.xlam', '.xll', '.xlm', '.xls', '.xlsm', '.xlsx', '.xlt', '.xltm', '.xltx',
            '.xlw'],

           ['Programs', '.py', '.c', '.cpp', '.h', '.java', '.js', '.php', '.pl', '.rb', '.sh', '.xml', '.html'],

           ['3D', '.stl', '.g3drem', '.gcode', '.sldprt', '.catpart', '.igs', '.step', '.stp', '.x3d', '.x3dv', '.x3db',
            '.x3dbz', '.sldasm'],

           ['Fonts', '.ttf', '.otf', '.woff', '.woff2', '.eot', '.fnt', '.fon', '.pfb', '.pfm', '.afm', '.dfont', '.dxf']]


print('Enter directories to organize (leave blank to continue):')
while True:
    location = input(' > ')
    if location == '':
        break
    elif os.path.exists(location):
        locations.append(location)
        print(f'Added {location}')
    else:
        print('Directory not found')

print('To create a custom folder or override default configuration, enter a folder name:')
while True:
    current_folder = []
    folder_input = input(' > ')
    if folder_input == '':
        break
    current_folder.append(folder_input)
    print(f'Enter file extensions for {current_folder}:')
    while True:
        extension_input = input(' > ')
        if extension_input == '':
            break
        for folder in folders:
            for file_type in folder:
                if extension_input == file_type:
                    folder.remove(file_type)
                    break
        current_folder.append(extension_input)
    folders.append(current_folder)

name = input('What would you like to call this organizer? >  ')

program_code = f"""from shutil import move
import os

locations = {locations}
folders = {folders}


def move_file(category):
    folder_name = category[0]
    for file_type in category:
        if file_ext.upper() == file_type.upper():
            file_destination = os.path.join(cwd, folder_name)
            if not os.path.exists(file_destination):
                os.mkdir(file_destination)
            file_path = os.path.join(file_destination, file)
            if os.path.exists(file_path):
                new_name = filename + '(duplicate)' + file_ext
                new_path = os.path.join(cwd, new_name)
                os.rename(file_source, new_path)
                try:
                    move(new_path, file_destination)
                except FileNotFoundError as exc:
                    print(exc)
            else:
                try:
                    move(file_source, file_destination)
                except FileNotFoundError as exc:
                    print(exc)

for location in locations:
    if os.path.exists(location):
        os.chdir(location)
        cwd = os.getcwd()

        print('Organizing files...')
        for file in os.listdir(cwd):
            filename, file_ext = os.path.splitext(file)
            file_source = os.path.join(cwd, file)

            for folder in folders:
                move_file(folder)

        print('Files have been organized.')
    else:
        print(f'Directory not found')
        """

with open(f'{name}.py', 'w') as f:
    f.write(program_code)
