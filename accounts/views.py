from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.shortcuts import render, get_object_or_404, redirect

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

@login_required
def edit_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    password = user.password
    if request.method=='POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            user=form.save(commit=False)
            user.password = password
            user.save()
            return redirect('accounts:edit_user', pk)
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'edit_user.html', {'form':form,
                                            'user':user})


@login_required
def account_info(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    return render(request, 'account_info.html', {'user': user})
