from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .camera import detect_faces_eyes_stream
from .color_shape import analyze_image_colors_shapes
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def index(request):
    return render(request, 'index.html')
def camera_view(request):
    # This view will run a blocking OpenCV stream on the server side.
    # For development/local use only. It opens the machine's camera.
    detect_faces_eyes_stream()
    return redirect('index')
def analyze_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        img = request.FILES['image']
        fs = FileSystemStorage(location=os.path.join(BASE_DIR, 'uploads'))
        os.makedirs(fs.location, exist_ok=True)
        filename = fs.save(img.name, img)
        full_path = fs.path(filename)
        out, colors, shapes = analyze_image_colors_shapes(full_path)
        # move result image to uploads to serve
        dest = os.path.join(fs.location, out)
        try:
            os.replace(out, dest)
        except Exception:
            pass
        context = {'analyzed_image': fs.url(out), 'colors': colors, 'shapes': shapes}
        return render(request, 'index.html', context)
    return render(request, 'index.html')
