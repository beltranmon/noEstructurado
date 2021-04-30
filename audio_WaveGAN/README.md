# WaveGAN

Práctica de audio de Anñalisis de datos no estructurados

Pablo Mena

Beltrán Rodríguez-Mon


## Datasets

WaveGAN se puede entrenar con cualquier dataset de datos **tras haberlo preprocesado**. En nuestro caso hemos omitido el entrenamiento y hemos utilizado el modelo ya entrenado, pero éste se puede realizar con un dataset como el siguiente:

- [Bach piano performances](http://deepyeti.ucsd.edu/cdonahue/wavegan/data/mancini_piano.tar.gz)

## Train a WaveGAN

Para comenzar (o continuar) el entrenamiento con datos mínimamente grandes (más de un par de segundos):

```
export CUDA_VISIBLE_DEVICES="0"
python train_wavegan.py train ./train \
	--data_dir ./data/dir_with_data
```

Si el dataset es de efectos de sonido corto:

```
export CUDA_VISIBLE_DEVICES="0"
python train_wavegan.py train ./train \
	--data_dir ./data/dir_with_data \
	--data_first_slice \
	--data_pad_end \
	--data_fast_wav
```
WaveGAN se puede entrenar en CPU, pero es extremadamente lento: 

flag `--data_prefetch_gpu_num -1` al ejecutar.

