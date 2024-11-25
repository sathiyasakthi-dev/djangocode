#from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
#from django.shortcuts import redirect
from .models import sathiya
#from .models import Post
from django.shortcuts import render
#from .forms import Userinfoform
#from django.http import HttpResponse
## JWT TOKEN
#from rest_framework.decorators import api_view,permission_classes
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.response import Response
#from rest_framework import viewsets
#from .models import Item
#from .serializers import ItemSerializer
#class ItemViewSet(viewsets.ModelViewSet):
 #   queryset = Item.objects.all()
  #  serializer_class = ItemSerializer
# Create your views here.
# need to response to display the direct data
#def fun(request):
 #   return HttpResponse("<h1> students <h1>")
#def index(request):
 #   return HttpResponse("hello world,this is my first django  project")
# dic only allowed to pass as argumnents
#def my_view(request):
 #   a={"title":"python"}
  #  return render (request,'index.html',a)
#define list and pass as value in dict
#like this u can pass tuple
#def list(request):
 #   a=[10,20,30,40,50]
  #  dict={"list":a}
   # return render(request,"list.html",dict)
# get data from form and display
#def form (request):
 #   if request .method == 'POST':
        # get form data from request.post dictionary
  #      username=request.POST.get('username')
   #     email=request.POST.get('email')
        #do something with the received data
    #    return HttpResponse(f"received username:{username},received email:{email}")
    #render template with the form
    #return render(request,'form.html')
#''' store user data in database  using[python manage.py make migrations (make changes),python manage .py migrate (connectdatabase)]'''

def add_db(request):
       if request.method== 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        sathiya.objects .create(name=name,age=age)
    #    return HttpResponseRedirect('/success')
        return "data added successfully"
       return render(request,'add_db.html')
#def success(request):
 #   persons=Person.objects.all()
  #  print(persons)
   # return render(request,"success.html",{"persons":persons})
#def delete(request,pername,perage):
 #   pers=Person.objects.get(name=pername)
  #  pers.delete()
   # return HttpResponseRedirect("/success")
#def update(request,pername,perage):
 #   person=Person.objects.get(name=pername)
  #  if request.method=="POST":
   #     newname=request.POST.get("name")
    #    newage=request.POST.get("age")
     #   person.name=newname
      #  person.age=newage
       # person.save()
        #return redirect("/success")
   # return render(request,"update.html",{"person":person})
# from django.shortcuts import render,get_object_or_404
#def post_list(request):
 #   posts=Post.objects.all()
  #  return render(request,'post_list.html',{'posts':posts})
#def post_detail(request, pk):
 #   post = get_object_or_404(Post,pk=pk)
  #  return render(request,'post_detail.html',{'post':post})




#def fun4(request):
 #   a=100
  #  return HttpResponse(a)
#def fun5(request):
 #   new=fun4(request)
  #  return HttpResponse(new)

#def index(request):
 #   if 'name' in request.session:
  #      name=request.session['name']
   #     return HttpResponse(f"Hello,{name}! welcome back.")
    #return render(request,'session.html')
#def set_name(request):
 #   if request.method == 'POST':
  #      name=request.POST.get('name')
   #     request.session['name']= name
    #    return HttpResponse("Name storedin session")
    #return HttpResponse("Invalid request.")
#def delete_name(request):
 #   if 'name' in request.session:
  #      del request.session['name']
   #     return HttpResponse("Name deleted from session.")
   # return HttpResponse("No name found in session") 
#@api_view(['GET'])
#@permission_classes([IsAuthenticated])
#def example_view(request):
 #   content={'message':'Authenticated!'}
  #  return Response(content)
#def user_info(request):
 #   if request.method == 'POST':
  #      form = Userinfoform(request.POST)
   #     if form.is_valid():
            #process the form data
    #        name = form.cleaned_data['name']
     #       email = form.cleaned_data['email']
            # you cana do further processing here,such as saving data to 
            # for simplicity ,we'll  just print the data.
      #      print(f"Name: {name},Email:{email}")
    #else:
     #   form=Userinfoform()
    #return render(request,'user_info.html',{'form': form})
