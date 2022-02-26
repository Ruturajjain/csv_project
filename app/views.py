from audioop import reverse
from cmath import e
import csv
import io
import logging
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, response
from django.shortcuts import render

from app.models import Employee

# Create your views here.

def home(request):
    return render(request, template_name='home.html')



def csv_export(request):
    all_active_data = Employee.objects.filter(active=True)
    # print(all_active_data)
    # return HttpResponse(all_active_data)
    response = HttpResponse(content_type='text/csv')
    csv_writer = csv.writer(response)
    csv_writer.writerow(['ID', 'Name', 'Salary', 'Company', 'Designation', 'DOJ', 'Active'])
    
    for emp in all_active_data.values_list('id','name','salary','company','designation','DOJ','active'):
        csv_writer.writerow(emp)
        
    response['Content-Disposition'] = 'attachment; filename="employee_data.csv"'
    return response




def upload_csv(request):
	data = {}
	if "GET" == request.method:
		return render(request, "upload1.html", data)
    # if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("upload_csv"))
        #if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("upload_csv"))

		file_data = csv_file.read().decode("utf-8")
		lines = file_data.split("\n")
		print(file_data)
		#loop over the lines and save them in db. If error , store as string and then display
		
			

	except Exception as e:
		messages.error(request,"Unable to upload file. "+repr(e))
		return HttpResponseRedirect(reverse("upload_csv"))
	return HttpResponse("Data upload successfully")



# def upload_csv(request):
#     template = "upload.html"
#     data = Employee.objects.all()
#     prompt = {
#         'order': 'Order of the CSV should be name, salary, company, designation, DOJ, active',
#         'profiles': data
#         }
#     if request.method == "GET":
#         return render(request, template, prompt)

#     csv_file = request.FILES['file']
#     if not csv_file.name.endswith('.csv'):
#         print ('THIS IS NOT A CSV FILE')

#     data_set = csv_file.read().decode('UTF-8')
#     io_string = io.StringIO(data_set)
#     next(io_string)
#     for column in csv.reader(io_string, delimiter=',', quotechar="|"):_, created = Employee.objects.update_or_create(
#             id =column[0],
#             name=column[1],
#             salary=column[2],
#             company=column[3],
#             designation=column[4],
#             DOJ=column[5],
#             active=column[6]
#         )
#     context = {}
#     return render(request, template, context)