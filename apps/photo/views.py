from datetime import datetime
from PIL import Image, ImageDraw
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.conf import settings


class GenerateImageView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        images = request.FILES.getlist('image_files')
        responses = []

        for image in images:
            original_image = Image.open(image)
            draw = ImageDraw.Draw(original_image)
            width, height = original_image.size
            for x in range(0, width, 80):
                draw.line([(x, 0), (x, height)], fill="red", width=1, joint="curve")
            for y in range(0, height, 80):
                draw.line([(0, y), (width, y)], fill="red", width=1, joint="curve")
            original_image = original_image.convert('RGB')
            curent_time = datetime.now().strftime("%H:%M:%S")
            processed_image_path = f"{settings.MEDIA_ROOT}/processed_image_{image.name}-{curent_time}.jpg"
            logo = Image.open("static/img/logo/logo.png")
            logo_width, logo_height = 150, 150
            original_image.paste(logo, (width - logo_width, height - logo_height))
            original_image.save(processed_image_path)
            responses.append({
                'image_url': f"https://9e24-84-54-120-115.ngrok-free.app/media/processed_image_{image.name}-{curent_time}.jpg",
                'upload_image': f"media/processed_image_{image.name}-{curent_time}.jpg",
                'width': f"{width}px",
                'name': f"{image.name}",
                'height': f"{height}px",
            })

        return Response(responses, status=status.HTTP_200_OK)