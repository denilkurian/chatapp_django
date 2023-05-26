from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ChatModel,Personal

from django.contrib.auth.models import User

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

########### index page
@login_required
def index(request):
    users = User.objects.exclude(username=request.user.username)
    personal_objects = Personal.objects.all()
    return render(request, 'index.html', context={'users': users,'personal_objects': personal_objects})



######### chat page where users interact with each other
@login_required
def chatPage(request, username):
    try:
        user_obj = User.objects.get(username=username)
        users = User.objects.exclude(username=request.user.username)
        personal_objects = Personal.objects.all()

        if request.user.id > user_obj.id:
            thread_name = f'chat_{request.user.id}-{user_obj.id}'
        else:
            thread_name = f'chat_{user_obj.id}-{request.user.id}'
        message_objs = ChatModel.objects.filter(thread_name=thread_name)

        return render(request, 'main_chat.html', context={'users': users, 'user': user_obj, 'messages': message_objs, 'personal_objects': personal_objects})

    except User.DoesNotExist:
        return HttpResponse("User does not exist.")




########### signup or registration
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not same!!")
        else:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Your account has been successfully created.")

            return redirect("/")
    return render(request, 'signup.html')



############# login/Access
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(request, username=username, password=pass1)
        messages.success(request, ' Logged in successfully.')
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("username or password is incorrect!!!")
    return render(request, 'login.html')


############## logout
def signout(request):
    logout(request)
    messages.success(request, 'Logout successfully.')
    return redirect('/')




########## search filtering if user existing or not
class Filter(LoginRequiredMixin,ListView):
    model = User
    template_name = 'searchuser.html'
    context_object_name = 'users'

    def get_queryset(self):
        query = self.request.GET.get('q')
        users = User.objects.filter(Q(username=query))
        return users

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        personal_objects = Personal.objects.all()
        context['personal_objects'] = personal_objects
        return context



########### autocomplete recommendation using AJAX
def autocomplete_username(request):
    if 'term' in request.GET:
        term = request.GET.get('term')
        users = User.objects.filter(username__istartswith=term)
        usernames = list(users.values_list('username', flat=True))
        return JsonResponse(usernames, safe=False)
    return JsonResponse([])



############### For creating,listing,updating, deleting dp and status for each users
class Personals(LoginRequiredMixin,ListView):
    model= Personal
    fields="__all__"
    context_object_name = 'personal'
    template_name='personal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personal'] = context['personal'].filter(user=self.request.user)
        return context



class Create(LoginRequiredMixin,CreateView):
    model = Personal
    fields = ['image','status']
    template_name = 'personal-create.html'
    success_url = reverse_lazy('list')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Create, self).form_valid(form)


class Update(LoginRequiredMixin,UpdateView):
    model = Personal
    fields = ['image', 'status']
    success_url = reverse_lazy('list')
    template_name = 'personal-create.html'

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
class Delete(LoginRequiredMixin,DeleteView):
    model = Personal
    fields = ['image', 'status']
    success_url = reverse_lazy('list')
    template_name = 'personal.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())




##################
###################
####################






