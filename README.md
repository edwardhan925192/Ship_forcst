# Setting  
!unzip /content/drive/MyDrive/data/hyundai/hyundai.zip  
!git clone https://github.com/edwardhan925192/Ship_forcst.git  
%cd /content/Ship_forcst  

# Ship_forecast  
```markdown
!python main.py\  
--lists ARI_CO SHIP_TYPE_CATEGORY\  
--file_path1 '/content/Ship_forcst/train.csv' \  
--file_path2 '/content/Ship_forcst/test.csv' \  
--load \  
--preprocess \  
--extract_dates \  
--datetime_col 'ATA'\  
--model_name 'autogluon'\  
--auto_time 4  
```

# Submission  
```markdown
from submission import get_submission  
get_submission(pred_path, test_path, name)  
```


