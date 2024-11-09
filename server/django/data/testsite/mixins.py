from django.views.generic.base import ContextMixin

class DataMixin(ContextMixin):
    title = None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.title is not None:
            context.update({'title': self.title})
        return context
    
    
class FormMixin(DataMixin):
    button_text = None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.button_text is not None:
            context.update({'button_text': self.button_text})
        return context