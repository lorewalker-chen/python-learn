def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 位置调用
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
# 关键字调用
describe_pet(pet_name='harry', animal_type='hamster')
