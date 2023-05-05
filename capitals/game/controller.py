from django.http import HttpResponseRedirect

from game.models import Choice



# controller
def glosowanie(request, wybor_id):
    wybor = Choice.objects.get(pk=wybor_id)
    wybor.votes += 1
    wybor.save()
    return HttpResponseRedirect("../oddano_glos")