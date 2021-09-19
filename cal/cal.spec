from kivy_deps import sd12, glew

# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['cal.py'],
             pathex=['C:\\Users\\skvin\\OneDrive\\Desktop\\course\\cal'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

a.datas +=[('code\calc.kv',
'C:\\Users\skvin\OneDrive\Desktop\course\cal\cal.kv',
'DATA')]

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='cal',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,TRee('C:\\Users\\skvin\\OneDrive\\Desktop\\course\\cal'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in 
               (sd12.dep_bins + 
               glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='cal')
