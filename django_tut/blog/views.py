from django.shortcuts import render

posts = [
    {
        'author': 'Ishaan',
        'title': 'First test blog',
        'content': 'First test content',
        'date_posted': 'Sep 10 2020'
    },
   
    {
          'author': 'Ram',
          'title': 'Second test blog',
          'content': 'Second test content',
          'date_posted': 'Sep 12 2020'
    },
]

def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
