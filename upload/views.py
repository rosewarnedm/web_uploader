from django.shortcuts import render

# Create your views here.

# upload/views.py

from django.shortcuts import render, redirect
from .forms import UploadFileForm
import os

# Function to handle saving the uploaded file
def handle_uploaded_file(f):
    path = os.path.join('/Users/dmr/Desktop/uploads', f.name)
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# View to handle the form and file upload
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('success')
    else:
        form = UploadFileForm()
    return render(request, 'upload/upload.html', {'form': form})

# Success view
def success(request):
    return render(request, 'upload/success.html')
