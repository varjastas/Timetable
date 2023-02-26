from .forms import *
def get_form_context(request):
    context = {}
    if request.method == 'POST':
        form = Formforgo(request.POST)
    else:
        form = Formforgo(data=request.POST)
    context['form'] = form
    return context