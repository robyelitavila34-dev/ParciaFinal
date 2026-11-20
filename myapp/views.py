
from django.shortcuts import render, redirect
from .forms import ProgramaForm

def crear_programa(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('crear_programa')
    else:
        form = ProgramaForm()

    return render(
        request,
        'crear_programa.html',
        {'form': form}
    )
