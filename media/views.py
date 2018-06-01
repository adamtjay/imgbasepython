from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse

from media.models import Media
from media.permissions import UserIsOwnerMedia
from media.serializers import MediaSerializer



def SearchImgsView(request):
    html = "<html><body> Hello </body></html>"
    return HttpResponse(html)

class MediaCreateAPIView(ListCreateAPIView):
    serializer_class = MediaSerializer

    def get_queryset(self):
        return Media.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MediaDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
    ## * require Auth
    # permission_classes = (IsAuthenticated, UserIsOwnerMedia)
