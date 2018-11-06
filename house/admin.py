import json
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from import_export.fields import Field
from .models import  LianjiaChengjiao, LianjiaErshoufang, LianjiaXiaoqu, LianjiaZufang


class EstateResource(resources.ModelResource):
    # 基本信息
    title = Field(attribute='title', column_name='标题')
    origin_url = Field(attribute='origin_url', column_name='网页源地址')
    price_total = Field(attribute='price_total', column_name='总价(万)')
    unit_price = Field(attribute='unit_price', column_name='单价(万)')
    community_name = Field(attribute='community_name', column_name='楼盘')
    area_name = Field(attribute='area_name', column_name='板块')
    input_time = Field(attribute='input_time', column_name='录入时间')
    cost_house = Field(column_name='房子交钱')

    @staticmethod
    def dehydrate_full_title(estate):
        return '%s by %s' % (estate.title, estate.city)

    @staticmethod
    def dehydrate_cost_house(estate):
        try:
            cost_payment = json.loads(estate.cost_payment)

            return cost_payment['cost_house']
        except:
            return 'bni'

    class Meta:
        model = LianjiaErshoufang

        # 定义导出excel有那些列
        fields = ('title', 'origin_url', 'price_total', 'unit_price', 'community_name', 'area_name', 'cost_house',
                  'input_time')

        # 定义导出excel类的顺序
        export_order = ('title', 'origin_url', 'price_total', 'unit_price', 'community_name', 'area_name',
                        'cost_house',
                        'input_time')


class EstateAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('area_name', 'community_name', 'title')
    list_filter = ('city', 'area_name')
    resource_class = EstateResource

class XiaoquResource(resources.ModelResource):
    # 基本信息
    title = Field(attribute='origin_title', column_name='标题')
    origin_url = Field(attribute='origin_url', column_name='网页源地址')
    price_total = Field(attribute='price_total', column_name='总价(万)')
    unit_price = Field(attribute='average_price', column_name='均价(元)')
    community_name = Field(attribute='service_fees', column_name='物业费')
    area_name = Field(attribute='service_company', column_name='物业公司')
    input_at = Field(attribute='input_at', column_name='录入时间')

    @staticmethod
    def dehydrate_full_title(estate):
        return '%s by %s' % (estate.title, estate.city)

    # @staticmethod
    # def dehydrate_cost_house(estate):
    #     try:
    #         cost_payment = json.loads(estate.cost_payment)

    #         return cost_payment['cost_house']
    #     except:
    #         return 'bni'

    class Meta:
        model = LianjiaErshoufang

        # 定义导出excel有那些列
        fields = ('title', 'origin_url', 'price_total', 'unit_price', 'community_name', 'area_name',
                  'input_at')

        # 定义导出excel类的顺序
        export_order = ('title', 'origin_url', 'price_total', 'unit_price', 'community_name', 'area_name',
                        'input_at')

class XiaoquAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):

    list_display = ('name', 'address', 'origin_title')
    list_filter = ('city', 'building_year')
    resource_class = XiaoquResource

admin.site.register(LianjiaErshoufang, EstateAdmin)
admin.site.register(LianjiaXiaoqu, XiaoquAdmin)
admin.site.register(LianjiaChengjiao)
