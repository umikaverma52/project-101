import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def uploadFile(self,importFrom,exportTo):
        dbx=dropbox.Dropbox(self.access_token)
        file=open(importFrom,"rb")
        dbx.files_upload(file.read(),exportTo)


access_token="sl.BKfaKvXLpGsx7vTipMCA5v4_ZA7h_YxPneh2zYDabadscnoyOXGQhGLsu_MK2qUjpCXe--SnJ3fI74A2mk38PPnm1mIImiCSSmIkwIXjEiZbfBFmQRQuZYq3TwiyHs5fOqwvIOXBWFdE"
td=TransferData(access_token)

importFrom="project.txt"
exportTo="/whitehat JR./project.txt"
td.uploadFile(importFrom,exportTo)