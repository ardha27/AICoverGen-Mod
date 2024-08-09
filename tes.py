import urllib.request
import os
import gdown

def download_online_model(url, dir_name):
    try:
        zip_name = url.split('/')[-1]
        extraction_folder = os.path.join("", dir_name)
        if os.path.exists(extraction_folder):
            print(f'[!] {dir_name} Model already exists!')

        if 'huggingface.co' in url:
            urllib.request.urlretrieve(url, zip_name)

        if 'pixeldrain.com' in url:
            zip_name = dir_name + '.zip'
            url = f'https://pixeldrain.com/api/file/{zip_name}'
            urllib.request.urlretrieve(url, zip_name)

        elif 'drive.google.com' in url:
            # Extract the Google Drive file ID
            zip_name = dir_name + '.zip'
            file_id = url.split('/')[-2]
            output = os.path.join('.', f'{dir_name}.zip')  # Adjust the output path if needed
            gdown.download(id=file_id, output=output, quiet=False)

        print(f'[+] {dir_name} Model successfully downloaded!')
        # extract_zip(extraction_folder, zip_name)
        return f'[+] {dir_name} Model successfully downloaded!'

    except Exception as e:
        print(f'[!] Error while downloading {dir_name} model!')

if __name__ == '__main__':
    url = 'https://drive.google.com/file/d/1-DQi6KZVnoSaI7OyiHEWsG_QgS7tYlJp/view?usp=drive_link'
    download_online_model(url, 'test')