from django.shortcuts import render, redirect
from django.utils import timezone
from .models import G
from .forms import GForm
# Create your views here.
def post_list(request):
    list = G.objects.filter(datetime__lte=timezone.now()).order_by('datetime')
    return render(request, 'gl0/post_list.html', {'list': list})

def g_new(request):
        if request.method == "POST":
            form = GForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('/', {'list': list})
        else:
            form = GForm()
        return render(request, 'gl0/g_edit.html', {'form': form})
