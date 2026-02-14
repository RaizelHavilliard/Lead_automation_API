import requests
from django.shortcuts import render
from django.http import HttpResponse

UPLOAD_URL = "https://lead-automation-api-2e5g.onrender.com/upload/"
DOWNLOAD_URL = "https://lead-automation-api-2e5g.onrender.com/download"


def upload_file(request):
    print("View called")  # مرحله 1
    if request.method == "POST":
        print("POST request received")  # مرحله 2
        try:
            file = request.FILES["file"]
            print(f"File received: {file.name}")  # مرحله 3
            files = {"file": (file.name, file, "text/csv")}
            upload_response = requests.post(UPLOAD_URL, files=files, timeout=120)
            print("Upload response received")  # مرحله 4
            upload_response.raise_for_status()

            download_response = requests.get(DOWNLOAD_URL, timeout=120)
            download_response.raise_for_status()
            print("Download response received")  # مرحله 5

        except Exception as e:
            print(f"Exception: {e}")  # مرحله 6
            return HttpResponse(f"API Error: {e}", status=500)

        return HttpResponse(
            download_response.content,
            content_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=cleaned.csv"}
        )

    return render(request, "uploader/upload.html")

