#!bin/bash
read -p "train step:" step
read -p "Do you want to see performance?[Y/N]" ChooseToTensorBoard
echo -e "Please enter your data path: "
read DATA_PATH
cd /home/user/tensorflow/seq2seq
#CUDA add to path
export LD_LIBRARY_PATH=/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
source ~/tensorflow/bin/activate
#you can change the type of data 
export VOCAB_SOURCE=${DATA_PATH}/Word
export VOCAB_TARGET=${DATA_PATH}/Word
export TRAIN_SOURCES=${DATA_PATH}/vneseTrain
export TRAIN_TARGETS=${DATA_PATH}/englishTrain
export DEV_SOURCES=${DATA_PATH}/vneseTest
export DEV_TARGETS=${DATA_PATH}/englishTest
export DEV_TARGETS_REF=${DATA_PATH}/englishTest
export TRAIN_STEPS=$step
export MODEL_DIR=/home/user/Documents/nmt_tutorial
echo "we will save train log in /home/user/Documents/nmt_tutorial "
echo "step = $step"
sleep 3
mkdir -p $MODEL_DIR
#CONFIG CAN BE CHANGE
python -m bin.train \
  --config_paths="
      ./example_configs/nmt_small.yml,
      ./example_configs/train_seq2seq.yml,
      ./example_configs/text_metrics_bpe.yml" \
  --model_params "
      vocab_source: $VOCAB_SOURCE
      vocab_target: $VOCAB_TARGET" \
  --input_pipeline_train "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - $TRAIN_SOURCES
      target_files:
        - $TRAIN_TARGETS" \
  --input_pipeline_dev "
    class: ParallelTextInputPipeline
    params:
       source_files:
        - $DEV_SOURCES
       target_files:
        - $DEV_TARGETS" \
  --batch_size 32 \
  --train_steps $TRAIN_STEPS \
  --output_dir $MODEL_DIR 
read -p "Do you want to make predictions?[Y/N]" ChooseToPredict
if [ "${ChooseToPredict}" = "Y" ]
then
    echo -e "Please Enter Prediction File Path:"
    read PredictPath
    echo "We will log the prediction in /home/user/Documents/nmt_tutorial/pred"
    sleep 3
    export PRED_DIR=${MODEL_DIR}/pred
    mkdir -p ${PRED_DIR}
    python -m bin.infer \
      --tasks "
        - class: DecodeText" \
      --model_dir $MODEL_DIR \
      --input_pipeline "
        class: ParallelTextInputPipeline
        params:
          source_files:
            - $DEV_SOURCES" \
      >  ${PRED_DIR}/predictions.txt
fi
if [ "${ChooseToTensorBoard}" = "Y" ]
then
   tensorboard --logdir $MODEL_DIR
fi
