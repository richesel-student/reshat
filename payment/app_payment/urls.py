from django.urls import path
from .views import ItemDetailView, BuyItemView

urlpatterns = [
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('buy/<int:id>/', BuyItemView.as_view(), name='buy_item'),
]
