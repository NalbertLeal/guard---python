if __name__ == '__main__':
    from sys import argv

    from guard import Guard

    if len(argv) == 0:
        print('>>> to use GUARD you need to pass some parameters:')
        print('>>> \t python guard.py <E or D> <KEY TO ENCRYPT OR DECRYPT>.')
        print('>>> If the first parameter are the letter E then this program encript;')
        print('>>> If the first parameter are the letter D then this program decript;\n')
    else:
        if argv[1] == '-h' and argv[1] == '--help':
            print('>>> to use GUARD you need to pass some parameters:')
            print('>>> \t python guard.py <E or D> <KEY TO ENCRYPT OR DECRYPT>.')
            print('>>> If the first parameter are the letter E then this program encript;')
            print('>>> If the first parameter are the letter D then this program decript;\n')
        else:
            if argv[1] == 'D':
                root_path = os.path.dirname(os.path.abspath(__file__))
                g = Guard(root_path, argv[2])
                g.run()
            elif argv[2] == 'E':
                root_path = os.path.dirname(os.path.abspath(__file__))
                g = Guard(root_path, argv[2])
                g.run()
            else:
                print('>>> to use GUARD you need to pass some parameters:')
                print('>>> \t python guard.py <E or D> <KEY TO ENCRYPT OR DECRYPT>.')
                print('>>> If the first parameter are the letter E then this program encript;')
                print('>>> If the first parameter are the letter D then this program decript;\n')
