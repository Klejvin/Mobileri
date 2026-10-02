from django.db import models
from django.utils.text import slugify

class Kategoria(models.Model):
    emri = models.CharField(max_length=100, verbose_name="Emri i Kategorisë")
    slug = models.SlugField(unique=True, blank=True, help_text="Gjenerohet automatikisht")

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoritë"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.emri)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.emri


class Produkti(models.Model):
    kategoria = models.ForeignKey(
        Kategoria, 
        on_delete=models.CASCADE, 
        related_name='produktet',
        verbose_name="Kategoria"
    )
    emri = models.CharField(max_length=200, verbose_name="Emri i Produktit")
    
    # Fusha për tekstin e shkurtër që shfaqet te karta (p.sh. "Dru lisi i punuar")
    shenim_shkurter = models.CharField(max_length=255, blank=True, verbose_name="Shënim i shkurtër")
    
    pershkrimi = models.TextField(blank=True, verbose_name="Përshkrimi i detajuar")
    
    # E ndryshuam në CharField që të shkruash edhe "Me marrëveshje"
    cmimi = models.CharField(max_length=50, verbose_name="Çmimi ose Statusi") 
    
    imazhi = models.ImageField(upload_to='produktet/', verbose_name="Foto Kryesore")
    
    data_krijimit = models.DateTimeField(auto_now_add=True)
    eshte_aktiv = models.BooleanField(default=True, verbose_name="I disponueshëm")

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produktet"
        ordering = ['-data_krijimit']

    def __str__(self):
        # E hoqëm simbolin € nga këtu pasi mund të jetë tekst
        return f"{self.emri} ({self.cmimi})"


class Fotot(models.Model):
    produkti = models.ForeignKey(Produkti, on_delete=models.CASCADE, related_name='galeria')
    imazhi = models.ImageField(upload_to='produktet/galeria/', verbose_name="Imazhi i Galerisë")

    class Meta:
        verbose_name = "Foto Galerie"
        verbose_name_plural = "Galeria e Fotove"