import asyncio

async def divide(first: int, second: int):
    """
    # Divide function
    /!\\ This is a coroutine, it needs to be awaited
    
    Description :
    ---
        Divide two numbers and return the result
    
    Access : 
    ---
        function_comments.py => divide()

    Parameters : 
    ---
        - first : :class:`int` => First number which will be divided
        - second : :class:`int` => The divide number

    Returns : 
    ---
        :class:`int` => Result of the division

    Raises : 
    ---
        :class:`ZeroDivisionError`
    """
    result = 0

    try:
        result = first / second 
    except ZeroDivisionError:
        print("Error there is a division by zero")

    return result


print(asyncio.run(divide(8, 2)))
print(asyncio.run(divide(7, 0)))


def template():
    """ # Name
    /!\\ This is a coroutine, it needs to be awaited
    
    Description :
    ---
    
    Access : 
    ---

    Parameters : 
    ---

    Returns : 
    ---

    Raises : 
    ---
    """

class Template:
    """ # Note class
        
    Description :
    ---
        Manage database notes to use database with some specific function to retrieve some datas

    Access : 
    ---
        src.database.models.tables.Note.py\n
        Note

    inheritance : 
    ---
        - Table : :class:`Table` => Parent class of database tables
    """