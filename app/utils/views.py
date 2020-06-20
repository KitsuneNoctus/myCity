from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, "index.html", {})


def creators(request):
    return render(request, "creators.html", {})


def image_upload(request):
    fs = FileSystemStorage()
    all_photos = fs.listdir(fs.base_location)

    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url, "all": all_photos
        })
    return render(request, "upload.html", {"all": all_photos})


def resources(request):
    return render(request, "resources.html", {})

def benefits(request):
    return render(request, "benefits.html", {})

# def pandemic_info(request):
#     return render(request, "pandemic_info.html", {})

def shelter_info(request):
    return render(request, "shelter_info.html", {})

def food_locations(request):
    return render(request, "food_locations.html", {})

def legal_help(request):
    return render(request, "legal_help.html", {})
