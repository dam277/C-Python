import asyncio
import time
import threading

# ASYNC/AWAIT
# async def get_user_by_id(id):
#     print(f"get user by id: {id}")
#     await asyncio.sleep(2)
#     print("end")

# async def get_users():
#     print("get all users")
#     await asyncio.sleep(1)
#     print("end")

# async def main():
#     # ASYNC/AWAIT => Lancer une fonction et attendre sa réponse, ainsi lancer la deuxième et attendre sa réponse
#     await get_user_by_id(2)
#     await get_users()

#     # TASK => Lancer les deux fonctions de manière asynchrone
#     await asyncio.gather(get_user_by_id(3), get_users())
    

# TASKS
# async def main():
#     long_task = asyncio.create_task(long_task_runner())

#     short_task = await short_task_runner()
#     print(short_task)

#     await long_task
#     print(long_task.result())

    
# async def long_task_runner():
#     print("Started the long task")

#     # Start timer
#     start_time = time.time()
#     await asyncio.sleep(10)
#     # End timer
#     end_time = time.time()

#     # Calculate elapsed time
#     elapsed_time = end_time - start_time
#     return f"the long task finished in {elapsed_time} seconds"

# async def short_task_runner():
#     print("Started the short task")

#     # Start timer
#     start_time = time.time()
#     await asyncio.sleep(2)
#     # End timer
#     end_time = time.time()

#     # Calculate elapsed time
#     elapsed_time = end_time - start_time
#     return f"the short task finished in {elapsed_time} seconds"


# # # Exécuter le programme principal
# asyncio.run(main())

# THREADING
def make_task(x):
    print(f"Started the task {x}")
    # Start timer
    start_time = time.time()

    time.sleep(5)

    # End timer
    end_time = time.time()
    elapsed_time = end_time - start_time

    return f"the task {x} finished in {elapsed_time} seconds"

if __name__ == "__main__":
    for x in range(5):
        th = threading.Thread(target=make_task, args=(x, ))
        th.start()

    print("launched all threads")




