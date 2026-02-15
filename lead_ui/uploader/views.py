import requests
from django.shortcuts import render
from django.http import HttpResponse

UPLOAD_URL = "https://lead-automation-api-2e5g.onrender.com/upload/"
DOWNLOAD_URL = "https://lead-automation-api-2e5g.onrender.com/download"

def upload_file(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        if not file:
            return HttpResponse("No file has been choosen.", status=400)

        try:
            requests.get("https://lead-automation-api-2e5g.onrender.com/docs", timeout=60)
        except:
            pass 

        try:
            # مرحله 2: آپلود فایل با stream
            files = {"file": (file.name, file, "text/csv")}
            upload_response = requests.post(UPLOAD_URL, files=files, timeout=300)
            upload_response.raise_for_status()

            download_response = requests.get(DOWNLOAD_URL, timeout=300)
            download_response.raise_for_status()

        except requests.exceptions.Timeout:
            return HttpResponse(
                "Conection to the API timeout",
                status=504
            )
        except requests.exceptions.ConnectionError:
            return HttpResponse(
                "Conection to the API didn't succeed",
                status=503
            )
        except requests.exceptions.HTTPError as e:
            return HttpResponse(f"HTTP Error: {e.response.status_code}", status=e.response.status_code)
        except Exception as e:
            return HttpResponse(f"Unexcepted Error : {e}", status=500)

        return HttpResponse(
            download_response.content,
            content_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=cleaned.csv"}
        )

    return render(request, "uploader/upload.html")
