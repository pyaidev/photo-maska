from django.shortcuts import render
from django.views.generic import ListView
from apps.common.mixins import overlay_grid_and_logo




def index(request):
    image = request.FILES.get('image_file')
    print(image)

    if image:
        overlay_grid_and_logo(image, 'result.png')
        return render(request, 'index.html', {'image': 'result.png'})
    return render(request, 'index.html')








