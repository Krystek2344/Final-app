from random import sample
from models import Task
import pytz


def random_tasks():
    """Return 3 random Tasks from db."""
    tasks = list(Task.objects.all())
    return sample(tasks, 3)

