from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """Задача отправки e-mail уведомлений при успешном оформлении заказа."""
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    # from_email = 'myshop@admin.com'
    # to = 'den88ant@yandex.ru'
    message = f'Dear, {order.first_name}, \n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    # html_content = 'This is an HTML message.'
    # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    # msg.attach_alternative(html_content, "text/html")
    # msg.send(fail_silently=False)
    mail_sent = send_mail(subject,
                          message,
                          'denant1993@gmail.com',
                          [order.email],
                          fail_silently=False)
    return mail_sent
