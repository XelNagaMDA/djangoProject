import json

from djangoProject.settings import PATH_TO_TASK_DATA_FILE


def get_all_tasks_from_json():
    """
    Extrage din fisier o lista de taskrui ca dictionare
    :param path:
    :return:
    """
    try:
        with open(PATH_TO_TASK_DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError as ex:
        # Fisierul nu a fost gasit, atunci probabil inca nu a fost creat,
        # lucram cu o lista ca date initiale
        return []


def save_tasks_to_json(list_of_tasks):
    """
    Salveaza o lista de taskuri intr-un fisier JSON dupa Path-ul stabilit
    :param list_of_tasks: lista de taskuri ca lista de dictionare
    :param path:
    :return:
    """
    with open(PATH_TO_TASK_DATA_FILE, 'w') as file:
        return json.dump(list_of_tasks, file)