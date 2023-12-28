from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        file_content = uploaded_file.read().decode('utf-8')  # Đọc nội dung của file

        # In ra nội dung của file
        print(file_content)
        # Thực hiện xử lý với file ở đây (ví dụ: lưu file vào thư mục)
        with open('uploads/' + uploaded_file.name, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        
        return JsonResponse({'message': 'File uploaded successfully'})
    
    return JsonResponse({'message': 'No file found'})
