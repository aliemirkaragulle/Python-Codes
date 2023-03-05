extension_name = input("File name: ")

dot_indices = []
for i in range(len(extension_name)):
    if extension_name[i] == ".":
        dot_indices.append(i)

extension = []
if len(dot_indices) > 0:
    j = max(dot_indices)
    while j != len(extension_name):
        extension.append(extension_name[j])
        j += 1
    extension = "".join(extension).strip().lower()
else:
    extension = ""

match extension:
    case ".gif":
        print("image/gif")
    case ".jpg" | ".jpeg":
        print("image/jpeg")
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".txt":
        print("text/plain")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")