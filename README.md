# SemEval 2017 Task 10

Conditional Random Fields for Subtask A and Subtask B of SemEval 2017 Task 10.
The task is "Extracting Keyphrases and Relations from Scientific Publications".
* Subtask A : Identification of keyphrases
* Subtask B : Classification of keyphrases

The data and scripts for the task can be obtained at: https://scienceie.github.io/resources.html <br>
CRF++ can be obtained at: https://taku910.github.io/crfpp/

Files and Folders
* CRF++\-0.58 : Folder containing files for CRF++. Contains "crf_learn.exe" for training, and "crf_test.exe" for testing.
* scienceie2017_dev/dev : Contains test data
* scienceie2017_train/train2: Contains training data
* scienceie2017_scripts : Contains evaluation script "eval.py"
* Test_Out_Boundary : Output files for Subtask A
* Test_Out : Output files for Subtask B
* all_ff.ffb : Feature file for training of Subtask A. Contains the features of all the training files.
* all_ff.ffb : Feature file for training of Subtask B. Contains the features of all the training files.
* template_task1.txt : Template file for training for Subtask A.
* template.txt : Template file for training for Subtask B.

How to train and test for Subtask A:
```shell
python create_features_task1.py
"CRF++\-0.58"/crf_learn template_task1.txt all_ff.ffb model_boundary.crf
python run_boundary.py
python evaluate_boundary.py
scienceie2017_scripts/eval eval.py scienceie2017_dev/dev Test_Out_Boundary/ types
```

How to train and test for Subtask B:
```shell
python create_features.py
"CRF++\-0.58"/crf_learn template.txt all_ff.ff model.crf
python run.py
python evaluate.py
scienceie2017_scripts/eval eval.py scienceie2017_dev/dev Test_Out/ rel
```
