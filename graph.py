import matplotlib.pyplot as plt
import sys


scores_user1 = []
scores_user2 = []
scores_user3 = []
timestamps = []
users = []


def load_file_contents(filename):
    file = open(filename, "r", encoding="utf8")
    file_content = file.read()
    file.close()
    return file_content


def parse_file_contents(contents):
    timestamp = 0  # minutes
    tables = contents.split("#############")
    for table in tables:
        lines = table.splitlines()
        for player in lines:
            info = player.split(",")
            if len(info) < 3:
                continue
            if info[1] == users[0] and len(scores_user1) < len(timestamps):
                arr = scores_user1
                score_earned = int(info[2])
                arr.append(score_earned)
            elif len(users) >= 2 and info[1] == users[1] and len(scores_user2) < len(timestamps):
                arr = scores_user2
                score_earned = int(info[2])
                arr.append(score_earned)
            elif len(users) >= 3 and info[1] == users[2] and len(scores_user3) < len(timestamps):
                arr = scores_user3
                score_earned = int(info[2])
                arr.append(score_earned)

        timestamps.append(timestamp)
        timestamp += 30


def main():
    if sys.argv is None or len(sys.argv) < 2:
        print("Must add at-least one system variable")
        return
    if len(sys.argv) >= 2:
        users.append(sys.argv[1])
    else:
        print("Must add at-least one system variable")
        return
    if len(sys.argv) >= 3:
        users.append(sys.argv[2])
    if len(sys.argv) >= 4:
        users.append(sys.argv[3])

    contents = load_file_contents("raid_analytics.txt")
    parse_file_contents(contents)

    while len(timestamps) > len(scores_user1):
        timestamps.pop(- 1)

    plt.plot(timestamps, scores_user1)

    if len(scores_user2) > 0:
        plt.plot(timestamps, scores_user2)

    if len(scores_user3) > 0:
        plt.plot(timestamps, scores_user3)

    plt.legend(users)
    plt.title('Resources Raided (Total)')
    plt.ylabel('Resources')
    plt.xlabel('Timestamp (Minutes)')
    plt.show()


if __name__ == "__main__":
    main()

