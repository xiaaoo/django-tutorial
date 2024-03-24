from django.shortcuts import render

posts = [
    {
        'author': 'xiaoyun',
        'title': 'vayager coffee',
        'content': 'coffee is good',
        'date_posted': 'Mar 23, 2024',
    },
        {
        'author': 'yuni',
        'title': 'Starbucks coffee',
        'content': 'coffee is okay',
        'date_posted': 'Mar 22, 2024',
    },
        {
        'author': 'sean',
        'title': 'cold brew office coffee',
        'content': 'coffee is great',
        'date_posted': 'Mar 21, 2024',
    }
]
# this is the logic for how we want to handle when the user goes to blog home page
def home(request):
    context = {
        'posts': posts,
        'title': 'I love Coffee'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})