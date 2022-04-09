from collections import deque

class Veterinarian:

    def __init__(self) -> None:
        self.pet_queue = deque()

    def accept(self, petName):
        self.pet_queue.append(petName)

    def heal(self):
        try:
            return self.pet_queue.popleft()
        except IndexError:
            return "Empty Pet Line"



if __name__ == "__main__":
    veterinarian = Veterinarian()
    print(veterinarian.heal())
    veterinarian.accept("Barkley")
    veterinarian.accept("Mittens")
    print(veterinarian.heal())
    print(veterinarian.heal())
    print(veterinarian.heal())