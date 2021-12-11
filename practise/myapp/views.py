from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from myapp.forms import (AddAircraftForm,
                         AddWorkOrderForm,
                         AddAircraftModelForm,
                         AddTaskForm,
                         AddCustomerForm,
                         AddWorkContentForm,
                         )
from .models import (
    Aircraft,
    WorkOrder,
    ACModel,
    Task,
    Customer,
)

""" Home page view """

def home(request):
    return render(request, 'home.html', {})


""" Classes for Login and Register Users"""


class LoginPageView(View):
    """Login page view """
    def get(self, request):
        ctx = {}
        return render(request, 'login.html', ctx)


""" Simple form to register users"""


class RegisterPageView(View):
    """ Form to register users """
    login_url = 'members/register_user/'
    success_url = '/persons'

    def get(self, request):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
        ctx = {'form': form}
        return render(request, 'register.html', ctx)


""" Form to create new Work Content """


class AddWorkContentView(LoginRequiredMixin, View):
    """Form to add work content """
    def get(self, request):
        form = AddWorkContentForm()
        ctx = {"form": form}
        return render(request, "add_workcontent.html", ctx)

    def post(self, request):
        form = AddWorkContentForm(request.POST)
        if form.is_valid():
            workorder_id = form.cleaned_data["workorder_id"]
            task_id = form.cleaned_data["task_id"]
            customer = Customer.objects.create(
                workorder_id=workorder_id,
                task_id=task_id,
            )
            return redirect("add-workcontent")
        else:
            ctx = {"form": form}
            return render(request, "add_workcontent.html", ctx)


class AddCustomerView(LoginRequiredMixin, View):
    """Form to add customers"""
    def get(self, request):
        form = AddCustomerForm()
        ctx = {"form": form}
        return render(request, "add_customer.html", ctx)

    def post(self, request):
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            aircraft_id = form.cleaned_data["aircraft_id"]
            customer = Customer.objects.create(
                name=name,
                aircraft_id=aircraft_id,
            )
            return redirect("add-customer")
        else:
            ctx = {"form": form}
            return render(request, "add_customer.html", ctx)


class AddTaskView(LoginRequiredMixin, View):
    """Form to add tasks """
    def get(self, request):
        form = AddTaskForm()
        ctx = {"form": form}
        return render(request, "add_task.html", ctx)

    def post(self, request):
        form = AddTaskForm(request.POST)
        if form.is_valid():
            id_number = form.cleaned_data["id_number"]
            description = form.cleaned_data["description"]
            task_id = form.cleaned_data["task_id"]
            model = form.cleaned_data["model"]
            task = Task.objects.create(
                id_number=id_number,
                description=description,
                task_id=task_id,
                model=model,
            )
            return redirect("add-task")
        else:
            ctx = {"form": form}
            return render(request, "add_task.html", ctx)


class AddAircraftModelView(View):
    def get(self, request):
        form = AddAircraftModelForm()
        ctx = {"form": form}
        return render(request, "add_acmodel.html", ctx)

    def post(self, request):
        form = AddAircraftModelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            model = ACModel.objects.create(
                name=name,
            )
            return redirect("all-models")
        else:
            ctx = {"form": form}
            return render(request, "add_acmodel.html", ctx)


class AddProjectView(View):
    def get(request):
        return render(request, 'add_workorder.html', {})

    def post(self, request):
        pass


class AddAircraftView(View):
    """Form to add aircraft """
    def get(self, request):
        form = AddAircraftForm()
        ctx = {"form": form}
        return render(request, "add_aircraft.html", ctx)

    def post(self, request):
        form = AddAircraftForm(request.POST)
        if form.is_valid():
            serial_number = form.cleaned_data["serial_number"]
            current_registration = form.cleaned_data["current_registration"]
            model = form.cleaned_data["model_id"]
            aircraft = Aircraft.objects.create(
                serial_number=serial_number.upper(),
                current_registration=current_registration,
                model_id=model,
            )
            return redirect("all-aircrafts")
        else:
            ctx = {"form": form}
            return render(request, "add_aircraft.html", ctx)


