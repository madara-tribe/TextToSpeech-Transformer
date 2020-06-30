# TextToSpeech-Transformer

## model stracture and process to generate audio

TextToSpeech-Transformer is based on [Neural Speech Synthesis with Transformer Network](https://arxiv.org/abs/1809.08895).
similar model is tactron2.

<b>model structure</b>


<b>process to generate audio</b>



## training step by generate audio
1. Download dataset you like(The LJ Speech Dataset is recommended)
2. Adjust hyper parameter in ```hyperparams.py```. Especially, set dataset specified folder.
3. ```python prepare_data.py```
4. ```python train_transformer.py```
5. ```train_postnet.py```
6. finally generate audio by ```generate_audio.py```


## Requirements


## data

dataset is [The LJ Speech Dataset](https://keithito.com/LJ-Speech-Dataset/)

## sample generated audio

When text is <b>「it dose not look like you are gonna」</b>
[generated audio1](https://www.instagram.com/p/CCDXhJBlqmr/?igshid=1dufrqobhvk0f)

When text is <b>「I never made it to sixth grade」</b>
[generated audio2](https://www.instagram.com/p/CCDXV6OFRYy/?igshid=6czncaupql0s)


## references

- [Tansformer-TTS like tactron](https://github.com/soobinseo/Transformer-TTS)
- [Prretrain model](https://drive.google.com/drive/folders/1r1tdgsdtipLossqD9ZfDmxSZb8nMO8Nf)




