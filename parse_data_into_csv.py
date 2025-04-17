from pathlib import Path


def generate_line(file: Path) -> str:
    filename = file.name

    split = filename.split('|')

    parsed = f'{split[0]},{split[1]},{split[2].removeprefix('thread_count_')},{split[4].removesuffix('.txt')},'

    with file.open() as opened:

        total_time = 0.0

        for line in opened.readlines():

            if line.lstrip() == '':
                continue

            if line.count('\t'):
                index = line.index('\t')
            else:
                index = line.index(' ')

            time_line = line[index:]

            min_secs = time_line.split('m')

            time = int(min_secs[0]) * 60 + float(min_secs[1].replace('s', ''))

            parsed += f'{time},'
            total_time += time
        
    return parsed + str(total_time) + '\n'

HEADER = 'timestamp,type,thread_count,file_size,real,user,sys,total\n'

walker = (Path.cwd() / 'data').walk()

with (Path.cwd() / 'output.csv').open('w+') as output:
    output.write(HEADER)

    for dir, _, files in walker:
        for file in files:
            if file.count('.txt') >= 1:
                output.write(generate_line(dir / file))
