import requests
from django.shortcuts import render
from django.http import HttpResponse

UPLOAD_URL = "https://lead-automation-api-2e5g.onrender.com/upload/"
DOWNLOAD_URL = "https://lead-automation-api-2e5g.onrender.com/download"

def upload_file(request):
    if request.method == "POST":
        file = request.FILES["file"]

        try:
            upload_response = requests.post(
                UPLOAD_URL,
                files = {
                    "file": (file.name, file.read(), "text/csv")
                }

                upload_response = requests.post(
                    UPLOAD_URL,
                    files=files,
                    timeout=120
                )


            download_response = requests.get(
                DOWNLOAD_URL,
                timeout=60
            )
            download_response.raise_for_status()

        except requests.exceptions.RequestException as e:
            return HttpResponse(f"API Error: {e}", status=500)

        return HttpResponse(
            download_response.content,
            content_type="text/csv",
            headers={
                "Content-Disposition": "attachment; filename=cleaned.csv"
            }
        )

    return render(request, "uploader/upload.html")
