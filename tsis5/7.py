def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)

snake_str = input("Enter a snake case string: ")
camel_str = snake_to_camel(snake_str)
print("Camel case string:", camel_str)