class AddWorkOrderView(View):
    def get(self, request):
        form = AddWorkOrderForm()
        ctx = {"form": form}
        return render(request, "add_workorder.html", ctx)

    def post(self, request):
        form = AddWorkOrderForm(request.POST)
        if form.is_valid():
            wo_number = form.cleaned_data["wo_number"]
            registration_number = form.cleaned_data["registration_number"]
            customer_id = form.cleaned_data["customer_id"]
            work_order = WorkOrder.objects.create(
                wo_number=wo_number,
                registration_number=registration_number,
                customer_id=customer_id,
            )
            return redirect("all-workorders")

    # List of items


class AllCustomerView(View):
    def get(self, request):
        customers = Customer.objects.all()
        ctx = {"customers": customers}
        return render(request, "all_customers.html", ctx)


class AllAircraftView(LoginRequiredMixin, View):
    def get(self, request):
        aircrafts = Aircraft.objects.all()
        ctx = {"aircrafts": aircrafts}
        return render(request, "all_aircrafts.html", ctx)


class AllWorkOrderView(LoginRequiredMixin, View):
    def get(self, request):
        workorders = WorkOrder.objects.all()
        ctx = {"workorders": workorders}
        return render(request, 'workorder_list.html', ctx)


class AllAircraftModelView(LoginRequiredMixin, View):
    def get(self, request):
        models = ACModel.objects.all()
        ctx = {"models": models}
        return render(request, "all_models.html", ctx)



    # Show items


class ShowWorkOrder(View):
    def get(self, request, wo_id):
        work_order = WorkOrder.objects.get(pk=wo_id)
        return render(request, 'show_wo.html', {'work_order': work_order})


class ShowModelTasks(View):
    def get(self, request, model):
        ac_model = ACModel.objects.get(pk=model)
        tasks = ac_model.task_set.all()
        return render(request, 'show_acmodel.html', {'ac_model': ac_model, 'tasks': tasks})


class ShowAircraft(View):
    def get(self, request, aircraft_id):
        aircraft = Aircraft.objects.get(pk=aircraft_id)
        return render(request, 'show_aircraft.html', {'aircraft': aircraft})

    # Update classes


class UpdateWorkOrderView(View):
    def get(self, request, wo_id):
        wo = WorkOrder.objects.get(pk=wo_id)
        form = AddWorkOrderForm(request.POST or None, instance=wo)
        ctx = {'wo_number': wo,
               'form': form}
        return render(request, 'update_wo.html', ctx)

    def post(self, request, wo_id):
        wo = WorkOrder.objects.get(pk=wo_id)
        form = AddWorkOrderForm(request.POST or None, instance=wo)
        if form.is_valid():
            form.save()
            return redirect('all-workorders')


class UpdateAircraftView(View):
    """ Aircraft update form"""
    def get(self, request, aircraft_id):
        aircraft = Aircraft.objects.get(pk=aircraft_id)
        form = AddAircraftForm(request.POST or None, instance=aircraft)
        ctx = {'aircraft': aircraft,
               'form': form}
        return render(request, 'update_aircraft.html', ctx)

    def post(self, request, aircraft_id):
        aircraft = Aircraft.objects.get(pk=aircraft_id)
        form = AddAircraftForm(request.POST or None, instance=aircraft)
        if form.is_valid():
            form.save()
            return redirect('all-aircrafts')
        else:
            ctx = {"form": form}
            return render(request, 'update_aircraft.html', ctx)


""" Delete functions """


class DeleteWorkOrderView(View):
    def get(self, request, wo_id):
        wo = WorkOrder.objects.get(pk=wo_id)
        wo.delete()
        return redirect('all-workorders')


class DeleteAircraftView(View):
    def get(self, request, aircraft_id):
        aircraft = Aircraft.objects.get(pk=aircraft_id)
        aircraft.delete()
        return redirect('all-aircrafts')


class DeleteAircraftModelView(View):
    def get(self, request, model_id):
        model = ACModel.objects.get(pk=model_id)
        model.delete()
        return redirect('all-models')
