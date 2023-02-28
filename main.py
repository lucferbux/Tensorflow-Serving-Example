from model import model_training
from persistance import persistance


if __name__ == "__main__":
    train_images, train_labels, test_images, test_labels = model_training.prepare_data()
    model = model_training.train_model(train_images, train_labels)
    model_training.evaluate_model(model, test_images, test_labels)
    persistance.save_model(model)
