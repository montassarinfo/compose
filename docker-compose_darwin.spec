# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['bin/docker-compose'],
             pathex=['.'],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='docker-compose',
          debug=False,
          strip=False,
          upx=True,
          console=True,
          bootloader_ignore_signals=True)
coll = COLLECT(exe,
          a.binaries,
          a.zipfiles,
          a.datas,
          [
            (
                'compose/config/config_schema_v1.json',
                'compose/config/config_schema_v1.json',
                'DATA'
            ),
            (
                'compose/config/config_schema_v4.0.json',
                'compose/config/config_schema_v4.0.json',
                'DATA'
            ),
            (
                'compose/GITSHA',
                'compose/GITSHA',
                'DATA'
            )
          ],
          strip=False,
          upx=True,
          upx_exclude=[],
          name='docker-compose-Darwin-x86_64')
