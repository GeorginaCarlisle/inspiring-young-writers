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
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']

            # Check title length
            if len(title) < 5:
                messages.error(
                    request, 
                    'Your title needs to more than 5 characters long to be published. Please add a little more.')
                context['create_writing_form'] = form
                return render(request, 'create_writing.html', context)

            # Check body length
            if len(body) <= 50:
                messages.error(
                    request, 
                    'Your writing needs to more than 50 characters long to be published. Please add a little more.')
                context['create_writing_form'] = form
                return render(request, 'create_writing.html', context)
            
            # Path if user clicked to Publish
            if 'publish' in request.POST:

                # If confirmation not recieved ask for
                if not request.GET.get('confirm'):
                    context['confirmation_needed'] = True
                    context['create_writing_form'] = form
                    return render(request, 'create_writing.html', context)

                # If confirmation recieved proceed
                else:
                    pending_approval = True
                    date_submitted = timezone.now()
                    author = request.user
                    slug = slugify(title)
                    updated_on = timezone.now()
                    form.save(author=author, slug=slug, updated_on=updated_on, pending_approval=pending_approval, date_submitted=date_submitted)
                    
                    messages.success(request, "You have successfully submitted your writing to be published")
                    return redirect('account_home')
                    
            # Path if user clicked to Save as draft
            else:
                author = request.user
                slug = slugify(title)
                updated_on = timezone.now()

                form.save(author=author, slug=slug, updated_on=updated_on)
                
                messages.success(request, "You have successfully saved your writing as a draft")
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


