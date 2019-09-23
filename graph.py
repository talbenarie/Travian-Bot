import matplotlib.pyplot as plt
from datetime import datetime


ranks = []
scores = []
timestamps = []


def load_file_contents(filename):
    file = open(filename, "r", encoding="utf8")
    file_content = file.read()
    file.close()
    return file_content


def parse_file_contents(contents):
    ts = 0  # minutes
    tables = contents.split("#############")
    for table in tables:
        lines = table.splitlines()
        for user in lines:
            info = user.split(",")
            if len(info) < 3:
                continue

            if info[1] == "TechnoTal":
                ranks.append(info[0])
                scores.append(int(info[2]))
                timestamps.append(ts)
                ts += 30
                break
            #info[0]  #rank
            #info[1]  #name
            #info[2]  #points


def main():
    contents = load_file_contents("raid_analytics.txt")
    parse_file_contents(contents)

    x = timestamps #  [1, 2, 3, 4, 5]  #date
    y = scores # [10, 1000, 5000, 1000000, 500000]  #value

    plt.plot(x, y)
    plt.ylabel('Resources Raided')
    plt.xlabel('Minutes since raiding is recorded')
    plt.show()


if __name__ == "__main__":
    main()

