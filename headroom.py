'''Headroom: A script to generate a playlist representing 24 hours of broadcast (cable) tv content.
'''

# There are 48, 30-minute slots throughout the day.
# Programming resets at 4am.
# There are prime-times at 7am, 3pm, 6pm, and 11pm. For educational, teen, young adult, and late-nite programming respectively.

# When populating a schedule, take the #1 program in a category, and put it on at prime-time.
# Then, fill the rest of the programming in that category in the direction of 4pm (magic number), but only halfway to the next prime time in that direction.
# When you run out of space, fill in the other direction, but only halfway to the next prime time in that direction.

# Commercials are 30 to 60 seconds long, but can be cut off or padded with dead air as appropriate.
# Commercials also have a target demographic which dictates which category they can play in.
# Some are targeted at parents who may also be watching, but will mostly be targeted at the target demographic for the programming.
# Commercial breaks are 3 minutes and 30 seconds long. That's a maximum of 7 commercials, and a minimum of 4.
# There are usually 2 commercial breaks, depending on the length of the program. Extra time at the end of the program should be filled with commercials where they can be played in full, otherwise bumps should be shown until the next program is set to begin.


def main():
    pass

if __name__ == "__main__":
    main()
