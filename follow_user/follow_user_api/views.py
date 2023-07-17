from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView , DestroyAPIView , UpdateAPIView , RetrieveAPIView
from user_app. models import User
from .serializer import AllUserSerializer , NotificationSerializer , RequestDeleteSerializer ,ProfileUpdateSerializer,ProfileSerializer
from follow_user.models import SendRequest 
from django.db.models import Q


# Create your views here.

class CheckAPI(APIView):
    def get(self,request):
        return Response("check......")
        

class AllUserView(ListAPIView):
    # http://localhost:8000/api/user/
    queryset = User.objects.all()
    serializer_class = AllUserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(
            ~Q(is_staff=True) , ~Q(email=self.request.user))
        
        followed_users = SendRequest.objects.filter(
            user=self.request.user).values_list('sender__email', flat=True).last()

        if followed_users:
            queryset = queryset.exclude(email = followed_users )
            return queryset
        return queryset


class NotificationView(ListAPIView):
    # localhost:8000/api/notification/
    queryset = SendRequest.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        queryset = SendRequest.objects.filter(user=self.request.user)
        return queryset


class UpdateStatusView(APIView):
    # http://localhost:8000/api/update_status/?user=6
    def get(self,request):
        user_id = self.request.GET.get("user")
        user = User.objects.get(id=user_id)
        users = SendRequest.objects.create(user=user, receive=self.request.user)
        users = SendRequest.objects.create(user=self.request.user, sender=user)
        return Response("Successfully update status")


class StartFollowing(APIView):
    # localhost:8000/api/start_following/?receive=99   
    def get(self,request):
        receive = request.GET.get("receive")

        # Update the status of the opposite user to "Following"
        receive_email= SendRequest.objects.filter(id= receive).values_list('receive__email',flat=True)
        update_opposite_user = SendRequest.objects.filter(user__email__in = receive_email , status = "Requested" , sender = request.user).update(
            status=SendRequest.STATUS_TYPE_CHOICES[1][0])
    
        # Update the status of the current user to "Accept"
        update_current_user = SendRequest.objects.filter(id=receive).update(status=SendRequest.STATUS_TYPE_CHOICES[5][0])
        return Response("Start Following")


class Requestdelete(DestroyAPIView):
    # localhost:8000/api/requestdelete/103/   
    queryset = SendRequest
    serializer_class = RequestDeleteSerializer

    def get_object(self):
        user_id = self.kwargs['pk']
        del_request_id = SendRequest.objects.filter(id=user_id).values_list('receive')
        sender_del = SendRequest.objects.filter(user__in=del_request_id, status="Requested", sender__email=self.request.user.email)
        sender_del.delete()
        return super().get_object()


class ProfileUpdateView(UpdateAPIView):
    #PATCH - localhost:8000/api/profile_update/7/
    queryset = User
    serializer_class = ProfileUpdateSerializer


class ProfileView(RetrieveAPIView):
    # GET - localhost:8000/api/profile/9
    queryset = User.objects.all()
    serializer_class = ProfileSerializer







