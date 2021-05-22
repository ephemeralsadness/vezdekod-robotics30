
def main():
    length = int(input())
    n = int(input())
    bots = [(bot, bot * 2 < length) for bot in sorted(list(map(int, input().split())))]

    mx = 0
    for bot, to_right in bots:
        if to_right:
            mx = max(mx, length - bot)
        else:
            mx = max(mx, bot)
    print(mx)


if __name__ == '__main__':
    main()
