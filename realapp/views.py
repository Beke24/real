from django.shortcuts import render,redirect
from .models import atendance,task
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .forms import CustomUserCreationForm
from datetime import datetime
# Create your views here. 
def home(request):
    return render(request, 'home.html')


@login_required
def dashboard(request):
    last_click = atendance.objects.filter(user=request.user).order_by('-date').first()
    is_disabled = False

    if last_click:
        time_elapsed = (now() - last_click.date).total_seconds()
        if time_elapsed < 14400:  # less than 4 hr
            is_disabled = True

    if request.method == "POST" and not is_disabled:
        attendance = atendance(user=request.user)
        attendance.save()
        
        return redirect('dashboard')  # Redirect to clear the POST request
    tasks = task.objects.filter(user=request.user)
    
        
    context = {
        "is_disabled": is_disabled,
        "date": datetime.now(),
        'tasks': tasks,
        
    }
    
    return render(request, "dashboard.html", context)

    #return render(request, "dashboard.html", {"is_disabled": is_disabled})
 # import if you have CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():
            user = form.save()

            return redirect('login')  
    else:
        form = CustomUserCreationForm()  
    return render(request, 'signup.html', {'form': form})
# Home View
def home(request):
   
    return render(request, 'home.html')


    
