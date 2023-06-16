from django.http import HttpResponseRedirect

from .models import Cc, History, AuthUser



# controller

def save_answers_history(request):
    if request.methode == 'POST':
        q_id = request.POST.get('q_id')
        a_id = request.POST.get('a_id')



def glosowanie(request, wybor_id):
    wybor = Countries.objects.get(pk=wybor_id)
    wybor.votes += 1
    wybor.save()
    return HttpResponseRedirect("../oddano_glos")