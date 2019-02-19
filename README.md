# Computer Vision experiments on coinshome.net datasets


#### [Test micro dataset with Inception V3 - micro-inception3-2019.02.04.ipynb](https://github.com/coin-vision/experiments/blob/master/experiments/micro-inception3-2019.02.04.ipynb)

#### [Test mini dataset with Inception V3 - mini-inception3-2019.02.06.ipynb](https://github.com/coin-vision/experiments/blob/master/experiments/mini-inception3-2019.02.06.ipynb)

#### [Test medium dataset with Inception V3  - medium-inception3-2019.02.10.ipynb](https://github.com/coin-vision/experiments/blob/master/experiments/medium-inception3-2019.02.10.ipynb)

```
medium-4000 dataset is used
[3-20] unique images per class for training set
first level augmentation x137 => [411 - 2,740] images/class max
5,091,605 total train images 
rest of the images go to validation set (without first level augmentation)
118,840 total validation images


After 1.5 epoc accuracy 0.98 top_5 accuracy 0.999 on tr set 
trainig steps per epoc:  79556.328125
Epoch 1/3
79557/79556 [==============================] - 109165s 1s/step - loss: 0.9718 - acc: 0.8000 - top_k_categorical_accuracy: 0.8911

Epoch 00001: saving model to /home/spa/coin-vision/ssd-data/medium-4000-20190205/inception_v3_20190212-085833.hdf5
Epoch 2/3
45939/79556 [================>.............] - ETA: 12:45:05 - loss: 0.0582 - acc: 0.9811 - top_k_categorical_accuracy: 0.9993

```

TODO: firs level augmentation can be much less (e.g. exclude rotation because it's used in keras ImageDataGenerator)

interesting that model.fit_generator() doesn't work with 'validation_data' when 'validation_data' doesn't have data for all classes. So, validation check was commented out for that run 
 
```

history = model.fit_generator(train_gen, 
                              epochs=train_epochs, 
                              steps_per_epoch=tr_steps_per_epoch,
                              shuffle=True, 
                              verbose=True,
#                              validation_data=test_gen,
#                              validation_steps=validation_steps, # fix me later if works
                              callbacks=callbacks_list)
                              
```

