from django.shortcuts import render
from django.views.generic import TemplateView



class TopView(TemplateView):
  template_name = 'base/top.html'

  def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    ctx['title'] = 'a'
    return ctx

def top(request):
  ctx = {'title': 'django'}
  return render(request, 'base/top.html', ctx)
