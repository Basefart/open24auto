# -*- mode: python -*-

block_cipher = None

added_data_files = [
('./*.pdf','.'),
('./*.png','.'),
('./*.xml','.'),
('./urls.txt','.')
]
added_binary_files = [
('C:/Drivers/WebDrivers/chromedriver.exe','.'),
('C:/Drivers/WebDrivers/geckodriver.exe','.')
]
a = Analysis(['Open24AutoGUI.py'],
             pathex=['C:\\Users\\tony.jansson.LEARNET\\Documents\\GitHub\\open24auto',
             'C:\\Windows\\WinSxS\\amd64_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.17134.1_none_ace56707ea44b3c5',
             'C:\\Windows\\WinSxS\\amd64_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.17134.1_none_2113a40cfedc7953'],
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
