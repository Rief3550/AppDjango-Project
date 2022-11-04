from django.db import models

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=28)
    construido_por = models.CharField(max_length=38)
    titulo_principal = models.CharField(max_length=38, default = '')
    subtitulo_principal = models.CharField(max_length=38, default = '')