import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm

# 🧰 Helper function to save uploaded file
def handle_uploaded_file(f):
    upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
    os.makedirs(upload_dir, exist_ok=True)  # Create directory if it doesn't exist

    file_path = os.path.join(upload_dir, f.name)
    print(f'File path: {file_path}')
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# View to handle the form and file upload
@login_required
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
