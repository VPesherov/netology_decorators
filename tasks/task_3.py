from tasks.task_1 import logger


@logger
def flag_generator(list_of_list):
    for item in list_of_list:
        for item_i in item:
            yield item_i
