from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost,Gallery,Animals,Accessories,Nature,Monuments,Heritage,HolyPlaces,Vehicles,DefenceBlog,SoftwareBlog
from django.core.paginator import Paginator
# Create your views here.
def index(request):
 gallery=Gallery.objects.all()
 page = request.GET.get('page', 1)
 paginator = Paginator(gallery, 20)
 try:
        photos = paginator.page(page)
 except PageNotAnInteger:
        photos = paginator.page(1)
 except EmptyPage:
        photos = paginator.page(paginator.num_pages)
 return render(request,'blog/home.html',{'gallery':gallery,'photos':photos})

def blogview(request):
    myposts=BlogPost.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(myposts, 10)
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    return render(request,'blog/blogview.html',{'myposts':myposts})   

def defenceblog(request):
    myposts=DefenceBlog.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(myposts, 10)
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    return render(request,'blog/blogview.html',{'myposts':myposts})  

def softwareblog(request):
    myposts=SoftwareBlog.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(myposts, 10)
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    return render(request,'blog/blogview.html',{'myposts':myposts})  


def blogpost(request,id):
    post=BlogPost.objects.filter(post_id=id)[0]
    return render(request,'blog/blogpost.html',{'post':post})   

def defence_blogpost(request,id):
    post=DefenceBlog.objects.filter(post_id=id)[0]
    return render(request,'blog/blogpost.html',{'post':post}) 

def software_blogpost(request,id):
    post=SoftwareBlog.objects.filter(post_id=id)[0]
    return render(request,'blog/blogpost.html',{'post':post}) 

def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'blog/Contact.html', {'thank': thank})    

def Imageview(request,myid):
    gallery=Gallery.objects.filter(id=myid)
    image=gallery[0].image     
    return render(request,"blog/Imageview.html",{'image':image})

def animals_Imageview(request,myid):
    gallery=Animals.objects.filter(id=myid)
    image=gallery[0].image     
    return render(request,"blog/Imageview.html",{'image':image})

def accessories_Imageview(request,myid):
    gallery=Accessories.objects.filter(id=myid)
    image=gallery[0].image     
    return render(request,"blog/Imageview.html",{'image':image})

def nature_Imageview(request,myid):
    gallery=Nature.objects.filter(id=myid)
    image=gallery[0].image     
    return render(request,"blog/Imageview.html",{'image':image})

def heritage_Imageview(request,myid):
    gallery=Heritage.objects.filter(id=myid)
    image=gallery[0].image     
    return render(request,"blog/Imageview.html",{'image':image})

def monuments_Imageview(request,myid):
    gallery=Monuments.objects.filter(id=myid)
    image=gallery[0].image     
    return render(request,"blog/Imageview.html",{'image':image})

def holyplaces_Imageview(request,myid):
    gallery=HolyPlaces.objects.filter(id=myid)
    image=gallery[0].image     
    return render(request,"blog/Imageview.html",{'image':image})

def vehicles_Imageview(request,myid):
    gallery=Vehicles.objects.filter(id=myid)
    image=gallery[0].image     
    return render(request,"blog/Imageview.html",{'image':image})

def searchMatch(query,item):
    if query  in item.title.lower() or query  in item.category.lower():
        return True
    else:
       return False

def search(request):
    query=request.GET.get('search')
    allProds = []
    catprods = Gallery.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodItem = Gallery.objects.filter(category=cat)
        prod=[item for item in prodItem if searchMatch(query,item)]
        if len(prod) != 0:
           allProds.append(prod)
    page = request.GET.get('page', 1)
    paginator = Paginator(allProds, 20)
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    params = {'allProds': allProds,'msg':'','photos':photos}    
    if len(allProds) == 0 or len(query)<4:
        params = { 'msg': 'Please make sure to enter relevant search query'}   
    return render(request, 'blog/search.html', params)    

def animals_photo(request):
   gallery=Animals.objects.all()
   page = request.GET.get('page', 1)
   paginator = Paginator(gallery, 20)
   try:
        photos = paginator.page(page)
   except PageNotAnInteger:
        photos = paginator.page(1)
   except EmptyPage:
        photos = paginator.page(paginator.num_pages)
   return render(request,'blog/photos.html',{'gallery':gallery,'photos':photos})

def accessories_photo(request):
    gallery=Accessories.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(gallery, 20)
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    return render(request,'blog/accessories_photos.html',{'gallery':gallery,'photos':photos})

def nature_photo(request):
   gallery=Nature.objects.all()
   page = request.GET.get('page', 1)
   paginator = Paginator(gallery, 20)
   try:
        photos = paginator.page(page)
   except PageNotAnInteger:
        photos = paginator.page(1)
   except EmptyPage:
        photos = paginator.page(paginator.num_pages)
   return render(request,'blog/nature_photo.html',{'gallery':gallery,'photos':photos})

def heritage_photo(request):
    gallery=Heritage.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(gallery, 20)
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    return render(request,'blog/heritage_photo.html',{'gallery':gallery,'photos':photos})

def monuments_photo(request):
   gallery=Monuments.objects.all()
   page = request.GET.get('page', 1)
   paginator = Paginator(gallery, 20)
   try:
        photos = paginator.page(page)
   except PageNotAnInteger:
        photos = paginator.page(1)
   except EmptyPage:
        photos = paginator.page(paginator.num_pages)
   return render(request,'blog/monuments_photo.html',{'gallery':gallery,'photos':photos})

def vehicles_photo(request):
    gallery=Vehicles.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(gallery, 20)
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    return render(request,'blog/vehicles_photo.html',{'gallery':gallery,'photos':photos})

def holyplaces_photo(request):
    gallery=HolyPlaces.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(gallery, 20)
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    return render(request,'blog/holyplaces_photo.html',{'gallery':gallery,'photos':photos})