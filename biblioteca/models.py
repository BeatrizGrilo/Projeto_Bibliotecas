from django.db import models

# Create your models here.
class Biblioteca(models.Model):
    nomeb = models.CharField(max_length=50)
    localidade = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nomeb} - {self.localidade}'

class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    nomebiblioteca = models.ManyToManyField(Biblioteca)

    def __str__(self):
        return f'{self.titulo} ({self.genero})'

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    morada = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self):
        return f'{self.nome}'

class Requesicao(models.Model):
    titulolivro = models.ForeignKey(Livro,on_delete=models.CASCADE)
    data = models.DateField()
    nomecliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nomecliente} - {self.titulolivro} ({self.data})'
