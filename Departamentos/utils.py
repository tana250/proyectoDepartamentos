def guardarArchivo(f):
    with open(f"archivo.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)