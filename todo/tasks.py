"""
Task:

id: int
title: str
created_at: str | datetime
completed_at: str | datetime
deleted: bool
"""
from collections import namedtuple
from datetime import datetime

from djangoProject.constants import DATE_TIME_FORMAT
from todo.data import get_all_tasks_from_json, save_tasks_to_json

Task = namedtuple('Task', [
    'id',
    'title',
    'created_at',
    'completed_at',
    'deleted',
])


def task_to_dict(task: Task) -> dict:
    """
    Functie care transforma un Task din named-tuple in dictionar
    Necesar pentru a stoca datele intr-un JSON
    :param task:
    :return:
    """
    return dict(
        id=task.id,
        title=task.title,
        # Salvam valorile de tip date-time ca string
        created_at=task.created_at.strftime(DATE_TIME_FORMAT),
        completed_at=task.completed_at.strftime(DATE_TIME_FORMAT) if task.completed_at else None,
        deleted=task.deleted,
    )


def task_from_dict(task: dict) -> Task:
    """
    Functie care transforma taskul din
    Dictionar (din JSON) intr-un named tuple
    Named-tuple este folosit pentru a lucra cu task-ul in cadrul programului
    """
    return Task(
        id=task['id'],
        title=task['title'],
        # Convertim valorile din string in datetime
        # Pentru a lucra cu ele mai usor in cadrul programului
        created_at=datetime.strptime(task['created_at'], DATE_TIME_FORMAT),
        completed_at=datetime.strptime(task['completed_at'], DATE_TIME_FORMAT) if task['completed_at'] else None,
        deleted=task['deleted'],
    )


def add_task(task_title):
    """
    Functia care adauga un task
    :param path:
    :param task_title:
    :return:
    """
    # Folosim titlul din argumente
    if not task_title:
        raise ValueError('Tasks must have a title')
    title = task_title
    # Extragem lista de taskuri din JSON pentru a o actualiza
    tasks_list = get_all_tasks_from_json()
    # Cream un task nou
    new_task = Task(
        id=len(tasks_list),
        title=title,
        created_at=datetime.now(),
        completed_at=None,
        deleted=False
    )
    # Transformam in dict pentru a stoca in JSON
    new_task = task_to_dict(new_task)
    # Adaugam in JSON
    tasks_list.append(new_task)
    # Salvam datele in fisier
    save_tasks_to_json(tasks_list)


def get_tasks(show_completed=False, deleted=False) -> list:
    """
    Functia care intoarce o lista de taskuri, din fisier,
     transformate in namedTuple-u de Task. Lista este filtrata dupa daca sunt completate sau sterse.
    :param show_completed: Daca aratam doar taskurile completate
    :param deleted: daca aratam doar taskurile sterse
    :return:
    """
    tasks_list = [task_from_dict(task) for task in get_all_tasks_from_json()]
    task_filtered = list(filter(
        lambda el: el.deleted == deleted and bool(el.completed_at) == show_completed,
        tasks_list
    ))
    return task_filtered


def list_tasks(path, show_completed=False):
    """
    Afisam toate taskurile complete sau incomplete
    :param path:
    :param show_completed:
    :return:
    """
    # Filtram lista de taskuri
    task_filtered = get_tasks(show_completed)
    # Afisam un mesaj initial, sa fie clar "ce" noi afisam.
    print(f'Listing all the {"completed" if show_completed else "uncompleted"} tasks.')
    if not len(task_filtered):
        # Afisam un mesaj in caz ca nu sunt taskuri de loc
        print(f'No {"completed" if show_completed else "uncompleted"} tasks ')
        return
    for index, task in enumerate(task_filtered):
        # Afisam atit taskul, cat si indicele lui
        task_str = f"[{task._title}] created at: [{task.created_at.strftime(DATE_TIME_FORMAT)}]"
        print_args = [index, task_str]
        if show_completed:
            # In caz ca taskul e completat, adaugam si timpul pentru completare
            print_args.append(
                f"Took: {task.completed_at - task.created_at}"
            )
        # Despachetam lista de argumente pentru PRINT
        print(*print_args, sep=' | ')


def find_task_by_id(list_of_tasks, task_id):
    """
    Gasim un task din-tro lista conform ID-ului si intoarcem intregul task
    :param list_of_tasks:
    :param task_id:
    :return:
    """
    for task in list_of_tasks:
        if task.id == task_id:
            return task
    raise IndexError("Task not found")


def mark_tasks_as_completed(task_id):
    """
    Functia are scoupul sa gaseasca task-ul care trebuie de marcat ca complet si sa-l marcheze ca complet
    :return:
    """
    all_task = [task_from_dict(a) for a in get_all_tasks_from_json()]
    # Gasim din lista de toate taskurile, elementul dupa id-ul taskului pe care il finisam
    task_to_change = find_task_by_id(all_task, task_id)
    task_index_in_all = all_task.index(task_to_change)
    # avand indexul taskului in lista din fisier, putem re-scrie taskul cu informatie noua
    all_task[task_index_in_all] = Task(
        id=task_to_change.id,
        title=task_to_change.title,
        created_at=task_to_change.created_at,
        # Pastram toata informatia cu exceptia la completed_at
        completed_at=datetime.now(),
        deleted=task_to_change.deleted
    )
    # Re-transformam totul in dictionare pentru a stoca in fisier
    all_task = [task_to_dict(a) for a in all_task]
    # Stocam in fisier
    save_tasks_to_json(all_task)