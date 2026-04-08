try:
    import requests, os, shutil
except:
    import os
    os.system('pip install requests')
    import requests, shutil
try:
    from run_check import *
except:pass
dir = 'Pmin_Sources'
dir2 = 'Input Text'
dir3 = 'com.garena.game.kgvn'
os.makedirs(dir, exist_ok=True)
os.makedirs(dir2, exist_ok=True)
os.makedirs(dir3, exist_ok=True)

url = {
    "version.txt": "https://raw.githubusercontent.com/DoanNguyenHaNam/SourceGame/main/version.txt",
    "tool_run.py": "https://raw.githubusercontent.com/DoanNguyenHaNam/SourceGame/main/tool_run_ngannganmod.py",
    "Resources.zip": "https://raw.githubusercontent.com/DoanNguyenHaNam/SourceGame/main/Resources.zip",
    "check.zip": "https://raw.githubusercontent.com/DoanNguyenHaNam/SourceGame/main/check.zip",
    "back.txt":"https://raw.githubusercontent.com/DoanNguyenHaNam/SourceGame/main/back.txt",
    "skin.txt":"https://raw.githubusercontent.com/DoanNguyenHaNam/SourceGame/main/skin.txt",
    "haste.txt":"https://raw.githubusercontent.com/DoanNguyenHaNam/SourceGame/main/haste.txt"
}
def main():
    try:
        with open(f'version.txt','rb') as f:
            check=f.read()
            response = requests.get(url['version.txt'])
            if response.content == check:
                print(f'Không Update Sources')
                return
    except:
        pass

    shutil.rmtree(dir)
    os.makedirs(dir, exist_ok=True)

    shutil.rmtree(dir2)
    os.makedirs(dir2, exist_ok=True)

    shutil.rmtree(dir3)

    for file in url:
        response = requests.get(url[file])
        output = file
        if 'zip' in file:
            output = f'{dir}/{output}'

        if 'txt' in file and 'version' not in file:
            output = f'{dir2}/{output}'

        if file == "check.zip":
            try:
                giainen()
                os.system(f'python find_check.py')
            except Exception as bug:
                print(bug)
                pass
        try:
            with open(output, "wb") as f:
                f.write(response.content)

            if 'zip' in file:
                shutil.unpack_archive(output, dir)
        except: pass

    print("Tải xong!")
    return

main()