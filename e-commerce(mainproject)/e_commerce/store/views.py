from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Customer,Category,Product,Orders,CartItem,wishlist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
def login1(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['psw']
        user=authenticate(request,username=username,password=password)
        if user is not None and user.is_superuser==1:
            login(request,user)
            return render(request,'admin_home.html')
            return HttpResponse("ok")
        if Customer.objects.filter(username=username,password=password).exists():
            customer=Customer.objects.filter(username=username,password=password)
            for i in customer:
                request.session['customer_id']=i.id
                a=Category.objects.all()
                user=request.session['customer_id']
              
                customer=Customer.objects.get(id=user)
                items=Orders.objects.filter(customer=user)
                # user=request.session['customer_id']
                wishlist_items=wishlist.objects.filter(customer=user)
                wishlist_count=wishlist_items.count()
                user_cart_items=CartItem.objects.filter(customer=user)
                count=user_cart_items.count()
               
             
                return render(request,'index.html',{'categorys':a,'count':count,'customer':customer,'wishlist_count':wishlist_count,'check_items':items})
        return HttpResponse("invalid username and password")
    else:
         return render(request,'login.html')
def signup(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        username=request.POST['uname']
        phone=request.POST['ph']
        password=request.POST['psw']
        email=request.POST['em']
        customer=Customer.objects.create(Firstname=firstname,Lastname=lastname,username=username,phone=phone,email=email,password=password)

        # return HttpResponse('Details registered')
        return redirect(login1)
    category=Category.objects.all()
    user=request.session['customer_id']
    user_cart_items=CartItem.objects.filter(customer=user)
    count=user_cart_items.count()
    wishlist_items=wishlist.objects.filter(customer=user)
    wishlist_count=wishlist_items.count()
    customer=Customer.objects.get(id=user)

    
    return render(request,'register.html',{'categorys':category,'count':count,'wishlist_count':wishlist_count,'customer':customer})
def home(request):
    return render(request,'index.html')
def add_products(request):
    return render(request,'add_products.html')
def index(request):
    a=Category.objects.all()
    b=Product.objects.all()
    user=request.session['customer_id']
    user_cart_items=CartItem.objects.filter(customer=user)
    count=user_cart_items.count()
    wishlist_items=wishlist.objects.filter(customer=user)
    wishlist_count=wishlist_items.count()
    items=Orders.objects.filter(customer=user)
    customer=Customer.objects.get(id=user)
    return render(request,'index.html',{'categorys':a,'count':count,'wishlist_count':wishlist_count,'check_items':items,'customer':customer})
def base(request):
    a=Category.objects.all()
    return render(request,'product-detail.html',{'categorys':a})
# def viewproducts(request,category_id):
#     category=Category.objects.get(pk=category_id)
#     products=Product.objects.filter(category=category)
#     return render(request,'category.html',{'products':products})


def cart1(request):
    return render(request,'cart.html')
def view_category(request):
    a=Category.objects.all()
    return render(request,'view_category.html',{'categories':a})
def adminhome(request):
    return render(request,'admin_home.html')

def delete_category(request,category_id):
    Category.objects.get(id=category_id).delete()
    return redirect(view_category)
def edit_category(request,category_id):
    a=Category.objects.get(id=category_id)
    if request.method=='POST':
        name=request.POST['name']
        Category.objects.filter(id=category_id).update(name=name)
        # messages.success(request,'changed')
        return redirect(view_category)
    return render(request,'Edit_category.html',{'category':a})
def view_product(request):
    products=Product.objects.all()
    count=products.count()
    return render(request,'view_products.html',{'products':products,'count':count})
def add_products(request):
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        image=request.FILES.get('file_img')
        category_id=request.POST.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        Product.objects.create(Name=name,Price=price,image=image,category=category)
        return redirect(
            view_product
        )
    a=Category.objects.all()
    return render(request,'add_products.html',{'categories':a})
def edit_product(request,eid):
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        # image=request.FILES.get('file_img')
        # category_id=request.POST.get('category')
        # category = get_object_or_404(Category, pk=category_id)

        Product.objects.filter(id=eid).update(Name=name,Price=price)
        return redirect(view_product)
        # return HttpResponse("okk")
    p=Product.objects.get(id=eid)
    return render(request,'Edit_product.html',{'product':p})
def delete_product(request,pid):
    Product.objects.get(id=pid).delete()
    return redirect(view_product)

def products_by_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    user=request.session['customer_id']
    customer=Customer.objects.get(id=user)
    user_cart_items=CartItem.objects.filter(customer=user)
    count=user_cart_items.count()
    wishlist_items=wishlist.objects.filter(customer=user)
    wishlist_count=wishlist_items.count()
    product_count=products.count()
    return render(request, 'store.html', 
                  {'category': category, 
                   'products': products,
                   'categories':categories,
                   'count':count,
                   'wishlist_count':wishlist_count,
                   'wishlist':wishlist_items,
                   'customer':customer,
                   'product_count':product_count})
    

def product_detail(request,product_id):
     p=Product.objects.get(id=product_id)
     a=Category.objects.all()
     user=request.session['customer_id']
     customer=Customer.objects.get(id=user)
     user_cart_items=CartItem.objects.filter(customer=user)
     count=user_cart_items.count()
     wish_items=wishlist.objects.filter(customer=user)
     wish_count=wish_items.count()
     return render(request,
     'product-detail.html',
     {'products':p,
     'categorys':a,
     'count':count,
     'cartitems':user_cart_items,
     'wish_count':wish_count,
     'customer':customer})
          
  
def cart(request):
    category=Category.objects.all()
    a=request.session['customer_id']
    customer=Customer.objects.get(id=a)
    cart_items=CartItem.objects.filter(customer=a)
    wishlist_items=wishlist.objects.filter(customer=a)
    count=cart_items.count()
    wishlist_count=wishlist_items.count()
    total_price = sum(item.product.Price * item.quantity for item in cart_items)
    product=Product.objects.all()
    if cart_items:
         return render(request,'cart2.html',
         {'cart_items':cart_items,
         'categorys':category,
         'count':count,
         'total':total_price,
         'wish_count':wishlist_count,
         'customer':customer})
    else:
        return render(request,'cart_empty.html',{'categorys':category,'customer':customer,'count':count,'wish_count':wishlist_count})
def view_cart(request):
    customer=Customer.objects.get(id=request.session.get('customer_id'))
    cart_items=CartItem.objects.filter(customer=customer)
    all_total_price=sum(item.product.Price*item.quantity for item in cart_items)
    
    return render(request,'category.html',{'cart_items':cart_items,'total':all_total_price})
def add_to_cart(request,product_id):
    if request.method=='POST':
        product=Product.objects.get(id=product_id)
        a=request.session['customer_id']
        customer=Customer.objects.get(id=a)
        quantity=request.POST['qtn']
    
        # tamount=quantity*product.Price
    
        if CartItem.objects.filter(customer=customer,product=product).exists():
            # a='good morning'
            messages.add_message(request,messages.INFO,"Item is already exists in the cart.")
            # return HttpResponse("item is already in the cart")
            return redirect(cart)
        else:
             CartItem.objects.create(customer=customer,product=product,quantity=quantity)
             all_cart_items=CartItem.objects.all()
             count=all_cart_items.count()
             count=count+1
        return redirect(index)
def remove_from_cart(request, cart_item_id):
    CartItem.objects.get(id=cart_item_id).delete()
    messages.success(request, "Item removed from your cart.")
    return redirect(cart)

def view_wishlist(request):

    user=request.session['customer_id']
    customer=Customer.objects.get(id=user)
    category=Category.objects.all()
    wishlist_items=wishlist.objects.filter(customer=user)
    wishlist_count=wishlist_items.count()
    cart_items=CartItem.objects.filter(customer=user)
    cart_count=cart_items.count()
    if wishlist_items:
            return render(request,
                          'wishlist.html',
                          {'wishlist_items':wishlist_items,
                           'categorys':category,
                           'wishlist_count':wishlist_count,
                           'cart_count':cart_count,
                           'customer':customer}
                           )
    else:
        return render(request,'wishlist_empty.html',{'categorys':category,'customer':customer,'count':cart_count,'wish_count':wishlist_count})
def account(request):
    user=request.session['customer_id']
    customer=Customer.objects.get(id=user)
    category=Category.objects.all()
    wishlist_items=wishlist.objects.filter(customer=user)
    wishlist_count=wishlist_items.count()
    cart_items=CartItem.objects.filter(customer=user)
    cart_count=cart_items.count()

    # items=Orders.objects.filter(customer=user)
    return render(request,'myaccount.html',{'customer':customer,'categorys':category,'wish_count':wishlist_count,'count':cart_count})
def editaccount(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        username=request.POST['uname']
        phone=request.POST['Phone']
        email=request.POST['email']
        password=request.POST['psw']
        customer=request.session['customer_id']
        x=Customer.objects.filter(id=customer).update(Firstname=firstname,
                                                      Lastname=lastname,
                                                      username=username,
                                                      phone=phone,
                                                      email=email,
                                                      password=password)
        return redirect(account)

        


def add_wishlist(request,product_id):
        product=Product.objects.get(id=product_id)
        a=request.session['customer_id']
        customer=Customer.objects.get(id=a)
        if wishlist.objects.filter(customer=customer,product=product).exists():
            messages.success(request,"item is alredy in your wishlist")
            return redirect(view_wishlist)

            
            # messages.error(request,"item is already in your wishlist")
        else:
            wishlist.objects.create(customer=customer,product=product,quantity=1)
            all_wishlist_items=wishlist.objects.all()
            count=all_wishlist_items.count()
            count=count+1
            
        return redirect(view_wishlist)
       
def remove_wishlist(request,item_id):
    wishlist.objects.get(id=item_id).delete()
    return redirect(view_wishlist)
        
def checkout(request):
    if request.method=='POST':
        a=request.session['customer_id']
        customer=Customer.objects.get(id=a)
        cart_items=CartItem.objects.filter(customer=customer)
        addres=request.POST['address']
        phone=request.POST['Phone']
        for items in cart_items:
            quantity=items.quantity
            price=items.product.Price
            Orders.objects.create(
                customer=customer,
                product=items.product,
                Quantity=quantity,
                Price=price,
                Address=addres,
                Phone=phone
                )
        cart_items.delete()
        return render(request,'cart_empty.html')

           
    
           
def view_orders(request):
    category=Category.objects.all()
    user=request.session['customer_id']
    customer=Customer.objects.get(id=user)
    cart_items=CartItem.objects.filter(customer=user)
    count=cart_items.count()
    wishlist_items=wishlist.objects.filter(customer=user)
    wishlist_count=wishlist_items.count()
    order_items=Orders.objects.filter(customer=user)
    if order_items:
        return render(request,'orders.html',{'orders':order_items,'count':count,'wishlist_count':wishlist_count,'customer':customer,'categorys':category})
    else:
        return render(request,'order_empty.html')
def add_category(request):
    if request.method=='POST':
        name=request.POST['name']
        a=Category.objects.create(name=name)
        messages.success(request,'added')
        return redirect(add_category)
    return render(request,'add_category.html') 


   