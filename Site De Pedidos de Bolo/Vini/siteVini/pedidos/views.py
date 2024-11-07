from django.views.generic import ListView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from .models import Note
from .forms import NoteForm



def index(request):
    notes = Note.objects.filter(done=False)
    template = "index.html" 
    context = {
        "notes": notes,
        "active_page": "index"
    }
    return render(request, template, context)


def create(request):
    form = NoteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("index"))

    template = "new.html"
    context = {
        "form": form,
        "action": "Criar",
        "active_page": "create"
    }

    return render(request, template, context)


def update(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    form = NoteForm(request.POST or None, instance=note)
    template = "new.html"

    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("index"))

    context = {
        "form": form,
        "action": "Editar"
    }

    return render(request, template, context)


def delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()

    # Verifica de onde a requisição foi feita
    if request.GET.get('from') == 'finalizados':
        return HttpResponseRedirect(reverse('finalizados'))
    else:
        return HttpResponseRedirect(reverse('index'))



def finalizar(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.done = True  #'done' é o campo que indica se a nota está finalizada
    note.save()
    return redirect('index',)

class FinalizadosView(ListView):
    model = Note
    template_name = "finalizados.html"
    context_object_name = "finalizados"

    def get_queryset(self):
        return Note.objects.filter(done=True)  # Retorna apenas as notas finalizadas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'finalizados'  # Adiciona a página ativa ao contexto
        return context

