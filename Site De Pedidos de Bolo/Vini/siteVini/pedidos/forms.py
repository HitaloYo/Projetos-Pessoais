from django import forms
from pedidos.models import Note

class NoteForm(forms.ModelForm):

	class Meta:
		model = Note

		fields = [
			"name",
			"description",
			"size",
			"contato",
			"massa",
			"recheio",
			
			
		]

		def __init__(self, *args, **kwargs):
			super(NoteForm, self).__init__(*args, **kwargs)
			self.fields['name'].widget.attrs.update({'class': 'form-control'})
			self.fields['topo'].widget.attrs.update({'class': 'form-control'})
			self.fields['description'].widget.attrs.update({'class': 'form-control'})
