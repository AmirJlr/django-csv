from django.shortcuts import render, redirect

from . forms import CsvForm
from django.contrib import messages
import csv
from .models import CSV, Player



def home_view(request):
    form = CsvForm()
    msg = 'Upload your file'

    if request.method == "POST":
        csv_file = request.FILES["csv_upload"]

        if not csv_file.name.endswith('.csv'):
            msg = 'Wrong format, file must be <csv>'

        else:
            file_data = csv_file.read().decode("ISO-8859-1")
            print(file_data)
            msg = 'Sucessfully Uploaded !'

            csv_data = file_data.split("\n")
            
 
            for x in csv_data[1:]:
                if x == '':
                    continue
                fields = x.split(",")
                
                created = Player.objects.update_or_create(
                    name = fields[0],
                    club = fields[1],
                    nationality = fields[2],
                    position = fields[3],
                    age = fields[4],
                    matches = fields[5],
                    )
            
            return redirect('home')

    context = {
        'form':form,
        'msg': msg,
    }

    return render(request, 'home.html', context)


# def csv_upload_view(request):
#     print('file is being')

#     if request.method == 'POST':
#         csv_file_name = request.FILES.get('file').name
#         csv_file = request.FILES.get('file')
#         obj, created = CSV.objects.get_or_create(file_name=csv_file_name)

#         if created:
#             obj.csv_file = csv_file
#             obj.save()

#             with open(obj.csv_file.path, 'r') as f:
#                 reader = csv.reader(f)
#                 reader.__next__()
#                 for row in reader:
#                     data = "".join(row)
#                     data = data.split(';')
#                     data.pop()
        
#                     transaction_id = data[1]
#                     product = data[2]
#                     quantity = int(data[3])
#                     customer = data[4]
#                     date = parse_date(data[5])

#                     try:
#                         product_obj = Product.objects.get(name__iexact=product)
#                     except Product.DoesNotExist:
#                         product_obj = None

#                     if product_obj is not None:
#                         customer_obj, _ = Customer.objects.get_or_create(name=customer) 
#                         salesman_obj = Profile.objects.get(user=request.user)
#                         position_obj = Position.objects.create(product=product_obj, quantity=quantity, created=date)

#                         sale_obj, _ = Sale.objects.get_or_create(transaction_id=transaction_id, customer=customer_obj, salesman=salesman_obj, created=date)
#                         sale_obj.positions.add(position_obj)
#                         sale_obj.save()
#                 return JsonResponse({'ex': False})
#         else:
#             return JsonResponse({'ex': True})

#     return HttpResponse()
