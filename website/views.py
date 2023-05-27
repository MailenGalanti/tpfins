from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


from website.models import Contact, Benchmark
from website.forms import BenchmarkForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

    
@method_decorator(login_required, name='dispatch')
class BenchmarkListView(ListView):
    model = Benchmark
    context_object_name = 'benchmarks'
    template_name = 'benchmark_list.html'
    
    def get_queryset(self):
        # Obtener los benchmarks del usuario actualmente logueado
        user = self.request.user
        queryset = super().get_queryset()
        queryset = queryset.filter(user=user)
        return queryset

class BenchmarkDeleteView(LoginRequiredMixin, DeleteView):
    model = Benchmark
    template_name = 'benchmark_confirm_delete.html'
    success_url = reverse_lazy('benchmark_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Benchmark deleted successfully.")
        return super().delete(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class BenchmarkDetailView(DetailView):
    model = Benchmark
    template_name = 'benchmark_detail.html'
    context_object_name = 'benchmark'

    def dispatch(self, request, *args, **kwargs):
        benchmark = self.get_object()
        if request.user == benchmark.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request, "You are not authorized to view this benchmark.")
            return HttpResponseRedirect(reverse('inicio'))

class BenchmarkUpdateView(UpdateView):
    model = Benchmark
    form_class = BenchmarkForm
    template_name = 'benchmark_form_edit.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        benchmark = self.get_object()
        if request.user == benchmark.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request, "You are not authorized to update this benchmark.")
            return HttpResponseRedirect(reverse('inicio'))

    def get_success_url(self):
        return reverse('benchmark_detail', kwargs={'pk': self.object.pk})
    
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

@method_decorator(login_required, name='dispatch')
class BenchmarkCreateView(CreateView):
    model = Benchmark
    form_class = BenchmarkForm
    success_url = reverse_lazy('benchmark_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)