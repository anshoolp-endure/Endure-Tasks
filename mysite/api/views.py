from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializers
#from rest_framework.views import APIView


# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers

    def delete(self, req, *args, **kwargs):
        BlogPost.objects.all().delete
        return Response(status = status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    lookup_field = "pk"


# class BlogPostList(APIView):
#     def get(self, request, format=None):
#         title = get.query_params.get("title", "")

#         if title:
#             blog_posts = BlogPost.objects.filter(title_icontains=title)
#         else:
#             blog_posts = BlogPost.objects.all()
#         serializer = BlogPostSerializers(blog_posts, many=True)
#         return Response(serializer.data, status = status.HTTP_200_OK)