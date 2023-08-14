from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo.tasks import get_tasks, task_to_dict, add_task, mark_tasks_as_completed


@api_view(["GET"])
def get_todo_list(request):
    tasks = get_tasks()
    if tasks:
        tasks = [task_to_dict(a) for a in tasks]
        return Response(tasks, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def add_task_to_list_view(request):
    try:
        add_task(request.data['title'])
    except ValueError as ex:
        return Response(data=str(ex), status=status.HTTP_400_BAD_REQUEST)
    except KeyError as ex:
        return Response(data=f"{ex} was not specified in the request data", status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["POST"])
def complete_task(request):
    try:
        mark_tasks_as_completed(int(request.data.get('id')))
    except ValueError:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response("Task marked as completed")