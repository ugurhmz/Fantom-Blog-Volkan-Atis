from PIL import Image
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify

#_______________________________ Cetagory() ___________________________________________________
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



#_______________________________ Tag() ___________________________________________________
class Tag(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(editable = False )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag,self).save(*args, **kwargs)


    def post_count(self):
        return self.posts.all().count() #posts -> related_name='posts' olan...



#_______________________________ Post() ___________________________________________________

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    publishing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True, upload_to='resimler/',default="resimler/sean-o-KMn4VEeEPR8-unsplash.jpg")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)#ForeignKey -> 1'e çok yani, 1 kullanıcı bir sürü yazı ekleyebilir ilişkisi
    slug = models.SlugField(default="slug", editable=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1, related_name="posts")#1 Category'nin ->BİR SÜRÜ POSTU OLABİLİR , category -> one, Post Many
    tag = models.ManyToManyField(Tag,related_name="posts", blank=True)
    slider_post = models.BooleanField(default=False)

    hit=models.PositiveIntegerField(default=0)




    def __str__(self):
        return self.title


    #Benim title'ımı slugum yap onun için save metodu (Yani kaydetmeden önce slugu, img bu şekilde ayarla)
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Post,self).save(*args,**kwargs)


    def post_tag(self):
        return ",".join(str(tag) for  tag in self.tag.all())


    def comment_count(self):
        return self.comments.all().count()





# _______________________________ Comment(models.Model) ___________________________________________________
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments') # 1 post, Çokça YORUM
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    publishing_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.post.title #Hangi Yazıya yorum yapılmış,admin panelinde göster.








        #gelen resimleri boyutlandırma Pillow (KALDIRILDI -RGB Den dolayı bozuyor..)
        # img = Image.open(self.image.path)
        #
        #
        # if img.height > 340 or img.width > 770:
        #     new_size = (340,770)
        #     img.thumbnail(new_size)
        #     img.save(self.image.path)








    """
   1 user -> Bir sürü yazısı olabilir, fakat 1 yazının(Aynı yazı) bir sürü useri olamaz :ForeignKey
    1 etiket bir çok posta ait olabilir, aynı zamanda o yazıda bir çok etikete sahip olabilir:ManyToMany
    """


"""
ForeignKey -> on_delete = models.CASCADE yapmalısın yani,bu kullanıcıyı sildin,bütün yazıları sil.
default=1 -> id numarası 1 olan kullanıcı anlamına gelir. Var olan postlarınıza bir kullanıcı ataması yapar.


"""