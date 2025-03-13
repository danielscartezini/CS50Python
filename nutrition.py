fruit_dict = {
    "apple" : "130",
    "avocado" : "50",
    "banana" : "110",
    "cantaloupe" : "50",
    "grapefruit" : "50",
    "grape" : "90",
    "honeydew melon" : "50",
    "kiwifruit" : "90",
    "lemon" : "15",
    "lime" : "20",
    "nectarine" : "60",
    "orange" : "80",
    "peach" : "60",
    "pear" : "100",
    "pineapple" : "50",
    "plums" : "70",
    "strawberry" : "50",
    "plums" : "70",
    "sweet cherries" : "100",
    "tangerine" : "50",
    "watermelon" : "80"
}
fruit = input("Item: ").lower()
if fruit_dict.get(fruit):
    print("Calories: ", fruit_dict.get(fruit))
