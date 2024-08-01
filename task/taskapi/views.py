from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotAllowed
from django.core.exceptions import ObjectDoesNotExist
from .models import Product,Inventories


##Products Apis 

@csrf_exempt

def CreateProduct(request):
    if request.method == "POST":
        data=json.load(request)
        try:
            product=Product.objects.create(name=data['name'],quantity=data['quantity'],type=data['type'],invname=data['invname'])
            response = {"message": "Product created successfully",}

            return HttpResponse( json.dumps(response),  status=200)
        except Exception as e:
            response = {"error": str(e), }
            return HttpResponse( json.dumps(response),  status=400
            )
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
    
@csrf_exempt

def FetchProduct(request):
    if request.method == "POST":
        data=json.load(request)
        try:
            product=Product.objects.get(name=data['name'])
            response = {
            "name": product.name,
            "quantity": product.quantity,
            "type": product.type,
            "invname": product.invname,
            }
            return HttpResponse( json.dumps(response),  status=200)
        except Exception as e:
            response = {
            "error": str(e),
            }
            return HttpResponse( json.dumps(response),  status=400)
    else:       
        return JsonResponse({"error": "Invalid request method"}, status=405)
    
@csrf_exempt
   
def DeleteProduct(request):
    if request.method == "POST":
        data=json.load(request)
        try:
            product=Product.objects.get(name=data['name'])
            product.delete()
            response = {
            "message": "Product deleted successfully",
            }
            return HttpResponse( json.dumps(response),  status=200)
        except Exception as e:
            response = {
            "error": str(e),
            }
            return HttpResponse( json.dumps(response),  status=400)
    else:    
        return JsonResponse({"error": "Invalid request method"}, status=405)
    
@csrf_exempt

def UpdateProduct(request):
    if request.method == "POST":
        data=json.load(request)
        try:
            product=Product.objects.get(name=data['name'])
            datatobeupdated=data["datatobeupdated"]
            
            if 'name' in datatobeupdated:
                product.name=datatobeupdated['name']
            if 'quantity' in datatobeupdated:
                product.quantity=datatobeupdated['quantity']
            if 'type' in datatobeupdated:
                product.type=datatobeupdated['type']
            if 'invname' in datatobeupdated:
                product.invname=datatobeupdated['invname']
            product.save()
            response = {
            "message": "Product updated successfully",
            }
            return HttpResponse( json.dumps(response),  status=200)
        except Exception as e:
            response = {
            "error": str(e),
            }
            return HttpResponse( json.dumps(response),  status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)

##inventories Apis

@csrf_exempt

def CreateInventory(request):
    if request.method == "POST":
        data=json.load(request)
        try:
            inventory=Inventories.objects.create(name=data['name'],capacity=data['capacity'],location=data['location'])
            response = {
            "message": "Inventory created successfully",
            }
            return HttpResponse( json.dumps(response),  status=200)
        except Exception as e:
            response = {
            "error": str(e),
            }
            return HttpResponse( json.dumps(response),  status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)    
        
@csrf_exempt

def FetchInventory(request):
    if request.method == "POST":
        data=json.load(request)
        try:
            inventory=Inventories.objects.get(name=data['name'])
            response = {
            "name": inventory.name,
            "capacity": inventory.capacity,
            "location": inventory.location,
        
            }
            return HttpResponse( json.dumps(response),  status=200)
        except Exception as e:
            response = {
            "error": str(e),
            }
            return HttpResponse( json.dumps(response),  status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
    
@csrf_exempt
   
def DeleteInventory(request):
    if request.method == "POST":
        data=json.load(request)
        try:
            inventory=Inventories.objects.get(name=data['name'])
            inventory.delete()
            response = {
            "message": "Inventory deleted successfully",
            }
            return HttpResponse( json.dumps(response),  status=200)
        except Exception as e:
            response = {
            "error": str(e),
            }
            return HttpResponse( json.dumps(response),  status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)   
    
@csrf_exempt

def UpdateInventory(request):
    if request.method == "POST":
        data=json.load(request)
        try:
            inventory=Inventories.objects.get(name=data['name'])
            datatobeupdated=data["datatobeupdated"]
            
            if 'name' in datatobeupdated:
                inventory.name=datatobeupdated['name']
            if 'capacity' in datatobeupdated:
                inventory.capacity=datatobeupdated['capacity']
            if 'location' in datatobeupdated:
                inventory.location=datatobeupdated['location']
            inventory.save()
            response = {
            "message": "Product updated successfully",
            }
            return HttpResponse( json.dumps(response),  status=200)
        except Exception as e:
            response = {
            "error": str(e),
            }
            return HttpResponse( json.dumps(response),  status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
        


##Joining Products and Inventories Api
@csrf_exempt
def Joinning(request):
    if request.method == "POST":
        try:
            # Fetch products
            products = Product.objects.all()
            # Create a dictionary for inventory data keyed by 'name'
            inventory_dict = {
                inv.name: inv for inv in Inventories.objects.all()
            }
            result = []
            for product in products:
                inv = inventory_dict.get(product.invname, None)
                if inv:
                    result.append({
                        'name': product.name,
                        'quantity': product.quantity,
                        'type': product.type,
                        'invname': product.invname,
                        'capacity': inv.capacity,
                        'location': inv.location
                    })
            response = {
                "results": result,
            }
            return JsonResponse(response, status=200)
        except Exception as e:
            response = {
                "error": str(e),
            }
            return JsonResponse(response, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)