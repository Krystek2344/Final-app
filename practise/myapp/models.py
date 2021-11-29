from django.db import models
from django.contrib.auth.models import User

ROLE_CHOICES = (
    (1, "Planista"),
    (2, "Mechanik"),
    (3, "Jakościowiec"),
    (4, "Dyrektor"),
)


class ACModel(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Aircraft(models.Model):
    serial_number = models.CharField(max_length=64)
    current_registration = models.CharField(max_length=10)
    model_id = models.ForeignKey(ACModel, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.current_registration


class Customer(models.Model):
    name = models.CharField(max_length=64)
    aircraft_id = models.ForeignKey(Aircraft, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WorkOrder(models.Model):
    wo_number = models.CharField(max_length=64)
    registration_number = models.ForeignKey(Aircraft, null=True, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.wo_number


class Task(models.Model):
    id_number = models.CharField(max_length=8)
    description = models.TextField(max_length=275)
    task_id = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    model_id = models.ForeignKey(ACModel, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_number


class WorkContent(models.Model):
    workorder_id = models.ForeignKey(WorkOrder, null=True, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, null=True, on_delete=models.CASCADE)
    # done_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    # checked_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)



