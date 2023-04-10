from django.db import models

# Create your models here.
class Produto(models.Model):
    id_produto = models.AutoField(primary_key= True)
    nome = models.models.TextField(max_Length=500)
    preco = models.DecimalField(decimal_places=2, max_digits=12)
    site = models.models.TextField(max_Length=255)
    data_cotacao = models.models.DateField()
    link_imagem = models.TextField(max_length=500, default='https://via.placeholder.com/150')
    
    
    
    