from PIL import Image
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(editable=False)


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category,self).save(*args,**kwargs)


    #Post saydırma
    def post_count(self):
        return self.posts.all().count() #posts -> related_name="posts" dan geliyor..




class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    publishing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True, upload_to='resimler/',default="resimler/sean-o-KMn4VEeEPR8-unsplash.jpg")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)#ForeignKey -> 1'e çok yani, 1 kullanıcı bir sürü yazı ekleyebilir ilişkisi
    slug = models.SlugField(default="slug", editable=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1, related_name="posts")#1 Category'nin ->BİR SÜRÜ POSTU OLABİLİR , category -> one, Post Many





    def __str__(self):
        return self.title


    #Benim title'ımı slugum yap onun için save metodu (Yani kaydetmeden önce slugu, img bu şekilde ayarla)
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Post,self).save(*args,**kwargs)

        #gelen resimleri boyutlandırma Pillow
        img = Image.open(self.image.path)


        if img.height > 340 or img.width > 770:
            new_size = (340,770)
            img.thumbnail(new_size)
            img.save(self.image.path)








"""
   1 user -> Bir sürü yazısı olabilir, fakat 1 yazının(Aynı yazı) bir sürü useri olamaz :ForeignKey
    1 etiket bir çok posta ait olabilir, aynı zamanda o yazıda bir çok etikete sahip olabilir:ManyToMany
"""


"""
ForeignKey -> on_delete = models.CASCADE yapmalısın yani,bu kullanıcıyı sildin,bütün yazıları sil.
default=1 -> id numarası 1 olan kullanıcı anlamına gelir. Var olan postlarınıza bir kullanıcı ataması yapar.


"""