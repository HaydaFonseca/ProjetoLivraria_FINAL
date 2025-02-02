from django.db import models
from .livro import Livro
from .user import User

class Favorito(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favoritos"
    )
    livro = models.ForeignKey(
        Livro, on_delete=models.CASCADE, related_name="favoritos"
    )

    