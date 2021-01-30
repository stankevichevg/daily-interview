# Given a string with the initial condition of dominoes, where:
#
# . represents that the domino is standing still
# L represents that the domino is falling to the left side
# R represents that the domino is falling to the right side
#
# Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.
#
# Example:
# Input:  ..R...L..R.
# Output: ..RR.LL..RR

def push_dominoes(dominoes: str):
    forces = [0] * len(dominoes)
    force = 0
    N = len(dominoes)
    for i in range(0, N):
        if dominoes[i] == "R":
            force = N
        elif dominoes[i] == "L":
            force = 0
        else:
            force = max(0, force - 1)
        forces[i] += force
    force = 0
    for i in range(N - 1, -1, -1):
        if dominoes[i] == "L":
            force = N
        elif dominoes[i] == "R":
            force = 0
        else:
            force = max(0, force - 1)
        forces[i] -= force
    result = ""
    for i in range(0, N):
        if forces[i] == 0:
            result += "."
        elif forces[i] < 0:
            result += "L"
        else:
            result += "R"
    return result


print(push_dominoes('..R...L..R.'))
# ..RR.LL..RR