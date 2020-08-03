from django.shortcuts import render, get_object_or_404
import markdown, re
from rest_framework.generics import ListAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import PostListSerializer
from .models import Post, Category
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.permissions import AllowAny


# Create your views here.
def index(request):
    post_list = Post.objects.all()  # .order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def about(request):
    return render(request, 'blog/about.html')


def kind(request, k):
    category_id = Category.objects.filter(name=k)[0]
    post_list = Post.objects.filter(category=category_id)
    return render(request, 'blog/serch.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        # 记得在顶部引入 TocExtension 和 slugify
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post': post})


class IndexPostListView(ListAPIView):  # 集成了基类和混入类  （ListModelMixin,GenericAPIView）
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    pagination_class = LimitOffsetPagination
    permission_classes = [AllowAny]


class PostViewSet(ListModelMixin, GenericViewSet):  # generic 负责属性和方法  网络请求接数据的   minxin负责增删改查   视图集负责路由
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]


