from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.utils import timezone
from .forms import CreateWritingForm


@login_required
def create_writing_view(request):

    context = {}
    # If form has been submitted
    if request.POST:
        form = CreateWritingForm(request.POST)
        if form.is_valid():
            title = title
            body = body
            author = request.user
            slug = slugify(title)
            updated_on = timezone.now
            pending_approval = True
            date_submitted = timezone.now
            form.save(author=author, slug=slug, updated_on=updated_on, pending_approval=pending_approval, date_submitted=date_submitted)
            
            messages.success(request, "You have successfully submitted your writing to be published")
            return redirect('account_home')
        else:
            messages.error(
                request,
                'There is an error with your title or writing')
            context['create_writing_form'] = form
    else:
        form = CreateWritingForm()
        context['create_writing_form'] = form

    return render(request, 'create_writing.html', context)


