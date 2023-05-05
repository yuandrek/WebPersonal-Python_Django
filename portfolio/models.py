

from django.db import models

# Create your models here.
class proyecto (models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='Project')
    link = models.URLField(null=True, blank=True, verbose_name='Direccion Web')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering =  ['-created'] 

    def __str__(self):
        return self.title


class slider(models.Model):
    image = models.ImageField(verbose_name='Imagen', upload_to='slider')

    

    

 
