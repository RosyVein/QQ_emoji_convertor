import os

def isTarget(filepath):
    # Check if the file is a emoji file by QQ
    # Check 1: file don't have extension
    if os.path.splitext(filepath)[1] != '':
        return False
    # Check 2: file name is 32 characters
    filename = os.path.basename(filepath)
    if len(filename) != 32:
        return False
    return True

# it may only have gif format and it will be unnecessary
def detect_image_format(data: bytes):
    if data.startswith(b'\xFF\xD8\xFF'):
        return 'jpg'
    elif data.startswith(b'\x89PNG\r\n\x1a\n'):
        return 'png'
    elif data.startswith(b'GIF87a') or data.startswith(b'GIF89a'):
        return 'gif'
    elif data.startswith(b'BM'):
        return 'bmp'
    elif data.startswith(b'RIFF') and data[8:12] == b'WEBP':
        return 'webp'
    else:
        return None

def rename_with_extension(filepath):
    with open(filepath, 'rb') as f:
        header = f.read(16)

    fmt = detect_image_format(header)
    if fmt:
        new_filepath = filepath + '.' + fmt
        if not os.path.exists(new_filepath):
            os.rename(filepath, new_filepath)
            print(f"Renamed to: {new_filepath}")
        else:
            print(f"Target file already exists: {new_filepath}")
    else:
        print(f"Unknown format: {filepath}")

def process_file(filepath):
    with open(filepath, 'rb') as f:
        data = bytearray(f.read())

    block_size = 50
    xor_len = 20
    xor_mask = 0xFF

    for i in range(0, len(data), block_size):
        for j in range(i, min(i + xor_len, len(data))):
            data[j] ^= xor_mask

    with open(filepath, 'wb') as f:
        f.write(data)

    print(f"Processed: {filepath}")

def batch_process(folder_dir):
    for root, _, files in os.walk(folder_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            if isTarget(filepath):
                process_file(filepath)
                rename_with_extension(filepath)

folder_path = input("Enter the path of the folder: ")
batch_process(folder_path)