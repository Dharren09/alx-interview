#!/usr/bin/python3

"""Lockboxes"""

def canUnlockAll(boxes):
    unlocked = [False] * len(boxes)
    unlocked[0] = True

    stack = [0]

    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
