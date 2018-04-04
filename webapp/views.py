from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Q
from . import models
from django.core.mail import send_mail
from itw2proj import settings

vidext = ['mp4', 'MP4', 'MKV', 'avi', 'mkv', 'flv', 'webm', 'wmv']
songext = ['mp3', 'aac3']
imgext = ['jpg', 'png','jpeg', 'gif']


def home(request):
    return render(request, 'webapp/home.html', context=None)


def pre_login(request):
    return render(request, 'webapp/prelogin.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            send_mail(
                'Registration complete',
                'Welcome to Mython,'+user_form.cleaned_data['first_name']+'   !   We’re glad you’re a part of our community.\n\n Find all you need, share with others, and connect with peers!\n\n\nThanks for joining!\nThe Mython team ',
                settings.EMAIL_HOST_USER,
                [user_form.cleaned_data['email'], 'mython.itw.gmail.com'],
                fail_silently=False,
            )
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'webapp/register.html', {'user_form': user_form,
                                                    'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/webapp/user_home')
            else:
                return HttpResponse("<h1>Your Home account is disabled</h1>")
        else:
            print("Invalid Login Detail: {0} {1}".format(username, password))
            return HttpResponse("Invalid Login detail provided")
    else:
        return render(request, 'webapp/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/webapp/')


def index(request):
    if request.user.is_authenticated():
        vidqr = models.Video.objects.all().order_by("-uploaded_at")[:6]
        msgqr = models.Message.objects.all().order_by("-pk")[:6]
        imgqr = models.Image.objects.all().order_by("-pk")[:6]
        fileqr = models.File.objects.all().order_by("-pk")[:6]
        context = {'vidqr': vidqr, 'msgqr': msgqr, 'imgqr':imgqr, 'fileqr':fileqr}
        return render(request, 'webapp/index.html', context)
    else:
        return render(request, 'webapp/home.html', context=None)


