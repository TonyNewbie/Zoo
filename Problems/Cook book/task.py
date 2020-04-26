pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"
ingredients = input()
if ingredients in pasta:
    print('You can make pasta')
if ingredients in apple_pie:
    print('You can make apple pie')
if ingredients in ratatouille:
    print('You can make ratatouille')
if ingredients in chocolate_cake:
    print('You can make chocolate cake')
if ingredients in omelette:
    print('You can make omelette')
