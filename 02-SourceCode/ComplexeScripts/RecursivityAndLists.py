# Create a list
my_list = [1, 2, 3, 4, 5]

# Create a generator expression
gen = (x for x in my_list)

print(gen)  # Output: <generator object <genexpr> at 0x7fdaa9a7c9e0>

for i in gen:
    print(i)  # Output: 1 2 3 4 5
print("-----------------------------------")
for i in gen:
    print(i)  # Output: 1 2 3 4 5

print(gen)

# # Now we can use the next() function to get the next value from the generator
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2



command = next(command for command in Command.commands if command["name"] == name)


# => RECURSIVE FUNCTION THAT GET A PARENT COMMAND WHICH GET HIS CHILDREN COMMANDS AND SO ON AND FINALY RETURN THE COMMANDS LIST WITH THE GOOD ORDER LIKE SO :
# [command1 : {name, children : [{name1.1, children :[]}, {name1.2, children : []}]}]

f"""
EXAMPLE OF A COMMANDS LIST :
[
  {'name': 'setup', 'description': 'Setup the server to the database', 'parent': None, 'params': {}, 'children': 
      [
          {'name': 'subSetup1', 'description': 'Setup the server to the database', 'parent': 'setup', 'params': {}, 'children': 
              [
                  {'name': 'subSetup1Child', 'description': 'Setup the server to the database', 'parent': 'subSetup1', 'params': {}}
              ]
          }, 
          {'name': 'subSetup2', 'description': 'Setup the server to the database', 'parent': 'setup', 'params': {}}
      ]
  }, 
  {'name': 'asas', 'description': 'Setup the server to the database', 'parent': None, 'params': {}, 'children': 
      [
          {'name': 'asasas', 'description': 'Setup the server to the database', 'parent': 'asas', 'params': {}}
      ]
  }
]
"""

# Get commands by parent function with recursivity
@staticmethod
def get_ordered_commands():
    """ # Get ordered commands function

    Description :
    ---
        Get a command by his parent

    Access : 
    ---
        src.bots.server_manager.commands.Command.py\n
        Command.get_command_by_parent()

    Parameters :
    ---
        parent : :class:`str` => Parent of the command to get

    Returns : 
    ---
        :class:`Command` => Command with the parent sended
    """
    # Get the top commands
    top_commands = [command for command in Command.commands if not command.get("parent")]
    children_commands = [command for command in Command.commands if command.get("parent")]
    print("Top : ", top_commands)
    print("Children : ", children_commands)
    print("----------------get_children()-------------------")

    def get_children(command: dict):
        print(f"{Fore.LIGHTBLUE_EX} Command : ", command)
        # Get all the commands with a parent
        subcommands = [subcommand for subcommand in children_commands if subcommand.get("parent") == command.get("name")]
        print(f"{Fore.LIGHTMAGENTA_EX}Subcommands : ", subcommands)
                    
        print(f"{Fore.LIGHTCYAN_EX} BASE COMMAND :", command)


        for subcommand in subcommands:
            print(f"{Fore.GREEN} SUBCOMMAND : ", subcommand)
            print(f"{Fore.RED} All commands BEFORE : ", command)
            print(f"{Fore.LIGHTCYAN_EX} CHILDREN :", command.get("children"))
            if not command.get("children"):
                command.update({"children": []})
            command.get("children").append(get_children(subcommand))
            # command.update({subcommand.get("name"): get_children(subcommand)})
            print(f"{Fore.LIGHTYELLOW_EX} All commands AFTER: ", command)

        print(f"{Fore.LIGHTWHITE_EX} RETURNS THE COMMAND : ", command)
        return command
    
    commands = []
    for command in top_commands:
        commands.append(get_children(command))

    print(f"{Fore.LIGHTYELLOW_EX}FINAL COMMANDS :", commands)