from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_welcome_email(artist_name, artist_email):

    subject = "Successfully Registered"
    message = f"""
    Congratulations {artist_name},
           You have successfully Registered to this company.
           Now, you are ready for further process.
           Our company provide Many Services 
    """

    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [artist_email],
            fail_silently=False,
        )
    except Exception as e:
        print('something wrong')
