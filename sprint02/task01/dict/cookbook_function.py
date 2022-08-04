# DESCRIPTION:
# Create a script with a function search_cookbook(), which takes in three arguments: cookbook, recipe, and section, the cookbook is a dict of dicts.
# The function looks for an item in the cookbook dict with recipe as the key.
# If found, it then looks for an item in the recipe dict with section as the key.
# On success, the function returns the found item.
# If there is no recipe in the cookbook, the function returns the string: 'There is no "[recipe]" recipe in the cookbook.'
# If there is no item with section key in the recipe, the function returns the string: 'There is no section "[section]" in the "[recipe]" recipe.'

##############
# NOTE: The function must use the method get().

def search_cookbook(cookbook, recipe, section):

    if recipe in cookbook.keys():
        recipe_value = cookbook.get(recipe)
        if section in recipe_value:
            return recipe_value.get(section)

        elif section not in recipe_value:
            return f'There is no section "{section}" in the "{recipe}" recipe.'

    elif recipe not in cookbook.keys():
        return f'There is no "{recipe}" recipe in the cookbook.'


