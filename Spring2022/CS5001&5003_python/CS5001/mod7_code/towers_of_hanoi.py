""" Align CS5001
    Sample code for Module 7: Recursion.
    Recursive implementation to the Towers of Hanoi problem
"""


def tower_of_hanoi(num_disks, from_rod, to_rod):
    """
    function: tower_of_hanoi, the starting point for our program
    params:   num_disks to be moved
              from_rod, the starting rod for the disks
              to_rod, the target to move the disks to
              :rtype: object
    """
    move_stack(num_disks, from_rod, to_rod)


def find_spare_rod(from_rod, to_rod):
    """
    function: find_spare_rod
    params:   from_rod & to_rod, the rods that are already in use
    return:   the spare rod
    """
    return 6 - (from_rod + to_rod)


def move_stack(num_disks, from_rod, to_rod):
    """
    function: move_stack, recursive function
    params:   num_disks to be moved
              from_rod, the starting rod for the disks
              to_rod, the target to move the disks to
    """

    if num_disks == 1:
        move_one_disk(1, from_rod, to_rod)
    else:
        spare_rod = find_spare_rod(from_rod, to_rod)
        move_stack(num_disks - 1, from_rod, spare_rod)
        move_one_disk(num_disks, from_rod, to_rod)
        move_stack(num_disks - 1, spare_rod, to_rod)


def move_one_disk(disk, from_rod, to_rod):
    """
    function: move_one_disk
    params:   disk to be moved
              from_rod, the starting rod for the disks
              to_rod, the target to move the disks to
    """
    print("Moving disk#", disk, "from rod", from_rod, "to", to_rod)
    # Later, can add code to control gnarly robotic arm,
    # or a Terminator T1000


def main():
    num_disks = int(input("Please enter the number of disks to be moved: "))
    tower_of_hanoi(num_disks, 1, 1)


if __name__ == '__main__':
    main()
