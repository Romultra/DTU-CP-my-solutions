"""A small example of how to use the super()-keyword."""
class Pet: 
    """A basic Pet-class."""

    def __init__(self, name, age):  
        """Create a new Pet object.

        :param name: The name of the Pet
        :param age: The age of the Pet.
        """
        self.name = name 
        self.age = age

    def __str__(self): 
        """
        Automatically called by ``print(..)``.

        :return: A string representation such as ``"Fido (3 years old)"``.
        """
        return f"{self.name} ({self.age} years old)"  

class SimpleCat(Pet):
    """A simple Cat-class. This example contains duplicated code."""

    def __init__(self, name, age, favorite_food): 
        """Construct a new Cat-object. Asides the name and age, it also has a favorite food.

        :param name: The name of the cat, for instance ``'Mr. Whiskers'``
        :param age: The age, for instance 3.
        :param favorite_food: The favorite food, for instance ``"fish"``.
        """
        self.name = name 
        self.age = age
        self.favorite_food = favorite_food

class ImprovedCat(Pet):
    """The ImprovedCat uses super() to avoid duplicate code."""

    def __init__(self, name, age, favorite_food): 
        """Construct a new Cat-object. The example function similar to the one before.

        :param name: The name of the cat, for instance ``'Mr. Whiskers'``
        :param age: The age, for instance 3.
        :param favorite_food: The favorite food, for instance ``"fish"``.
        """
        super().__init__(name, age)         # Call the Pet.__init__()-method. 
        self.favorite_food = favorite_food  # We stll need to store this one. 


if __name__ == "__main__":
    a = SimpleCat("Mr. Whiskers", 3, "fish")
    print(a)
    print(a.favorite_food)
    # Now let's make an improved cat.

    b = SimpleCat("Mr. Super-duper whiskers", 4, "whatever you are eating")
    print(b)
    print(b.favorite_food)
