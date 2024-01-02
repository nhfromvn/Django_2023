from django.shortcuts import render
import PyPDF2
import io
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:

        uploaded_file = request.FILES['file'].read()
        
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file))
        print(pdf_reader)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            print(f"Page {page_num + 1}:\n{text}\n")
        # NumPages = len(pdf_reader.pages)
        # i = 0
        # content = []
        # while (i<NumPages):
        #     text =  pdf_reader.pages(i)
        #     content.append(text.extractText())
        #     i +=1
        # print(content)
        # file_content = uploaded_file.read().decode('utf-8')  # Đọc nội dung của file
        # In ra nội dung của file
        # print(file_content)
        # Thực hiện xử lý với file ở đây (ví dụ: lưu file vào thư mục)
        # with open('uploads/' + uploaded_file.name, 'wb+') as destination:
        #     for chunk in uploaded_file.chunks():
        #         destination.write(chunk)
        
        
        return JsonResponse({'message': "success"})
    
    return JsonResponse({'message': 'No file found'})
