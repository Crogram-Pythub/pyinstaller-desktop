# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
APP_ID = 'org.pythub.pyinstaller-desktop'
APP_NAME = 'PyInstaller Desktop'
APP_NAME_DISPLAY = 'PyInstaller 桌面客户端'
APP_APP = 'PyThub PyInstaller Desktop.app'
APP_VERSION = '1.0.0'
APP_BUILD = 1
APP_COPYRIGHT = 'Copyright © 2020-present Jackson Dou All Rights Reserved.'
# HIDDEN_IMPORTS = ['PyInstaller.__main__']  # 源文件的依赖模块
EXCLUDES = ['altgraph', 'numpy', 'psutil', 'wheel', 'setuptools', 'PIL']  # 不需要打包的模块
UPX = True  # 如果有UPX安装(执行Configure.py时检测),会压缩执行文件(Windows系统中的DLL也会)
MacDeveloperID='Developer ID Application: CROGRAM INC. (4LWSS9P873)'


a = Analysis(['src/app.py'],
        pathex=['src'],
        binaries=[],
        datas=[],
        hiddenimports=None,
        hookspath=[],
        hooksconfig={},
        runtime_hooks=[],
        excludes=EXCLUDES,
        win_no_prefer_redirects=False,
        win_private_assemblies=False,
        cipher=block_cipher,
        noarchive=False)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
    a.scripts, [],
    exclude_binaries=True,
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=UPX,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None)
coll = COLLECT(exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=UPX,
    upx_exclude=[],
    name=APP_NAME)
app = BUNDLE(coll,
    name=APP_APP,
    icon='resources/app.icns',
    bundle_identifier=APP_ID,
    info_plist={
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME_DISPLAY,
        'CFBundleDevelopmentRegion': 'zh_CN',
        'CFBundleExecutable': APP_NAME,
        'CFBundlePackageType': 'APPL',
        'CFBundleSupportedPlatforms': ['MacOSX'],
        'CFBundleGetInfoString': 'Jackson Dou',
        'CFBundleIdentifier': APP_ID,
        'CFBundleShortVersionString': APP_VERSION,
        'CFBundleVersion': APP_BUILD,
        # 'CFBundleInfoDictionaryVersion': '6.0',
        'NSHighResolutionCapable': True,
        'LSApplicationCategoryType': 'public.app-category.utilities',
        'NSHumanReadableCopyright': APP_COPYRIGHT
    })
