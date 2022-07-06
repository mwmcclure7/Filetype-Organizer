def organize_files(location):
    import os
    from shutil import move

    if os.path.exists(location):
        os.chdir(location)
        cwd = os.getcwd()

        def move_file(folder_name, *file_types):
            for file_type in file_types:
                if file_ext.upper() == file_type.upper():
                    file_destination = os.path.join(cwd, folder_name)
                    if not os.path.exists(file_destination):
                        os.mkdir(file_destination)
                    file_path = os.path.join(file_destination, file)
                    if os.path.exists(file_path):
                        new_name = filename + '(duplicate)' + file_ext
                        new_path = os.path.join(cwd, new_name)
                        os.rename(file_source, new_path)
                        move(new_path, file_destination)
                    else:
                        move(file_source, file_destination)

        print('Organizing files...')
        for file in os.listdir(cwd):
            filename, file_ext = os.path.splitext(file)
            file_source = os.path.join(cwd, file)

            move_file('Compressed Files', '.zip', '.bin', '.rar',
                      '.7z', '.tar', '.gz', '.bz2', '.xz')

            move_file('Audio Files', '.aac', '.adt', '.adts', '.aif',
                      '.aifc', '.aiff', '.m4a', '.mp3', '.wav', '.wma', '.flac', '.ogg', '.wv')

            move_file('Documents', '.doc', '.docm', '.docx',
                      '.dot', '.dotx', '.pdf', '.txt', '.wbk', '.wps', '.log')

            move_file('Pictures', '.gif', '.jpg',
                      '.jpeg', '.png', '.psd', '.tif', '.tiff', '.webp', '.xcf')

            move_file('Videos', '.vob', '.wmv', '.mov', '.mp4', '.m4v', '.m4a')

            move_file('Applications', '.exe', '.msi', '.msu', '.msp', '.msc')

            move_file('Presentations', '.pot', '.potm', '.potx', '.ppam',
                      '.pps', '.ppsm', '.ppsx', '.ppt', '.pptm', '.pptx', '.sldm', '.sldx')

            move_file('Spreadsheets', '.xla', '.xlam', '.xll',
                      '.xlm', '.xls', '.xlsm', '.xlsx', '.xlt', '.xltm', '.xltx', '.xlw')

            move_file('Programs', '.py', '.c', '.cpp', '.h', '.java',
                      '.js', '.php', '.pl', '.rb', '.sh', '.xml', '.html')

            move_file('3D', '.stl', '.g3drem',
                      '.gcode', '.sldprt', '.catpart', '.igs', '.step', '.stp', '.x3d', '.x3dv', '.x3db', '.x3dbz', '.sldasm')

            move_file('Fonts', '.ttf', '.otf',  '.woff', '.woff2')

        print('Files have been organized.')
    else:
        print('Directory Not Found')


def organize_pics(location):
    import os
    from shutil import move

    if os.path.exists(location):
        os.chdir(location)

        cwd = os.getcwd()

        for picture in os.listdir(cwd):
            filename, file_ext = os.path.splitext(picture)
            picture_date = filename[0:4]
            picture_source = os.path.join(cwd, picture)
            picture_destination = os.path.join(cwd, picture_date)

            if file_ext and os.path.exists(picture_destination):
                move(picture_source, picture_destination)
            elif file_ext and os.path.exists(os.path.join(cwd, 'Other')):
                move(picture_source, os.path.join(cwd, 'Other'))
        print('Pictures have been organized.')
    else:
        print('Directory Not Found')


def organize_3d(location):
    import os
    from shutil import move

    if os.path.exists(location):
        os.chdir(location)

        cwd = os.getcwd()

        def move_file(folder_name, *file_types):
            for file_type in file_types:
                if file_ext.upper() == file_type.upper():
                    file_destination = os.path.join(cwd, folder_name)
                    if not os.path.exists(file_destination):
                        os.mkdir(file_destination)
                    file_path = os.path.join(file_destination, file)
                    if os.path.exists(file_path):
                        new_name = filename + '(duplicate)' + file_ext
                        new_path = os.path.join(cwd, new_name)
                        os.rename(file_source, new_path)
                        move(new_path, file_destination)
                    else:
                        move(file_source, file_destination)

        print('Organizing files...')
        for file in os.listdir(cwd):
            filename, file_ext = os.path.splitext(file)
            file_source = os.path.join(cwd, file)

            move_file('STL Files', '.stl')
            move_file('GCODE Files', '.gcode', '.g3drem')

        print('Files have been organized.')
    else:
        ('Directory Not Found')
