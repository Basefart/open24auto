# -*- mode: python -*-

block_cipher = None


a = Analysis(['Open24AutoGUI.py'],
             pathex=['C:\\Users\\tony.jansson.LEARNET\\Desktop\\Automatisering\\Python\\Open24Auto_5'],
             binaries=[],
             datas=[],
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
          name='Open24AutoGUI',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='favicon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Open24AutoGUI')