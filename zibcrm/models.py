from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    national_id = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=200)
    tel = models.CharField(max_length=20, unique=True)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #date = models.DateTimeField('adding date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial_national_id = self.national_id

    def natural_key(self):
        return (self.national_id)
        
    def __str__(self):
        return self.full_name
    
class Store(models.Model):
    name = models.CharField(max_length=50)
    manager = models.CharField(max_length=20)
    store_manager = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    #added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #date = models.DateTimeField('adding date')

    def natural_key(self):
        return (self.name)
        
    def __str__(self):
        return self.name

class GoodsManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)
        
class Goods(models.Model):
    #objects = GoodsManager()
    #name = models.CharField(max_length=20)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    #date = models.DateTimeField('adding date')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    GARDANBAND = 1
    GARDANBAND_RANGI = 2
    GARDANBAND_TENIS = 3
    GARDANBAND_FLOWER = 4
    DASTBAND = 5
    DASTBAND_RANGI = 6
    DASTBAND_TENIS = 7
    DATBAND_FLOWER = 8
    GOOSHVARE = 9
    GOOSHVARE_RANGI = 10
    GOOSHVARE_TAKNEGIN = 11
    HALGHE = 12
    HALGHE_YEKRAJ = 13
    SOLITER = 14
    HALGHE_VA_POSHT_HALGHE = 15
    HALGHE_MARDANE_PLATIN = 16
    ANGOSHTARE_RANGI = 17
    HALGHE_FLOWER = 18
    AVIZ = 19
    AVIZ_TAKNEGIN = 20
    AVIZ_RANGI = 21
    HALGHE_MARDANE_TALA = 22
    NIM_SET = 23
    ALANGOO = 24
    DOKME_SARDAST = 25
    SANJAGH_KEREBAT = 26
    GOOSHVARE_FLOWER = 27
    HALGHE_MARDANE_NOGHRE = 28
    ZANJIR_PLATIN = 29
    PRODUCT_TYPE_CHOICES = ((GARDANBAND, "گردنبند"),
                                                  (GARDANBAND_RANGI, "گردنبند رنگی"),
                                                  (GARDANBAND_TENIS, "گردنبند تنیس"),
                                                  (GARDANBAND_FLOWER, "گردنبند فاور"),
                                                  (DASTBAND, "دستببند"), 
                                                  (DASTBAND_RANGI, "دستببند رنگی"),
                                                  (DASTBAND_TENIS, "دستببند تنیس"), 
                                                  (DATBAND_FLOWER, "دستببند فلاور"),
                                                  (GOOSHVARE, "گوشواره"),
                                                  (GOOSHVARE_RANGI, "گوشواره رنگی"),
                                                  (GOOSHVARE_TAKNEGIN, "گوشواره تک نگین"),
                                                  (HALGHE, "حلقه"),
                                                  (HALGHE_YEKRAJ, "حلقه یک رج"),
                                                  (SOLITER, "سولیتر"),
                                                  (HALGHE_VA_POSHT_HALGHE, "حلقه و پشت حلقه"),
                                                  (HALGHE_MARDANE_PLATIN, "حلقه مردانه پلاتین"),
                                                  (ANGOSHTARE_RANGI, "انگشتر رنگی"),
                                                  (HALGHE_FLOWER, "حلقه پلاتین"),
                                                  (AVIZ, "آویز"),
                                                  (AVIZ_TAKNEGIN, "آویز تک نگین"),
                                                  (AVIZ_RANGI, "آویز رنگی"),
                                                  (HALGHE_MARDANE_TALA, "حلقه مردانه طلا"),
                                                  (NIM_SET, "نیم ست"),
                                                  (ALANGOO, "النگو"),
                                                  (DOKME_SARDAST, "دکمه سردست"),
                                                  (SANJAGH_KEREBAT, "سنجاق کربات"),
                                                  (GOOSHVARE_FLOWER, "گوشواره فلاور"),
                                                  (HALGHE_MARDANE_NOGHRE, "حلقه مردانه نقره"),
                                                  (ZANJIR_PLATIN, "زنجیر پلاتین"),
                                                )
    product_type = models.PositiveSmallIntegerField(choices=PRODUCT_TYPE_CHOICES )
    
    TALA = 1
    PLATIN = 2
    NOGHRE = 3
    FELEZ_TYPE_CHOICES = ((TALA, "طلا"),
                                            (PLATIN, "پلاتین"),
                                            (NOGHRE, "نقره"),
                                            )
    felez_type = models.PositiveSmallIntegerField(choices=FELEZ_TYPE_CHOICES)
    felez_weight = models.FloatField()
    felez_price = models.FloatField()
    
    BRILLIANUM = 1
    EMERALD = 2
    RUBY_RUBY = 3
    SAPPHIRE = 4
    RUBY_QUILTED = 5
    AMETHYST = 6
    THYROID = 7
    PEARL = 8
    COLORED_STONE = 9
    SEEDS = 10
    GIA_OR_HRD_SEEDS = 11
    FIROOZEH = 12
    TOPAZ = 13
    TANZANITE = 14
    OPAL = 15
    TOURMALINE = 16
    STONE_TYPE_CHOICES = ((BRILLIANUM, "Brillianum"),
                                             (EMERALD, "Emerald"),
                                             (RUBY_RUBY, "Ruby Ruby"),
                                             (SAPPHIRE, "Sapphire"),
                                             (RUBY_QUILTED, "Ruby Quilted"),
                                             (AMETHYST, "Amethyst"),
                                             (THYROID, "Thyroid"),
                                             (PEARL, "Pearl"),
                                             (COLORED_STONE, "Colored Stone"),
                                             (SEEDS, "Seeds"),
                                             (GIA_OR_HRD_SEEDS, "GIA or HRD Seeds"),
                                             (FIROOZEH, "Firoozeh"),
                                             (TOPAZ, "Topaz"),
                                             (TANZANITE, "Tanzanite"),
                                             (OPAL, "Opal"),
                                             (TOURMALINE, "Tourmaline"),
                                            )
    stone_type = models.PositiveSmallIntegerField(choices=STONE_TYPE_CHOICES)
    stone_weight = models.FloatField()
    
    ROUND = 1
    MARQUIS = 2
    TEARS = 3
    BUGAT = 4
    PRINCESSES = 5
    OVAL = 6
    TRELLENS = 7
    MIX = 8
    EMERALD = 9
    TERRY_ENGEL = 10
    CUT_TYPE_CHOICES = ((ROUND, "Round"),
                                         (MARQUIS, "Marquis"),
                                         (TEARS, "Tears"),
                                         (BUGAT, "Bugat"),
                                         (PRINCESSES, "Princesses"),
                                         (OVAL, "Oval "),
                                         (TRELLENS, "Trellens"),
                                         (MIX, "MIX"),
                                         (EMERALD, "Emerald"),
                                         (TERRY_ENGEL, "Terry Engel"),
                                        )
    cut_type = models.PositiveSmallIntegerField(choices=CUT_TYPE_CHOICES)
    
    COLOR_G = 1
    COLOR_D = 2
    COLOR_E = 3
    COLOR_F = 4
    COLOR_H = 5
    COLOR_I = 6
    COLOR_K = 7
    COLOR_L = 8
    COLOR_J = 9
    COLOR_M = 10
    STONE_COLOR_TYPE_CHOICES = ((COLOR_G, "G"),
                                                         (COLOR_D, "D"),
                                                         (COLOR_E, "E"),
                                                         (COLOR_F, "F"),
                                                         (COLOR_H, "H"),
                                                         (COLOR_I, "I"),
                                                         (COLOR_K, "K"),
                                                         (COLOR_L, "L"),
                                                         (COLOR_J, "J"),
                                                         (COLOR_M, "M"),
                                                        )
    stone_color_type = models.PositiveSmallIntegerField(choices=STONE_COLOR_TYPE_CHOICES)
    
    SL3 = 1
    SL2 = 2
    SL1 = 3
    VS2 = 4
    VS1 = 5
    VVS2 = 6
    VVS1 = 7
    IF = 8
    CLEAN_TYPE_CHOICES = ((SL3, "SL3"),
                                             (SL2, "SL2"),
                                             (SL1, "SL1"),
                                             (VS2, "VS2"),
                                             (VS1, "VS1"),
                                             (VVS2, "VVS2"),
                                             (VVS1, "VVS1"),
                                             (IF, "IF"),
                                            )
    clean_type = models.PositiveSmallIntegerField(choices=CLEAN_TYPE_CHOICES)
    
    GAI = 1
    HRD = 2
    ID_TYPE_CHOICES = ((GAI, "GAI"),
                                       (HRD, "HRD"),
                                     )
    id_type = models.PositiveSmallIntegerField(choices=ID_TYPE_CHOICES)

    price = models.FloatField()
    store = models.ManyToManyField(Store)
    #filedata = models.FileField(null=True, blank=True)
    
    def natural_key(self):
        return (self.name)
    
    def __str__(self):
        return self.get_product_type_display()\
        +" | metal_type:"+self.get_felez_type_display()\
        +" | metal_price:"+str(self.felez_price)\
        +" | stone_type:"+self.get_stone_type_display()\
        +" | stone_weight:"+str(self.stone_weight)\
        +" | price:"+str(self.price)
    
class Purchase(models.Model):
    buyer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    product = models.ManyToManyField(Goods)
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING, null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #date = models.DateTimeField('adding date')
    
    def __str__(self):
        products_count = len(self.product.all())
        products_postfix = "product" if products_count==1 else "products"
        product_str = str(products_count) + products_postfix
        return str(self.buyer) + ":" + product_str + "_from:" + str(self.store)
        