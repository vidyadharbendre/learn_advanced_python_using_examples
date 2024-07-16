## Set Up Your Kaggle API Credentials

### Install Kaggle API

please ensure that you are in conda activated environment 
```bash
conda activate base
```

```basg
conda install -c conda-forge kaggle
```

### Download Kaggle API Token

Go to your Kaggle account settings: Kaggle Account.

Scroll down to the "API" section and click "Create New API Token". 
This will download a kaggle.json file containing your API credentials.
Move the kaggle.json File

Move the kaggle.json file to a secure location such as '~/.kaggle/':

```bash
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

### Using Kaggle API
Now that you have the Kaggle API installed, you can proceed with downloading datasets and submitting your solutions.

```bash
# Download competition data
kaggle competitions download -c <competition-name>



predictions = model.predict(test_data_scaled)
submission = pd.DataFrame({'Id': test_data['Id'], 'Prediction': predictions})
submission.to_csv('submission_1.csv', index=False)


# Submit predictions
#kaggle competitions submit -c <competition-name> -f <submission-file> -m "Your submission message"
kaggle competitions submit -c <competition-name> -f submission_1.csv -m "Your submission message"
```


