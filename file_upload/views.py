from django.shortcuts import render
import PyPDF2
import io
import magic
# Create your views here.
import json
import csv
from PyPDF2 import PdfReader
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        file_content = uploaded_file.read()  # Đọc nội dung của file
        # In ra nội dung của file
        print(file_content)
        # Thực hiện xử lý với file ở đây (ví dụ: lưu file vào thư mục)
        with open('uploads/' + uploaded_file.name, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        return JsonResponse({'message': 'File uploaded successfully'})

    return JsonResponse({'message': 'No file found'})
def read_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        print(uploaded_file)
        file_content = uploaded_file.read()
        print(file_content)
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file))
        print(pdf_reader)
        num_pages = len(pdf_reader.pages)
        content=""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            content+=text
            print(f"Page {page_num + 1}:\n{text}\n")
    
        
        
        return JsonResponse({'message': "done"})
    
    return JsonResponse({'message': 'No file found'})
