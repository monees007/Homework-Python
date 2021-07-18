import os


def create(week, ppa, grpa):

    global content
    print(f'Welcome to Week {week}')
    """
creates week hierarchy
    :param week: int
    :param ppa: int
    :param grpa: int
    :return:
    """
    cwd = os.path.dirname(os.path.realpath(__file__))

    try:
        print(f'Making Directory at {cwd}')
        os.mkdir(f'{cwd}/Week{week}')
    except OSError:
        print('Directory already exist. Proceeding...')
    # Create the PPAs
    for i in range(1, ppa + 1):
        try:
            x = open(f'{cwd}/Week{week}/PPA{i}.py', 'x')
        except FileExistsError:
            print(f'Should I overwrite? (y/N)')
            if input().lower() == 'y':
                x = open(f'{cwd}/Week{week}/PPA{i}.py', 'w')
                x.close()
            else:
                break
    # Create the GrPAs
    for i in range(1, grpa + 1):
        try:
            x = open(f'{cwd}/Week{week}/GrPA{i}.py', 'x')
        except FileExistsError:
            print(f'Should I overwrite? (y/N)')
            if input().lower() == 'y':
                x = open(f'{cwd}/Week{week}/PPA{i}.py', 'w')
                x.close()
            else:
                break

    # get the main content

    main = open('../main.py', 'r')
    r = main.read()  # read as a string
    last_line_index = r.rindex('\n') + 1
    last_line = r[last_line_index:]
    if 'create' in last_line:
        content = r[:last_line_index]
    main.close()
    # All content of main.py as 's' string except the self

    # delete the main.py
    os.remove("../main.py")

    # recreate main.py
    f = open('../main.py', 'w')
    f.write(content)
    f.write('template.create()')
    f.close()

    print(f'Week {week} is ready, Enjoy...')
