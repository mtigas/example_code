from django.views.generic.simple import direct_to_template
from django.views.decorators.cache import never_cache

from forms import FeetInchesModelForm
from models import DemoModel

@never_cache
def formtest(request):

    test_objects = DemoModel.objects.all()

    form_kwargs = {}
    edit_obj = None
    if request.GET.has_key('id'):
        try:
            edit_obj = test_objects.get(pk=request.GET['id'])
            form_kwargs['instance'] = edit_obj
        except:
            pass

    if request.method == "POST":
        f = FeetInchesModelForm(data=request.POST,**form_kwargs)
        if f.is_valid():
            f.save()
    else:
        f = FeetInchesModelForm(**form_kwargs)

    return direct_to_template(
        request = request,
        template = 'formtest.html',
        extra_context = {
            'form': f,
            'test_objects':test_objects,
            'edit_obj':edit_obj
        }
    )
