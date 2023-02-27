from tensorflow import keras
import tempfile
import os

def save_model(model):
    MODEL_DIR = tempfile.gettempdir()
    export_path = os.path.join(MODEL_DIR, str(1))
    print(f'MODEL_DIR = {MODEL_DIR}\n')
    print(f'export_path = {export_path}\n')

    keras.models.save_model(
        model,
        export_path,
        overwrite=True,
        include_optimizer=True,
        save_format=None,
        signatures=None,
        options=None
    )

    print(f'\nSaved model: ${export_path}')

    return export_path

