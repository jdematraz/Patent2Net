# -*- mode: python -*-
a = Analysis(['FusionIramuteq2.py'],
             pathex=['D:\\Doc-David\\Developpement\\SpyderWorkspace\\Patent2Net\\Patent2Net\\Patent2Net\\Development'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='FusionIramuteq2.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='FusionIramuteq2')
