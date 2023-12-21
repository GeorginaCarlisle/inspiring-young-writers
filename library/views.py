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

    # create a list of all users who have given feedback
    feedback_received = writing.received_feedback.all()
    given_feedback = []
    for feedback in feedback_received:
        giver = feedback.giver.username
        given_feedback.append(giver)

    context = {}

    context['writing'] = writing
    context['given_feedback'] = given_feedback

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
                    
                    messages.success(
                        request,
                        f'You have successfully submitted your feedback for "{writing}". It may take a couple of days to be approved.')
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


"""
View to view the feedback asscoiated with an instance of writing
Called from read page
"""
@login_required
def read_feedback_view(request, writing_id):
        
    writing = get_object_or_404(Writing, pk=writing_id)

    approved_feedback = writing.received_feedback.all().filter(approved = True)

    context = {}

    # locate any instances of feedback for the logged in user
    all_feedback = writing.received_feedback.all()
    for feedback in all_feedback:
        if feedback.giver.username == request.user.username:
            user_feedback = feedback
            context['user_feedback'] = user_feedback

    context['writing'] = writing
    context['feedback_received'] = approved_feedback
    
    return render(request, 'read_feedback.html', context)


"""
View to edit an instance of feedback created by the logged in user
Called from read page
"""
@login_required
def edit_feedback_view(request, feedback_id):
        
    feedback = get_object_or_404(Feedback, pk=feedback_id)
    writing_id = feedback.writing.id
    writing = get_object_or_404(Writing, pk=writing_id)

    context = {}

    context['writing'] = writing
    context['feedback'] = feedback

    # Check that the logged in user id matches the giver of the feedback
    if request.user != feedback.giver:
        messages.error(request, 'You have been returned to your account home page, \
                       as you were trying to access a page you are not authorised to view.')
        return redirect('account_home')
    

    # If form has been submitted
    if request.POST:
        form = GiveFeedbackForm(request.POST, request.FILES, instance=feedback)

        if form.is_valid():
            star_one = form.cleaned_data['star_one']
            star_two = form.cleaned_data['star_two']
            wish = form.cleaned_data['wish']

            # Check star_one length
            if len(star_one) < 10:
                messages.error(
                    request, 
                    'Please add a little more to your first star')
                context['edit_feedback_form'] = form
                return render(request, 'edit_feedback.html', context)

            # Check star_two length
            if len(star_two) < 10:
                messages.error(
                    request, 
                    'Please add a little more to your second star')
                context['edit_feedback_form'] = form
                return render(request, 'edit_feedback.html', context)

            # Check wish length
            if len(wish) < 10:
                messages.error(
                    request, 
                    'Please add a little more to your wish')
                context['edit_feedback_form'] = form
                return render(request, 'edit_feedback.html', context)

            # If confirmation not recieved ask for
            if not request.GET.get('confirm'):
                context['confirmation_needed'] = True
                context['edit_feedback_form'] = form
                return render(request, 'edit_feedback.html', context)

            # If response to confirmation received
            else:
                
                # If submit confirmed
                if 'confirm' in request.POST:
                    date_last_edit = timezone.now()
                    approved = False
                    form.save(date_last_edit=date_last_edit, approved=approved)
                    
                    messages.success(
                        request,
                        f'You have successfully editted your feedback for "{feedback.writing}". It may take a couple of days to be approved.')
                    return redirect('library')
                
                # If submit cancelled
                if 'cancel' in request.POST:
                    context['edit_feedback_form'] = form
                    return render(request, 'edit_feedback.html', context)
                    
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
            context['edit_feedback_form'] = form
    else:
        form = GiveFeedbackForm(instance=feedback)
        context['edit_feedback_form'] = form

    return render(request, 'edit_feedback.html', context)

    
"""
View to delete an instance of feedback
"""
@login_required
def delete_feedback_view(request, feedback_id):
        
    feedback = get_object_or_404(Feedback, pk=feedback_id)

    context = {}

    # Check that the logged in user id matches the user_id from the url
    if request.user != feedback.giver:
        messages.error(request, 'You have been returned to your account home page, \
                       as you were trying to access a page you are not authorised to view.')
        return redirect('account_home')
    

    # If confirmation not recieved ask for
    if not request.GET.get('confirm_delete'):

        # Gather all info needed to refresh the read_feedback page with confirmation message
        writing_id = feedback.writing.id
        writing = get_object_or_404(Writing, pk=writing_id)
        approved_feedback = writing.received_feedback.all().filter(approved = True)

        # locate any instances of feedback for the logged in user
        all_feedback = writing.received_feedback.all()
        for feedback in all_feedback:
            if feedback.giver.username == request.user.username:
                user_feedback = feedback
                context['user_feedback'] = user_feedback

        context['writing'] = writing
        context['feedback_received'] = approved_feedback
        context['confirmation_delete_needed'] = True

        return render(request, 'read_feedback.html', context)

    # If confirmation recieved proceed
    else:
        feedback.delete()
        writing_id = feedback.writing.id
        messages.success(request, "You have successfully deleted your feedback")
        return redirect('read_feedback', writing_id=writing_id) 
