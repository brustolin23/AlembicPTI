def remove_null_bytes(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()

    cleaned_content = content.replace(b'\x00', b'')

    with open(file_path, 'wb') as f:
        f.write(cleaned_content)

    print(f"Null bytes removed from {file_path}")


# Remover bytes nulos do arquivo models.py
remove_null_bytes('models.py')


# Verificar novamente se os bytes nulos foram removidos
def check_for_null_bytes(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
        if b'\x00' in content:
            print(f"Null byte found in {file_path}")
        else:
            print(f"No null byte found in {file_path}")


check_for_null_bytes('models.py')
