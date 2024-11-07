from django.db import models

tamanhoChoice = [
    ('n/a','N/A'),
    ('pequeno', 'Pequeno'),
    ('medio', 'Medio'),
    ('grande', 'Grande'),
]

massaChoice = [
    ('n/a','N/A'),
    ('chocolate', 'Chocolate'),
    ('fubá', 'Fubá'),
    ('cenoura', 'Cenoura'),
]

recheioChoice = [
    ('n/a','N/A'),
    ('chocolate', 'Chocolate'),
    ('morango', 'Morango'),
    ('caramelo', 'Caramelo'),
]

class Note(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=64)
    contato = models.CharField(max_length=64)
    description = models.TextField(max_length=256)
    done = models.BooleanField(default=False)
    size = models.CharField(max_length=20, choices=tamanhoChoice, default='N/A')
    massa = models.CharField(max_length=20, choices=massaChoice, default='N/A')
    recheio = models.CharField(max_length=20, choices=recheioChoice, default='N/A')
    

    def __str__(self):
        return self.description
