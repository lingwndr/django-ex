from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from .models import Customer, Goods, Purchase, Store

class CustomerAdmin(admin.ModelAdmin):
    exclude = ('added_by',)
    list_display = ('national_id', 'full_name', 'tel',  'created_at', 'updated_at', 'added_by')

    def get_queryset(self, request):
        qs = super(CustomerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(added_by=request.user)
        
    def save_model(self, request, obj, form, change):
        if not change:
            obj.added_by = request.user
            u = User(username=obj.national_id)
            u.set_password(obj.tel)
            u.save()
        else:
            u = User.objects.get(username=obj.initial_national_id)
            u.username = obj.national_id
            #u.set_password(obj.tel) #no need to update password
                                                    #maybe it has been changed
                                                    #by user. so we should not
                                                    #overrided it.
            u.save()
        obj.save()
  
class GoodsAdmin(admin.ModelAdmin):
    #exclude = ('added_by', )      
    list_display = ('product_type', 'felez_type', 'felez_weight', 'stone_type', 'stone_weight', 'price', 'created_at', 'updated_at', 'added_by')

    '''
    fieldsets = [
                        ("محصول", {'fields':  ('product_type', 'felez_type', 'felez_weight', 'felez_price')}),
                        ("ویژگی های سنگ", {'fields': ['stone_type', 'stone_weight', 'cut_type', 'stone_color_type']}),
                        (None, {'fields': ['clean_type', 'id_type']}),
                        (None, {'fields': ['price']}),
                        (None, {'fields': ['store']}),
                     ]
    '''
    fields = (('product_type', 'felez_type', 'felez_weight', 'felez_price'),
                  'stone_type', 'stone_weight', 'cut_type', 'stone_color_type', 'clean_type', 'id_type',
                  'price', 
                  'store',
                 )

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ['added_by']
        if not request.user.is_superuser:
            self.exclude.append('store') #here!
        return super(GoodsAdmin, self).get_form(request, obj, **kwargs)
        
    def get_queryset(self, request):
        qs = super(GoodsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        store = Store.objects.get(store_manager=request.user)
        #return qs.filter(added_by=request.user)
        return qs.filter(store=store)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "store":
            if not request.user.is_superuser:
                kwargs["queryset"] = Store.objects.filter(store_manager=request.user)
        return super().formfield_for_manytomany(db_field, request, **kwargs)
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.added_by = request.user
        obj.save()
        if not request.user.is_superuser:
            stores = Store.objects.filter(store_manager=request.user)
            for store in stores:
                obj.store.add(store)

'''
class GoodsInLine(admin.TabularInline):
    model = Purchase.product.through
    fields = ['product_type', 'felez_type']
    readonly_fields = ['product_type', 'felez_type']
    def product_type(self, instance):
        return instance.goods.product_type_display()
    product_type.short_description = 'نوع محصول'
                
    def felez_type(self, instance):
        return instance.goods.get_felez_type_display()
    felez_type.short_description = 'felez type'
'''  

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'store',  'created_at', 'updated_at', 'added_by')
    '''
    inlines = [
        GoodsInLine,
    ]
    '''
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ['added_by']#, 'product']
        if not request.user.is_superuser:
            self.exclude.append('store') #here!
        return super(PurchaseAdmin, self).get_form(request, obj, **kwargs)
        
    def get_queryset(self, request):
        qs = super(PurchaseAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(added_by=request.user)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "product":
            if not request.user.is_superuser:
                store = Store.objects.get(store_manager=request.user)
                #kwargs["queryset"] = store.goods_set.all() #both are correct
                kwargs["queryset"] = Goods.objects.filter(store=store)
        return super().formfield_for_manytomany(db_field, request, **kwargs)
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "buyer":
            if not request.user.is_superuser:
                kwargs["queryset"] = Customer.objects.filter(added_by=request.user)
        elif db_field.name == "store":
            if not request.user.is_superuser:
                kwargs["queryset"] = Store.objects.filter(store_manager=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
        
    def save_model(self, request, obj, form, change):
        if not change:
            obj.added_by = request.user
        obj.save()
        if not request.user.is_superuser:
            store = Store.objects.get(store_manager=request.user)
            obj.store = store
            obj.save()
            #obj.store.add(store)
            #stores = Store.objects.filter(store_manager=request.user)
            #for store in stores:
                #obj.store.add(store)   
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'store_manager', 'address', 'created_at', 'updated_at')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "store_manager":
            kwargs["queryset"] = User.objects.filter(is_staff=True) #filters out customers
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Store, StoreAdmin)
