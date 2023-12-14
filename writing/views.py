from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.utils import timezone
from .forms import CreateWritingForm
from .models import User, Writing

"""
View to create a new instance of writing
"""
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
            form_errors = form.errors.get('title', None)
            if form_errors:
                messages.error(request, form_errors)
            else:
                messages.error(
                    request,
                    'There is an error with your title or writing')
            context['create_writing_form'] = form
    else:
        form = CreateWritingForm()
        context['create_writing_form'] = form

    return render(request, 'create_writing.html', context)


"""
View for user to see all their saved writing
"""
@login_required
def my_writing_view(request, user_id):

    # Check that the logged in user id matches the user_id from the url
    if request.user.id != user_id:
        messages.error(request, 'You have been returned to your account home page, \
                       as you were trying to access a page you are not authorised to view.')
        return redirect('account_home')

    context = {}

    user = User.objects.get(id=user_id)
    work = user.writing.all()
    published_work = work.filter(approved = True).order_by('-date_approved')
    awaiting_approval = work.filter(pending_approval = True).order_by('-date_submitted')
    failed_approval = work.filter(failed_approval = True).order_by('-date_failed')
    draft = work.filter(approved = False, pending_approval = False).order_by('-updated_on')



    context['published_work'] = published_work
    context['awaiting_approval'] = awaiting_approval
    context['failed_approval'] = failed_approval
    context['drafts'] = draft

    return render(request, 'my_work.html', context)


"""
View to edit an instance of writing
"""
@login_required
def edit_writing_view(request, writing_id):
    
    writing = get_object_or_404(Writing, pk=writing_id)

    context = {}

    # Check that the logged in user id matches the user_id from the url
    if request.user != writing.author:
        messages.error(request, 'You have been returned to your account home page, \
                       as you were trying to access a page you are not authorised to view.')
        return redirect('account_home')

    # If form has been submitted
    if request.POST:
        form = CreateWritingForm(request.POST, request.FILES, instance=writing)

        # Path if user clicked to delete
        if 'delete' in request.POST:

            # If confirmation not recieved ask for
            if not request.GET.get('confirm_delete'):
                context['confirmation_delete_needed'] = True
                context['create_writing_form'] = form
                context['work_id'] = writing_id
                return render(request, 'edit_writing.html', context)

            # If confirmation recieved proceed
            else:
                writing.delete()
                messages.success(request, "You have successfully deleted your writing")
                return redirect('my_work', user_id=request.user.id)
            
        # Path is user clicks to NOT delete, only available if initially clicked to delete
        if 'keep' in request.POST:
                context['create_writing_form'] = form
                context['work_id'] = writing_id
                return render(request, 'edit_writing.html', context)

        # Save as draft and submit to publish pathways
        if form.is_valid():

            # Path if user clicked to Publish
            if 'publish' in request.POST:

                # If confirmation not recieved ask for
                if not request.GET.get('confirm'):
                    context['confirmation_needed'] = True
                    context['create_writing_form'] = form
                    context['work_id'] = writing_id
                    return render(request, 'edit_writing.html', context)

                # If confirmation recieved proceed
                else:
                    pending_approval = True
                    date_submitted = timezone.now()
                    updated_on = timezone.now()
                    form.save(updated_on=updated_on, pending_approval=pending_approval, date_submitted=date_submitted)
                    
                    messages.success(request, "You have successfully submitted your writing to be published")
                    return redirect('account_home')
                    
            # Path if user clicked to Save as draft
            elif 'draft' in request.POST:
                updated_on = timezone.now()
                form.save()
                messages.success(request, f'You have successfully saved "{writing.title}" as a draft.')
                return redirect('my_work', user_id=request.user.id)
            
        else:
            messages.error(
                request,
                'There is an error with your title or writing')
            context['create_writing_form'] = form
            context['work_id'] = writing_id

    else:
        form = CreateWritingForm(instance=writing)
        context['create_writing_form'] = form
        context['work_id'] = writing_id

    return render(request, 'edit_writing.html', context)