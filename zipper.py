import zipfile

with zipfile.PyZipFile("bar_pkg.zip", mode="w") as zip_pkg:
    zip_pkg.writepy("bar")

with zipfile.PyZipFile("bar_pkg.zip", mode="r") as zip_pkg:
    zip_pkg.printdir()
