from django.utils import timezone
from django.contrib import admin

from .models import Category, Product, Review

# Register your models here.


class ReviewInline(admin.TabularInline):  
    '''Tabular Inline View for '''
    model = Review
    extra = 3
    classes = ('collapse',)
    # min_num = 3
    # max_num = 20

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date", 'added_days_ago', 'how_many_reviews',)
    list_editable = ('is_in_stock',)
    list_display_links = ('name', 'create_date')
    search_fields = ('name', 'create_date')
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
    date_hierarchy = 'update_date'
    inlines = (ReviewInline,)

    # fields=(('name', 'slug'),'description', "is_in_stock" )
    fieldsets = (
        ('Fields', {
            "fields": (
                ('name', 'slug'), "is_in_stock" # to display multiple fields on the same line, wrap those fields in their own tuple
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("description",'additional_info', 'categories'),
            'description' : "You can use this section for optionals settings"
        })

    )
    filter_horizontal = ("categories", )
    
    actions = ('is_in_stock',)

    def is_in_stock(self, request, queryset ):
        count = queryset.update(is_in_stock=True)
        self.message_user(request,f'{count} types of items added to the stock.')
    
    is_in_stock.short_description='Add checked items to the stock.'

    def added_days_ago(self, product):
        diff = timezone.now() - product.create_date
        return diff.days

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    raw_id_fields = ('product',) 

    actions = ('is_released',)

    def is_released(self, request, queryset):
        count = queryset.update(is_released=True)
        self.message_user(request,f'{count} reviews were released.')
    
    is_released.short_description='Release selected reviews.'




admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Category)


admin.site.site_title = ' My Admin'
admin.site.site_header = 'Best Admin Portal Ever'
admin.site.index_title = "Welcome to my Admin Portal"
