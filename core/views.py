from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import DetailView


from .models import Service, Team, Product, Blog, Contact, Plan


# Create your views here.
def home(request):
    service = Service.objects.all()
    team = Team.objects.all()
    blog = Blog.objects.all()
    product = Product.objects.all()
    plan = Plan.objects.all()
    context = {
        'service': service,
        'team': team,
        'blog': blog,
        'product': product,
        'plan': plan,
    }
    return render(request, 'core/index.html', context)


def about(request):
    team = Team.objects.all()
    context = {
        'team': team
    }
    return render(request, 'core/about.html', context)


class TeamDetail(DetailView):

    model = Team
    template_name = 'core/team_detail.html'
    redirect_field_name = 'login'


@login_required(login_url='login')
def blog(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog
    }
    return render(request, 'core/blog.html', context)


# def blog_detail(request, id):
#     blog_det = Blog.objects.get(id=id)
#     context = {
#         'b': blog_det
#     }
#     return render(request, 'core/blog_detail.html', context)
#

class BlogDetail(LoginRequiredMixin, DetailView):

    model = Blog
    template_name = 'core/blog_detail.html'
    redirect_field_name = 'login'


@login_required(login_url='login')
def contact(request):

    if request.method == "POST":
        form = Contact()
        first_name = request.POST['first_name']
        second_name = request.POST['second_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            email,
            ['jerriesvector12@gmail.com']

        )
        if form.is_valid():
            form.save()
        return render(request, 'core/contact.html')
    else:
         return render(request, 'core/contact.html',)


@login_required(login_url='login')
def counter(request):

    return render(request, 'core/counter.html')