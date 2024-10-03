# import tensorflow as tf
# from PIL import Image, ImageFile
# from pathlib import Path

# ImageFile.LOAD_TRUNCATED_IMAGES = True

# class PrepareBaseModel:
#     def __init__(self, config):
#         self.config = config

#     def get_base_model(self):
#         try:
#             # Load VGG16 base model
#             self.model = tf.keras.applications.vgg16.VGG16(
#                 input_shape=self.config.params_image_size,
#                 weights=self.config.params_weights,
#                 include_top=self.config.params_include_top
#             )
#             print("Base model loaded successfully.")
#         except Exception as e:
#             print(f"Error loading base model: {e}")
#             raise  # Re-raise the exception after logging it

#         try:
#             # Save the base model
#             self.save_model(path=self.config.base_model_path, model=self.model)
#         except Exception as e:
#             print(f"Error saving base model: {e}")
#             raise  # Re-raise the exception after logging it

#     def load_and_preprocess_image(self, image_path):
#         try:
#             # Load the image using PIL (this helps with truncated images)
#             image = Image.open(image_path)
#             image = image.resize((224, 224))  # Resize to VGG16 input size

#             # Convert the image to a NumPy array and normalize pixel values
#             image_array = tf.keras.preprocessing.image.img_to_array(image)
#             image_array = tf.keras.applications.vgg16.preprocess_input(image_array)  # Normalize the image
#             return image_array
#         except Exception as e:
#             print(f"Error processing image {image_path}: {e}")
#             return None  # Skip the corrupted image

#     @staticmethod
#     def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
#         try:
#             if freeze_all:
#                 for layer in model.layers:
#                     layer.trainable = False
#             elif freeze_till is not None and freeze_till > 0:
#                 for layer in model.layers[:-freeze_till]:
#                     layer.trainable = False

#             flatten_in = tf.keras.layers.Flatten()(model.output)
#             prediction = tf.keras.layers.Dense(
#                 units=classes,
#                 activation="softmax"
#             )(flatten_in)

#             full_model = tf.keras.models.Model(inputs=model.input, outputs=prediction)

#             full_model.compile(
#                 optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
#                 loss=tf.keras.losses.CategoricalCrossentropy(),
#                 metrics=["accuracy"]
#             )

#             full_model.summary()
#             return full_model
#         except Exception as e:
#             print(f"Error preparing full model: {e}")
#             raise

#     def update_base_model(self):
#         try:
#             self.full_model = self._prepare_full_model(
#                 model=self.model,
#                 classes=self.config.params_classes,
#                 freeze_all=True,
#                 freeze_till=None,
#                 learning_rate=self.config.params_learning_rate
#             )
#         except Exception as e:
#             print(f"Error updating base model: {e}")
#             raise

#         try:
#             self.save_model(path=self.config.updated_base_model_path, model=self.full_model)
#         except Exception as e:
#             print(f"Error saving updated base model: {e}")
#             raise

#     @staticmethod
#     def save_model(path, model):
#         try:
#             model.save(path)
#             print(f"Model saved successfully at {path}")
#         except Exception as e:
#             print(f"Error saving model: {e}")
#             raise

# # Example usage:

# config = PrepareBaseModelConfig(
#     params_image_size=(224, 224, 3),
#     params_weights='imagenet',
#     params_include_top=False,
#     base_model_path=Path('./base_model.h5'),
#     updated_base_model_path=Path('./updated_base_model.h5'),
#     params_classes=4,
#     params_learning_rate=0.0001
# )

# model_preparer = PrepareBaseModel(config)
# model_preparer.get_base_model()
# model_preparer.update_base_model()



import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )

        self.save_model(path=self.config.base_model_path, model=self.model)

    

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model
    
    
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    
        
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)