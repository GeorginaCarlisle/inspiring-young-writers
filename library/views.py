from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from writing.models import Writing


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
