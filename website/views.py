from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from website.models import Contact, Benchmark, TPfinsTool


def search_benchmark(request):
    if request.method == "POST":
        data = request.POST
        search = data["search"]
        benchmark = Benchmark.objects.filter(country__contains=search)
        contexto = {
            "benchmarks": benchmark,
        }
        http_response = render(
            request=request,
            template_name='benchmark_list.html',
            context=contexto,
        )
        return http_response

def success_messages(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='success_messages.html',
        context=contexto,
    )
    return http_response

class ContactCreateView(CreateView):
    model = Contact
    fields = ('name', 'email', 'message')
    success_url = reverse_lazy('success_messages')

class BenchmarkCreateView(CreateView):
    model = Benchmark
    fields = ('type_analysis', 'country', 'industry', 'credit_rating_borrower')
    success_url = reverse_lazy('inicio')

class TPfinsToolCreateView(CreateView):
    model = TPfinsTool
    fields = ('currency', 'principal', 'type_of_interest_rate', 'base_rate')
    success_url = reverse_lazy('inicio')
