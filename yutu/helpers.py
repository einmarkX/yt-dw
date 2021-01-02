def ceksize(filesize: 0) -> str:
    """ parameter : int (byte) """
    ukuran = "bit"
    if (filesize < 1000):
        ukuran = "byte"
        filesize = (filesize/1000)
    elif (filesize < 1000000):
        ukuran = "kB"
        filesize = (filesize/100000)
    elif (filesize >= 1000000):
        ukuran = "MB"
        filesize = (filesize/1000000)

    return "{0:.1f} {1}".format(filesize, ukuran)

def pilihAngka(tanya)-> int:
    try:
        pilih = int(input(tanya))
    except ValueError:
        print("Input Invalid")
        pilihAngka(tanya)

    return pilih