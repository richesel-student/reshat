# import stripe
#
# from django.conf import settings
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404, render
# from django.views import View
# from django.views.generic import DetailView
# import logging
# logger = logging.getLogger(__name__)
#
# from .models import Item
#
# stripe.api_key = settings.STRIPE_SECRET_KEY
#
#
#
# class ItemDetailView(DetailView):
#     model = Item
#     template_name = 'item_detail.html'
#     context_object_name = 'item'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         item = self.get_object()
#         try:
#             intent = stripe.PaymentIntent.create(
#                 amount=item.get_price_cents(),
#                 currency=item.currency,
#                 automatic_payment_methods={'enabled': True}
#             )
#             logger.info(f"PaymentIntent created: {intent.id}, client_secret: {intent.client_secret}")
#             context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
#             context['client_secret'] = intent.client_secret
#         except Exception as e:
#             logger.error(f"Error creating PaymentIntent: {e}") # Логируем ошибку
#             context['error_message'] = "Произошла ошибка при создании платежа." # Передаем сообщение об ошибке в шаблон
#         return context
#
# class BuyItemView(View):
#     # Этот view больше не нужен, его можно удалить
#     pass

from django.views.generic.detail import DetailView
from django.conf import settings
from .models import Item
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
import logging

# logger = logging.getLogger(__name__)
#
# from .models import Item
#
# stripe.api_key = settings.STRIPE_SECRET_KEY
#
# class BuyItemView(View):
#     def post(self, request, id):
#         item = get_object_or_404(Item, id=id)
#         try:
#             intent = stripe.PaymentIntent.create(
#                 amount=item.get_price_cents(),
#                 currency=item.currency,
#                 automatic_payment_methods={'enabled': True}
#             )
#             logger.info(f"PaymentIntent created: {intent.id}, client_secret: {intent.client_secret}")
#             return JsonResponse({'client_secret': intent.client_secret})
#         except Exception as e:
#             logger.error(f"Error creating PaymentIntent: {e}")
#             return JsonResponse({'error': 'Ошибка при создании платежа.'}, status=400)

logger = logging.getLogger(__name__)
stripe.api_key = settings.STRIPE_SECRET_KEY

class BuyItemView(View):
    def post(self, request, id):
        item = get_object_or_404(Item, id=id)
        try:
            intent = stripe.PaymentIntent.create(
                amount=item.get_price_cents(),
                currency=item.currency,
                automatic_payment_methods={'enabled': True}
            )
            logger.info(f"PaymentIntent created: {intent.id}, client_secret: {intent.client_secret}")
            return JsonResponse({'client_secret': intent.client_secret})
        except Exception as e:
            logger.error(f"Error creating PaymentIntent: {e}")
            return JsonResponse({'error': 'Ошибка при создании платежа.'}, status=400)


class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
        return context
