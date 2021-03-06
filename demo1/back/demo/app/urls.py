from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


# 使用router来注册 ViewSet，让urlconf自动生成
router = DefaultRouter()        # 可以处理视图的路由器
router.register(r'pic',views.PicViewSet)
router.register(r'cd_pic', views.CdPicViewSet)    # 注册变化检测图片
router.register(r'split_images', views.SplitImagesViewSet)

urlpatterns = [
    path(r'', include(router.urls)),  # 将路由器中的所有路由信息追加到django的路由列表中
]
