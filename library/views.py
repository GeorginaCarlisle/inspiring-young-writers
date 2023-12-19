from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from writing.models import Writing
from .forms import GiveFeedbackForm
from .models import Feedback


"""
View for user to see all the writing that has been published
"""
@login_required
def library_view(request):

    context = {}

    work = Writing.objects.all()
    published_work = work.filter(approved = True).order_by('-date_approved')
    
    context['published_work'] = published_work

    return render(request, 'library.html', context)


"""
View to read an instance of published writing 
"""
@login_required
def read_view(request, writing_id):
        
    writing = get_object_or_404(Writing, pk=writing_id)

    context = {}

    context['writing'] = writing

    return render(request, 'read.html', context)


"""
View to create a new instance of feedback
"""
@login_required
def give_feedback_view(request, writing_id):

    writing = get_object_or_404(Writing, pk=writing_id)

    context = {}

    context['writing'] = writing

    # If form has been submitted
    if request.POST:
        form = GiveFeedbackForm(request.POST)

        if form.is_valid():
            star_one = form.cleaned_data['star_one']
            star_two = form.cleaned_data['star_two']
            wish = form.cleaned_data['wish']

            # Check star_one length
            if len(star_one) < 10:
                messages.error(
                    request, 
                    'Please add a little more to your first star')
                context['give_feedback_form'] = form
                return render(request, 'give_feedback.html', context)

            # Check star_two length
            if len(star_two) < 10:
                messages.error(
                    request, 
                    'Please add a little more to your second star')
                context['give_feedback_form'] = form
                return render(request, 'give_feedback.html', context)

            # Check wish length
            if len(wish) < 10:
                messages.error(
                    request, 
                    'Please add a little more to your wish')
                context['give_feedback_form'] = form
                return render(request, 'give_feedback.html', context)

            # If confirmation not recieved ask for
            if not request.GET.get('confirm'):
                context['confirmation_needed'] = True
                context['give_feedback_form'] = form
                return render(request, 'give_feedback.html', context)

            # If response to confirmation received
            else:
                
                # If submit confirmed
                if 'confirm' in request.POST:
                    giver = request.user
                    writing = writing
                    date_last_edit = timezone.now()
                    date_created = timezone.now()
                    
                    form.save(giver=giver, writing=writing, date_last_edit=date_last_edit, date_created=date_created)
                    
                    messages.success(request, "You have successfully submitted your feedback. It may take a couple of days to be approved")
                    return redirect('library')
                
                # If submit cancelled
                if 'cancel' in request.POST:
                    context['give_feedback_form'] = form
                    return render(request, 'give_feedback.html', context)
                    
        else:
            # Check for errors and return as a message
            star_one_form_errors = form.errors.get('star_one', None)
            star_two_form_errors = form.errors.get('star_two', None)
            wish_form_errors = form.errors.get('wish', None)

            if star_one_form_errors:
                messages.error(request, star_one_form_errors)
            if star_two_form_errors:
                messages.error(request, star_two_form_errors)
            if wish_form_errors:
                messages.error(request, wish_form_errors)
            context['give_feedback_form'] = form
    else:
        form = GiveFeedbackForm()
        context['give_feedback_form'] = form

    return render(request, 'give_feedback.html', context)
