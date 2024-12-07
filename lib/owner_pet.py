class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self,name,pet_type,owner =None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(F"the pet type is not the one available, {pet_type} must belong to {Pet.PET_TYPES}")
        self.pet_type = pet_type
        self.name = name
        self.owner = owner
        Pet.all.append(self)
        
        
       
        pass
    pass

class Owner:

    def __init__(self,name):
        self.name = name
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    def add_pet(self,pet):
        if isinstance(pet,Pet):
            pet.owner = self
        else:
            raise Exception(f"The pet '{pet}' is not a valid pet, please enter a new one")
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet:pet.name)