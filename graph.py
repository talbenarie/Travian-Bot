import matplotlib.pyplot as plt
import sys


scores = []  # represents the raiding scores
gaps = []  # represents the resources raided in one hour
timestamps = []  # timestamps
users = []  # the users in the graph


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
            if info[1] == users[0]:
                prev_score = scores[-1] if len(scores) > 0 else 0
                score_earned = int(info[2])
                scores.append(score_earned)
                gaps.append(score_earned - prev_score)
                timestamps.append(timestamp)
                timestamp += 30
                break




def main():
    if sys.argv is None or len(sys.argv) < 2:
        print("Must add at-least one system variable")
        return
    if len(sys.argv) >= 2:
        users.append(sys.argv[1])
    else:
        print("Must add at-least one system variable")
        return

    contents = load_file_contents("raid_analytics.txt")
    parse_file_contents(contents)

    print(scores)
    print(timestamps)

    gaps.pop(0)
    scores.pop(0)
    timestamps.pop(0)

    plt.subplot(2, 1, 1)
    plt.plot(timestamps, gaps)
    plt.title('Resources Raided (Raid per 30m)')
    plt.ylabel('Resources')

    plt.subplot(2, 1, 2)
    plt.plot(timestamps, scores)
    plt.ylabel('Resources')
    plt.xlabel('Timestamp (Minutes)')
    plt.show()


if __name__ == "__main__":
    main()

