# -*- mode: python -*-

block_cipher = None

added_data_files = [
('./*.pdf','.'),
('./*.png','.'),
('./*.xml','.'),
('./testurls.txt','.'),
('./urls.txt','.')
]
added_binary_files = [
('C:/Drivers/WebDrivers/chromedriver.exe','.'),
('C:/Drivers/WebDrivers/geckodriver.exe','.')
]
a = Analysis(['Open24AutoGUI.py'],
             pathex=['C:\\Users\\tony.jansson.LEARNET\\Desktop\\Automatisering\\Python\\Open24Auto_5'],
             binaries=added_binary_files,
             datas=added_data_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Open24Auto',
          debug=False,
          strip=False,
          upx=False,
          console=False , icon='favicon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Open24Auto')