def addvid(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = VideosForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.extension = form.cleaned_data['video'].name.split(sep='.')[-1]
                form.instance.size = form.cleaned_data['video'].size/1024
                if form.instance.extension in vidext:
                    form.save()
                    return render(request, 'webapp/uploadsuccess.html', context=None)
                else:
                    if form.instance.extension in songext:
                        temp = 'songs'
                        ref = 'webapp:addsong'

                    if form.instance.extension in imgext:
                        temp = 'images'
                        ref = 'webapp:img_add'
                    elif form.instance.extension in vidext:
                        temp = 'videos'
                        ref = 'webapp:vid_add'
                    else:
                        temp = 'files'
                        ref = 'webapp:file_add'
                    return render(request, 'webapp/unsupportedextension.html', context={
                            'ext': form.instance.extension,
                            'temp': temp,
                            'ref':ref
                        })
        else:
            form = VideosForm()
        return render(request, 'webapp/Forms/FileForm.html', {
            'form': form
        })
    else:
        return render(request, 'webapp/home.html', context=None)


def vid_all(request):
    if request.user.is_authenticated():
        vidall = models.Video.objects.all().order_by("-uploaded_at")
        context = {'vidall': vidall}
        return render(request, 'webapp/vid_all.html', context)
    else:
        return render(request, 'webapp/home.html', context=None)


def vid(request, vid_id):
    if request.user.is_authenticated():
        video = get_object_or_404(models.Video, pk=vid_id)
        context = {'video': video}
        return render(request, 'webapp/vid.html', context)
    else:
        return render(request, 'webapp/home.html', context=None)


def messages_all(request):
    if request.user.is_authenticated():
        msg = models.Message.objects.all().order_by("-pk")
        context = {'all_messages': msg}
        return render(request, 'webapp/messages_all.html', context)
    else:
        return render(request, 'webapp/home.html', context=None)


def message(request, mid):
    if request.user.is_authenticated():
        msg = get_object_or_404(models.Message, pk=mid)
        context = {'msg': msg}
        return render(request, 'webapp/message.html', context)
    else:
        return render(request, 'webapp/home.html', context=None)


def add_message(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = MessagesForm(request.POST)
            if form.is_valid():
                form.instance.sender = request.user.username
                form.save()
                return render(request, 'webapp/uploadsuccess.html', context=None)
        else:
            form = MessagesForm()
        return render(request, 'webapp/Forms/MessageForm.html', {
            'form': form
        })
    else:
        return render(request, 'webapp/home.html', context=None)


def notification_all(request):
    if request.user.is_authenticated():
        ntfc = models.Notification.objects.filter(send_to=request.user).order_by("-pk")
        sent = models.Notification.objects.filter(sender__exact=request.user.username).order_by("-pk")
        context = {'all_notification': ntfc, 'sent': sent}
        return render(request, 'webapp/notifications_all.html', context)
    else:
        return render(request, 'webapp/home.html', context=None)


def notification(request, nid):
    if request.user.is_authenticated():
        ntfc = get_object_or_404(models.Notification, pk=nid)
        context = {'ntfc': ntfc}
        return render(request, 'webapp/notification.html', context)
    else:
        return render(request, 'webapp/home.html', context=None)


def add_notification(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = NotificationForm(request.POST)
            if form.is_valid():
                form.instance.sender = request.user.username
                form.save()
                return render(request, 'webapp/uploadsuccess.html', context=None)
        else:
            form = NotificationForm()
        return render(request, 'webapp/Forms/MessageForm.html', {
            'form': form
        })
    else:
        return render(request, 'webapp/home.html', context=None)


def uploadmenu(request):
    if request.user.is_authenticated():
        return render(request, 'webapp/uploadmenu.html')
    else:
        return render(request, 'webapp/home.html', context=None)


def contact(request):
    if request.user.is_authenticated():
        return render(request, 'webapp/contact.html')
    else:
        return render(request, 'webapp/home.html', context=None)


def delete_vid(request, vid_id):
    if request.user.is_authenticated():
        video_reqd = models.Video.objects.get(pk=vid_id)
        video_reqd.delete()
        vidall = models.Video.objects.all()
        context = {'vidall': vidall}
        return render(request, 'webapp/vid_all.html', context)
    else:
        return render(request, 'webapp/home.html', context=None)


def search(request):
    if request.user.is_authenticated():
        query = request.GET.get("q")
        vid_query = models.Video.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query)
        )
        file_query = models.File.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
        msg_query = models.Message.objects.filter(
            Q(sender__icontains=query) |
            Q(message__icontains=query)
        )
        ntfc_query = models.Notification.objects.filter(
            Q(sender__icontains=query) |
            Q(body__icontains=query) |
            Q(send_to__email__icontains=query) |
            Q(send_to__username__icontains=query) |
            Q(send_to__first_name__icontains=query) |
            Q(send_to__last_name__icontains=query)
        )
        img_query = models.Image.objects.filter(
            Q(name__icontains=query)
        )
        if len(vid_query) == 0 and len(msg_query) == 0 and len(ntfc_query) == 0 and len(img_query)==0 and len(file_query)==0:
            obj = 0
            return render(request, 'webapp/search.html', context={'obj': obj})
        else:
            obj = 1
            return render(request, 'webapp/search.html', context={
                            'vid_query': vid_query,
                            'msg_query': msg_query,
                            'ntfc_query': ntfc_query,
                            'img_query': img_query,
                            'file_query':file_query,
                            'obj': obj}
                          )
    else:
        return render(request, 'webapp/home.html', context=None)


def hello(request):
    return render(request, 'webapp/hello.html', None)


def delete_img(request, img_id):
    if request.user.is_authenticated():
        image_reqd = models.Image.objects.get(pk=img_id)
        image_reqd.delete()
        imgall = models.Image.objects.all()
        context = {'imgall': imgall}
        return render(request, 'webapp/img_all.html', context)
    else:
        return render(request, 'webapp/home.html', context=None)


def img_all(request):
    if request.user.is_authenticated():
        imgall = models.Image.objects.all().order_by("-uploaded_at")
        context = {'imgall': imgall }
        return render(request, 'webapp/img_all.html', context)
    else:
        return render(request, 'webapp/home.html', context=None)


def img(request, img_id):
    if request.user.is_authenticated():
        image = get_object_or_404(models.Image, pk=img_id)
        context = {'image': image}
        return render(request, 'webapp/img.html', context)
    else:
        return render(request, 'webapp/home.html', context=None)


def addimg(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = ImagesForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.extension = form.cleaned_data['img'].name.split(sep='.')[-1]
                form.instance.size = form.cleaned_data['img'].size/1024
                if form.instance.extension in imgext:
                    form.save()
                    return render(request, 'webapp/uploadsuccess.html', context=None)
                else:
                    if form.instance.extension in songext:
                        temp = 'songs'
                        ref = 'webapp:addsong'
                        k = 1


                    elif form.instance.extension in vidext:
                        temp = 'videos'
                        ref = 'webapp:vid_add'
                        k = 1
                    else:
                        temp = 'files'
                    return render(request, 'webapp/unsupportedextension.html', context={
                            'ext': form.instance.extension,
                            'temp': temp,
                            'ref':ref
                        })
        else:
            form = ImagesForm()
        return render(request, 'webapp/Forms/FileForm.html', {
            'form': form
        })
    else:
        return render(request, 'webapp/home.html', context=None)



def addalbum(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST , request.FILES )
        if form.is_valid():
            form.save()
            return render(request, 'webapp/uploadsuccess.html',context=None)
    else:
        form = AlbumForm()
    return render(request, 'webapp/Forms/FileForm.html', {
        'form': form
    })


def addsong(request):
    if request.method == 'POST':
        form = SongsForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.extension = form.cleaned_data['song'].name.split(sep='.')[-1]
            form.instance.size = form.cleaned_data['song'].size/1024
            form.save()
            return render(request, 'webapp/uploadsuccess.html',context=None)
    else:
        form = SongsForm()
    return render(request, 'webapp/Forms/FileForm.html', {
        'form': form
    })


def album_all(request):
    albumall = models.Album.objects.all()
    context = {'albumall': albumall}
    return render(request,'webapp/albumall.html',context)


def album(request, s_id):
    album_reqd = get_object_or_404(models.Album, pk=s_id)
    song_query = models.Song.objects.filter(album_i__title__exact=album_reqd.title)
    # if len(song_query) == 0:
    #     obj = 0
    #     return render(request, 'webapp/album.html', context={'obj': obj})
    # else:
    #     obj = 1
    return render(request, 'webapp/album.html', context={
        'album': album_reqd,
        'songs': song_query,
    }
                      )


def delete_file(request, file_id):
    if request.user.is_authenticated():
        file_reqd = models.File.objects.get(pk=file_id)
        file_reqd.delete()
        fileall = models.File.objects.all()
        context = {'fileall': fileall}
        return render(request, 'webapp/file_all.html', context)
    else:
        return render(request, 'webapp/home.html', context=None)


def addfile(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = FileForm(request.POST, request.FILES)
            if form.is_valid():
                k=0
                form.instance.extension = form.cleaned_data['src'].name.split(sep='.')[-1]
                form.instance.size = form.cleaned_data['src'].size / 1024

                if form.instance.extension in songext:
                    temp = 'songs'
                    ref = 'webapp:addsong'
                    k=1

                if form.instance.extension in imgext:
                    temp = 'images'
                    ref = 'webapp:img_add'
                    k=1
                elif form.instance.extension in vidext:
                    temp = 'videos'
                    ref = 'webapp:vid_add'
                    k=1
                if k==1:
                    return render(request, 'webapp/unsupportedextension.html', context={
                        'ext': form.instance.extension,
                        'temp': temp,
                        'ref':ref,
                    })
                else:
                    form.save()
                    return render(request, 'webapp/uploadsuccess.html', context=None)

        else:
            form = FileForm()
        return render(request, 'webapp/Forms/FileForm.html', {
            'form': form
        })
    else:
        return render(request, 'webapp/home.html', context=None)

def file_all(request):
    if request.user.is_authenticated():
        fileall = models.File.objects.all().order_by("-uploaded_at")
        context = {'fileall': fileall}
        return render(request, 'webapp/file_all.html', context)
    else:
        return render(request, 'webapp/home.html', context=None)

def file(request, file_id):
    if request.user.is_authenticated():
        file = get_object_or_404(models.File, pk=file_id)
        context = {'file': file}
        return render(request, 'webapp/file.html', context)
    else:
        return render(request, 'webapp/home.html', context=None)


