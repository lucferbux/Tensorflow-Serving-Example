from tensorflow import keras
import tempfile
import os


def save_model(model):
    MODEL_DIR = tempfile.gettempdir()
    export_path = os.path.join(MODEL_DIR, str(1))

    keras.models.save_model(
        model,
        export_path,
        overwrite=True,
        include_optimizer=True,
        save_format=None,
        signatures=None,
        options=None
    )

    print(f'\nSaved model: {MODEL_DIR}')

    print(
        f"docker run -p 8501:8501 --privileged=true --platform linux/amd64 --mount type=bind,source={MODEL_DIR},target=/models/fashion_model -e MODEL_NAME=fashion_model -t tensorflow/serving")
    print(
        f"docker run -p 8501:8501 --privileged=true --platform linux/arm64 --mount type=bind,source={MODEL_DIR},target=/models/fashion_model -e MODEL_NAME=fashion_model -t emacski/tensorflow-serving")

    return export_path
