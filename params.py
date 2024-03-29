import os

save_all_directory='../'

images_directory=os.path.join(save_all_directory, 'images')
cifarCSV=os.path.join(save_all_directory, 'CIFAR-10.csv')

cifar10_to_execute=os.path.join(save_all_directory, 'cifar-10-batches-py')
cifar100_to_execute=os.path.join(save_all_directory, 'cifar-100-python')

our_images_csv=os.path.join(save_all_directory, 'our_images.csv')
our_images_directory=os.path.join(save_all_directory, 'our_resized_images')

labels_json=os.path.join(save_all_directory, 'labels_names.json')
thresh_json=os.path.join(save_all_directory,'threshes.json')
model_path = 'keras_cifar10_trained_model_15_classes.h5'
valid_size = 0.18
train_size = 0.15