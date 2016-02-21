from django.shortcuts import render, get_object_or_404
from .models import Poll
from django.shortcuts import redirect
from .forms import PollForm
from django.utils import timezone

# Create your views here.
def poll_list(request):
  if request.method == "POST":
    vote = request.POST.get("submit")
    pk = request.POST.get("key")
    poll = get_object_or_404(Poll, pk=pk)
    
    if vote == 'YES':
      poll.yes_votes = poll.yes_votes+1
    elif vote == 'NO':
      poll.no_votes = poll.no_votes+1
    poll.save()
    #post.author = request.user
    #post.published_date = timezone.now()
    #post.save()
    
  polls = Poll.objects.all()
  return render(request, 'vote/templates/poll_list.html', {'polls':polls})

def poll_new(request):
  if request.method == "POST":
    form = PollForm(request.POST)
    if form.is_valid():
      poll = form.save(commit=False)
      poll.author = request.user
      poll.yes_votes = 0
      poll.no_votes = 0
      poll.created_date = timezone.now()
      poll.save()
      return redirect('poll_list')
  else:
    print("fsss")
    form = PollForm()
    
  return render(request, 'vote/templates/poll_new.html', {'form':form})