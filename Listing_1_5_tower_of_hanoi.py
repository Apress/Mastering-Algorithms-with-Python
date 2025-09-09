def tower_of_hanoi(num_disks, from_pole, with_pole, to_pole):
    if num_disks == 1:
        print (f"Move disk 1 from {from_pole} to {to_pole}")
    else:
        tower_of_hanoi(num_disks - 1,from_pole, to_pole, with_pole)
        print (f"Move disk {num_disks} from {from_pole} to {to_pole}")
        tower_of_hanoi(num_disks - 1, with_pole, from_pole, to_pole)

if __name__ == "__main__":
    tower_of_hanoi(4, "A", "B", "C")
