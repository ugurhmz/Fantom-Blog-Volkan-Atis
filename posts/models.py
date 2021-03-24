from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    publishing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True, upload_to='resimler/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)#ForeignKey -> 1'e çok yani, 1 kullanıcı bir sürü yazı ekleyebilir ilişkisi
    slug = models.SlugField(default="slug")



    def __str__(self):
        return self.title


    #Benim title'ımı slugum yap onun için save metodu
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Post,self).save(*args,**kwargs)










"""
   1 user -> Bir sürü yazısı olabilir, fakat 1 yazının(Aynı yazı) bir sürü useri olamaz :ForeignKey
    1 etiket bir çok posta ait olabilir, aynı zamanda o yazıda bir çok etikete sahip olabilir:ManyToMany
"""


"""
ForeignKey -> on_delete = models.CASCADE yapmalısın yani,bu kullanıcıyı sildin,bütün yazıları sil.
default=1 -> id numarası 1 olan kullanıcı anlamına gelir. Var olan postlarınıza bir kullanıcı ataması yapar.


"""