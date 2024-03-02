from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from website_project.web.forms import ProfileEditForm

from website_project.web.models import CustomUser


class AccountEdit(View):
    def get(self, request, username):
        profile = get_object_or_404(CustomUser, username=username)
        if profile.username != request.user.username:
            return redirect('account:account-details', username=username)

        if request.method == 'POST':
            form = ProfileEditForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()

                return redirect('account:account-details', username=username)
        else:
            form = ProfileEditForm(instance=profile)

        context = {
            'user': profile,
            'form': form
        }

        return render(request, 'account/account-edit.html', context)

    def post(self, request, username):
        profile = get_object_or_404(CustomUser, username=username)
        return redirect('account:account-edit', username=profile.username)


class AccountView(View):
    def get(self, request, username):
        profile = get_object_or_404(CustomUser, username=username)
        editable = False

        if request.user.is_authenticated:
            if profile.username == request.user.username:
                editable = True

        return redirect('account:account-edit', username=username)






