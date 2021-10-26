# -*- mode: python ; coding: utf-8 -*-
import kivy
import kivymd
from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path
from PyInstaller.utils.hooks import collect_submodules
block_cipher = None

my_hidden_imports = collect_submodules('pyttsx3')

added_files = [
         ( 'C:\\wamp64\\www\\python_env\\Reminder_system\\new_login.kv', '.' ),
		 ( 'C:\\wamp64\\www\\python_env\\Reminder_system\\sign_up.kv', '.' ),
		 ( 'C:\\wamp64\\www\\python_env\\Reminder_system\\calendar.kv', '.' ),
		 ( 'C:\\wamp64\\www\\python_env\\Reminder_system\\Ttable.kv', '.' ),
		 ( 'C:\\wamp64\\www\\python_env\\Reminder_system\\scheduler.kv', '.' ),
		 ( 'C:\\wamp64\\www\\python_env\\Reminder_system\\user_menu.kv', '.' ),
		 ( 'C:\\wamp64\\www\\python_env\\Reminder_system\\home.kv', '.' ),
		 ( 'C:\\wamp64\\www\\python_env\\Reminder_system\\advan.txt', '.' ),
		 ( 'C:\\wamp64\\www\\python_env\\Reminder_system\\Advantages.txt', '.' ),
         ( 'C:\\wamp64\\www\\python_env\\Reminder_system\\inspirational_quotes.txt', '.' ),
         ( 'C:\\wamp64\\www\\python_env\\Reminder_system\\user_data.json', 'json' ),
		 ( 'C:\\wamp64\\www\\python_env\\Reminder_system\\images', 'images' ),
         ]
		 
a = Analysis(['main.py'],
             pathex=['C:\\wamp64\\www\\python_env\\Reminder_system'],
             binaries=[],
             datas=added_files,
             hiddenimports=my_hidden_imports,
             hookspath=[kivymd_hooks_path],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
			 
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
		  icon='C:\\wamp64\\www\\python_env\\Reminder_system\\icon_file.ico',
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
		  
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
			   *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
