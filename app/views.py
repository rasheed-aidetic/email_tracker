from django.shortcuts import render
from .models import SendMail, TrackMail
from django.http.response import HttpResponse
from django.templatetags.static import static
import os
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from django.conf import settings
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class CreateEmailData(APIView):

    def post(self, request):
        print(request.data)
        sender = request.data['sender']
        reciever = request.data['receiver']
        created_data = SendMail.objects.create(sender=sender, reciever=reciever)
        return Response({"message" : "Mail data created successfully", "data" : created_data.pk}, status=status.HTTP_201_CREATED)



class TrackOpenedMail(APIView):
    
    def get(self, request, uuid, image_filename = 'test.png'):
        image_path = os.path.join(settings.STATIC_ROOT, 'images', image_filename)
        print(uuid)
        # try:
        email = SendMail.objects.get(pk=uuid)
        current_time = datetime.now()
        send_Time = email.sent_at

        time_diff = current_time - send_Time.replace(tzinfo=None)
        print(time_diff, 80 * 'kdfj ')
        
        TrackMail.objects.create(mail = email, opened_time_diff = str(time_diff))
        if os.path.exists(image_path):
                print('it exists')
                with open(image_path, 'rb') as image_file:
                    image_data = image_file.read()

                    content_type = 'image/jpeg'  

                    response = HttpResponse(image_data, content_type=content_type)
                    return response
        else:
            # Return a 404 Not Found response if the image doesn't exist
            return HttpResponse(status=404)
        
        # except:
        #     return Response('mail does not exist')


class SendEmail(APIView):
     
     def post(self, request):
        email = request.data['email']
        mail_subject = 'test'
        message = request.data['message']
        message = render_to_string('send_email.html', {
            'message' : message
        })
        to_mail = email
        send_mail = EmailMessage(mail_subject, message, to=[to_mail])
        send_mail.content_subtype = "html"
        send_mail.send()
        
        return Response({"message" : "Message sent successfully"})
