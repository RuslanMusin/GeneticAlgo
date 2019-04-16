import owlready2
from owlready2 import *

owlready2.JAVA_EXE = "C:\\Program Files\\Java\\jdk-11.0.2\\bin\\java.exe"
onto_path.append("/path/to/your/local/ontology/repository")
onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl")
onto.load()


class NonVegetarianPizza(onto.Pizza):
    equivalent_to = [
        onto.Pizza
        & (onto.has_topping.some(onto.MeatTopping)
           | onto.has_topping.some(onto.FishTopping)
           )]

    def eat(self): print("Beurk! I'm vegetarian!")


test_pizza = onto.Pizza("test_pizza_owl_identifier")
test_pizza.has_topping = [onto.CheeseTopping(),
                          onto.TomatoTopping()]
test_pizza.has_topping.append(onto.MeatTopping())
sync_reasoner()
print(test_pizza.__class__)
test_pizza.eat()

with onto:
    class BodyPart(Thing): pass


    class part_of(BodyPart >> BodyPart, TransitiveProperty): pass


abdomen = BodyPart("abd")
heart = BodyPart("heart", part_of=[abdomen])
left_ventricular = BodyPart("left_ventricular", part_of=[heart])
kidney = BodyPart("kidney", part_of=[abdomen])

print(left_ventricular.part_of)
print(left_ventricular.INDIRECT_part_of)
