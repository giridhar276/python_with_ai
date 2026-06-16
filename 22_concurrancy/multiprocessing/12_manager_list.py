"""
Multiprocessing Example 12: Manager List

Concept:
Manager can create shared objects like list and dictionary.
"""

import multiprocessing


def add_item(shared_list, item):
    shared_list.append(item)


if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        shared_list = manager.list()
        processes = []

        for item in ["Python", "Pandas", "ML", "AI"]:
            process = multiprocessing.Process(target=add_item, args=(shared_list, item))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        print("Shared list:", list(shared_list))
