from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.views.decorators.cache import never_cache
from django.contrib import messages

@never_cache
def pos_billing(request):
    #try:
       if request.session['username']:
         u = request.session['username']
         products = Products.objects.filter(p_belong=u).values()
         categ = Category.objects.filter(cat_belong=u).values()
         carts = Cart.objects.filter(cart_user =u).values()
         con = {
            'products': products,
            'categ': categ,
            'carts':carts,
         }
         return render(request,'pos_home.html',con)
    #except:
    #   response = redirect('/pos_login')
    #   return response
def pos_login(request):
  if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        try:   
         user = Users.objects.get(username=u,password=p)
         if user: 
          request.session['username'] = user.id
          response = redirect('/')
          return response
        except:
           response = redirect('/pos_login')
           return response
  else:
    return render(request, 'pos_login.html')

def add_cart(request):
  if request.session['username']:
    if request.method == 'POST':
        p = request.POST.getlist('prod')
        q = request.POST.getlist('quan')
        if (len(p)<=0):
           messages.info(request,"NO products has selected")
        else:   
         u = request.session['username']
         i=0
         while i<len(p):
           price = Products.objects.get(p_belong=u,p_id=p[i])
           print(price.p_price)
           cart = Cart.objects.filter(cart_user=Users.objects.get(id=u),cart_bp=price.p_id)
           if not cart:
              cart = Cart()
              cart.cart_user = Users.objects.get(id=u) 
              cart.cart_bp = price.p_id
              cart.cart_data = int(q[i])
              cart.save()
           else:
              cart = Cart.objects.get(cart_user=Users.objects.get(id=u),cart_bp=price.p_id)
              cart.cart_data += int(q[i]) 
              cart.save()
           i=i+1
         messages.info(request,"Products Updated")
        response = redirect('/')
        return response
  response = redirect('/pos_login')  
  return response

def check(request):
   if request.session['username']:
     u = request.session['username']
     carts = Cart.objects.filter(cart_user=Users.objects.get(id=u),cart_live=1)
     deta = {}
     for i in carts:
        deta.update({i.cart_name:i.cart_number})
     print(deta)
     c = [
        ['Payment Methods', 'Data'],
        ['Upi',     50],
        ['Cash',      100],
        ['Card', 250],
        ]
     b = [
          ['Day', 'Revenue'],
          ["Today", 10],
          ["Day - 1", 31],
          ["Day - 2", 12],
          ["Day - 3", 10],
          ['Day - 4', 30]
        ]
     con = { 'pie':c,
          'bar':b,
           'carts':deta }
     return render(request,'cart.html',con)